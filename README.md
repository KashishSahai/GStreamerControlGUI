# GStreamerControlGUI

**GStreamerControlGUI** is a Python-based graphical interface that allows users to play local video files and stream them via RTSP over a network. Built with Tkinter and powered by GStreamer, it combines simplicity in design with robust streaming capabilities.

---

## 🚀 Features

- Browse and select local video files via GUI
- Play videos locally using GStreamer
- Start/stop an RTSP video stream to share across devices
- Supports common formats like `.mp4`, `.avi`, `.mkv`
- Platform-independent (tested on Linux and Windows)

---

## 🛠 Requirements

- Python 3.6 or newer
- [GStreamer 1.18+](https://gstreamer.freedesktop.org/download/)
- PyGObject
- Tkinter (comes pre-installed with Python on most systems)

Install dependencies via pip:

```bash
pip install PyGObject
```

---

## 📂 Project Structure

```
GStreamerControlGUI/
├── frontend.py          # Tkinter-based GUI application
├── rtspserver.py        # GStreamer RTSP streaming backend
├── requirements.txt     # Python dependencies (optional)
└── README.md            # Project documentation
```

---

## 🧭 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/GStreamerControlGUI.git
cd GStreamerControlGUI
```

### 2. Launch the GUI
```bash
python frontend.py
```

### 3. Using the App

- **Browse** to select a local video file
- Click **Play Video** to preview it locally
- Click **Start RTSP Stream** to launch the backend RTSP stream
- Access the stream at:  
  `rtsp://localhost:8554/stream`
- Click **Stop RTSP Stream** when done

---

## 🔭 Future Enhancements

- Embed video output directly into GUI using Gtk drawing area  
- Add webcam/live camera RTSP support  
- Stream status indicators and logs in GUI  
- Basic stream authentication for secure RTSP access  
- Docker support and CLI interface
