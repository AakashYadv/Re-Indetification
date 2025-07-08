
import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load YOLOv11 model
model = YOLO("models/yolov11_player.pt")  # Make sure model is placed here

# Initialize Deep SORT tracker
tracker = DeepSort(max_age=30, n_init=2)

# Open video
cap = cv2.VideoCapture("15sec_input_720p.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter("output_tracking.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    detections = []

    for box in results.boxes:
        cls_id = int(box.cls[0].item())
        if cls_id != 0:
            continue  # Skip non-player classes
        x1, y1, x2, y2 = box.xyxy[0]
        conf = float(box.conf[0])
        detections.append(([x1.item(), y1.item(), (x2 - x1).item(), (y2 - y1).item()], conf, 'player'))

    tracks = tracker.update_tracks(detections, frame=frame)
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        l, t, r, b = map(int, track.to_ltrb())
        cv2.rectangle(frame, (l, t), (r, b), (0, 255, 0), 2)
        cv2.putText(frame, f'Player {track_id}', (l, t - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    out.write(frame)
    cv2.imshow("Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
