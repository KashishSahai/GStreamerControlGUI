import gi
import tkinter as tk
from tkinter import filedialog
gi.require_version('Gtk', '3.0')
gi.require_version('Gst', '1.0')
from gi.repository import Gtk, Gst, GdkX11
Gst.init(None)

class VideoPlayer:
    def __init__(self,root):
        self.root=root
        self.root.title("Gstreamer Video Player")

        self.entry=tk.Entry(root,width=50)
        self.entry.pack(pady=10)

        self.browse_button=tk.Button(root,text="Browse",command=self.browse_file)
        self.browse_button.pack(pady=10)

        self.play_button=tk.Button(root,text="Play Video",command=self.play_video)
        self.play_button.pack(pady=10)

        self.video_widget=Gtk.DrawingArea()
        self.video_widget.set_size_requests(1800,1600)

        self.gtk_window=Gtk.window()
        self.gtk_window.set_default_size(1800,1600)
        self.gtk_window.set_child(self.video_widget)
        self.gtk_window.present()
        
        # Create GStreamer pipeline
        self.pipeline = Gst.ElementFactory.make("playbin","play_pipeline")

        def browse_file(self):
            file_path = filedialog.askopenfilename(title="Select Video File",filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
            if file_path:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, file_path)
        
        def play_video(self):
            file_path= self.entry.get()
            if file_path:
                if file_path.startswith(("https://","http://","rtsp://")):
                    self.pipeline=Gst.parse_launch(f" playbin uri={file_path}")
                elif file_path.startswith(("udp://")):
                    self.pipeline=Gst.parse_launch(f"udpsrc uri={file_path}!decodebin!videoconvert!autovideosink")
                else:
                    self.pipeline=Gst.parse_launch(f" playbin uri=file://{file_path}")
                self.pipeline.set_state(Gst.State.PLAYING)

        # Create video sink (GTK-compatible)
        self.video_sink = Gst.ElementFactory.make("autovideosink", "video_sink")
        self.playbin=Gst.ElementFactory.make("playbin","play_pipeline")
        self.pipeline.set_property("uri", file_path)

        # Build Tkinter UI for file selection
        root = tk.Tk()
        player=VideoPlayer(root)
        root.mainloop()
