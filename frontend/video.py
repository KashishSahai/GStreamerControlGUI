import gi
import tkinter as tk
from tkinter import filedialog
import subprocess
import sys
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

        self.stream_button = tk.Button(root, text="Start RTSP Stream", command=self.start_rtsp)
        self.stream_button.pack(pady=10)

        self.stop_stream_button = tk.Button(root, text="Stop RTSP Stream", command=self.stop_rtsp)
        self.stop_stream_button.pack(pady=10)

        self.rtsp_process = None
        self.pipeline = None

        def browse_file(self):
            file_path = filedialog.askopenfilename(title="Select Video File",filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
            if file_path:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, file_path)
        
        def play_video(self):
            file_path= self.entry.get()
            def play_video(self):
        file_path = self.entry.get()
        if file_path:
            if file_path.startswith(("rtsp://", "http://", "https://")):
                uri = file_path
            else:
                uri = "file://" + file_path
            try:
                self.pipeline = Gst.parse_launch(f"playbin uri={uri}")
                self.pipeline.set_state(Gst.State.PLAYING)
            except Exception as e:
                print("GStreamer error:", e)

    def start_rtsp(self):
        video_file = self.entry.get()
        if video_file:
            if self.rtsp_process is None:
                self.rtsp_process = subprocess.Popen([sys.executable, "rtspserver.py", video_file])
                print("RTSP stream started.")

    def stop_rtsp(self):
        if self.rtsp_process:
            self.rtsp_process.terminate()
            self.rtsp_process = None
            print("RTSP stream stopped.")
            
# Build Tkinter UI for file selection
root = tk.Tk()
player=VideoPlayer(root)
root.mainloop()
