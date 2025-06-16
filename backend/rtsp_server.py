import gi
import os

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import GstRtspServer, GLib, Gst

Gst.init(None)

def kill_previous_server(port):
    os.system(f"fuser -k {port}/tcp")

class VideoStreamFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self, video_file):
        super().__init__()
        self.video_file = video_file
        self.set_launch(f"( filesrc location={video_file} ! qtdemux ! avdec_h264 ! videoconvert ! x264enc ! rtph264pay name=pay0 pt=96 )")


class RTSPServerManager:
    def __init__(self, video_file):
        self.video_file = video_file
        self.server = GstRtspServer.RTSPServer()
        self.server.set_service("8554")
        self.server.set_address("0.0.0.0")  # Allows local network access
        mount_points = self.server.get_mount_points()
        factory = VideoStreamFactory(video_file)
        mount_points.add_factory("/stream", factory)

    def start_server(self):
        self.server.attach(None)
        print(f"RTSP Server running at rtsp://localhost:8554/stream")
        
        try:
            loop = GLib.MainLoop()
            loop.run()
        except KeyboardInterrupt:
            self.stop_server()

    def stop_server(self):
        self.server.dispose()
        print("RTSP Server stopped.")

if __name__ == "__main__":
    port = "8554"
    kill_previous_server(port)
    
    video_file = input("Enter the path of your MP4 file: ")
    server = RTSPServerManager(video_file)
    server.start_server()
