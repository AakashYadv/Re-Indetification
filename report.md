# 📊 Player Re-ID Tracking — Report

## 🧠 Approach

- Used YOLOv11 fine-tuned model for detecting players, ball, and referee.
- Used StrongSORT with `osnet_x1_0` Re-ID model for consistent ID assignment.
- Implemented tracking pipeline with FastAPI endpoint for video upload and result retrieval.

## ⚙️ Techniques Tried

- Deep SORT with default embedder (not reliable for long disappearance)
- StrongSORT with Re-ID backbone (better re-identification)

## ❗ Challenges Faced

- Re-ID inconsistencies on CPU-only setups
- Real-time performance degraded without GPU
- Render CPU deployment needed frame skipping

## ✅ If Incomplete

- Could integrate automatic download of model weights at runtime
- Could visualize ID tracks better (color-coded IDs)
- With GPU access, real-time tracking and re-ID would be feasible