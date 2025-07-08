# Player Re-Identification and Tracking (YOLOv11 + StrongSORT)

This project tracks players in a football match video and assigns consistent IDs even if players leave and re-enter the frame. It uses a YOLOv11 object detector and StrongSORT for tracking and Re-ID.

---

## ✅ How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Add Models

- Place your YOLOv11 model in `models/yolov11_player.pt`
- Place Re-ID model (`osnet_x1_0.pth`) in `reid/osnet_x1_0.pth`

### 3. Run the System

```bash
python main.py
```

The input video must be named `15sec_input_720p.mp4` and placed in the root folder.  
The output will be saved as `output_tracking.mp4`.

---

## 📦 Deployment on Render

You can deploy this system using `render.yaml`. Use `app.py` for FastAPI interface.