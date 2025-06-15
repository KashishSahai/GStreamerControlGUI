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


def start_rtsp_server(video_file):
    server = GstRtspServer.RTSPServer()
    server.set_service("8554")
    server.set_address("172.25.223.28")
    mount_points = server.get_mount_points()
    factory = VideoStreamFactory(video_file)
    mount_points.add_factory("/stream", factory)
    server.attach(None)

    print(f"RTSP Server running... Open in VLC: rtsp://172.25.223.28:8554/stream")
    
    loop = GLib.MainLoop()
    loop.run()

if __name__ == "__main__":
    port="8554"
    kill_previous_server(port)
    video_file = input("Enter the path of your MP4 file: ")
    start_rtsp_server(video_file)
