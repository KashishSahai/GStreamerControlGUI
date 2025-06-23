import gi
import os
import sys
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
        self.server.set_address("0.0.0.0")
        mount_points = self.server.get_mount_points()
        factory = VideoStreamFactory(self.video_file)
        mount_points.add_factory("/stream", factory)

    def start_server(self):
        self.server.attach(None)
        print("RTSP Server running at rtsp://localhost:8554/stream")
        loop = GLib.MainLoop()
        loop.run()
        
if __name__ == "__main__":
    f len(sys.argv) < 2:
        print("Usage: python rtspserver.py <video_file_path>")
        sys.exit(1)

    video_path = sys.argv[1]
    #If running independently take input for the source file
    kill_previous_server("8554")
    server = RTSPServerManager(video_path)
    server.start_server()
