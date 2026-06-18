import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO
import torch

def run_lr_finder(model_path, data_yaml, lr_start=1e-6, lr_end=1, num_steps=100):
    model = YOLO(model_path)

    lrs = np.logspace(np.log10(lr_start), np.log10(lr_end), num_steps)
    losses = []

    for i, lr in enumerate(lrs):
        print(f"[{i+1}/{num_steps}] Training with lr={lr:.6f}")
        results = model.train(data=data_yaml, imgsz=640, epochs=1, batch=16, lr0=lr, verbose=False)
        # Get final training loss from history
        loss = results['metrics']['train/box_loss'] + results['metrics']['train/cls_loss']
        losses.append(loss)
        # Optional: clean cache between runs
        torch.cuda.empty_cache()

    return lrs, losses

# === Run it ===
model_path = 'runs/detect/train3/weights/last.pt'       # Or your custom checkpoint .pt
data_yaml = 'second/evo-classes.yml'         # Replace with your dataset YAML

lrs, losses = run_lr_finder(model_path, data_yaml)

# === Plot result ===
plt.figure(figsize=(8, 5))
plt.plot(lrs, losses)
plt.xscale('log')
plt.xlabel("Learning Rate (log scale)")
plt.ylabel("Loss")
plt.title("YOLOv8 Manual Learning Rate Finder")
plt.grid(True)
plt.show()

# Suggest a good LR
min_idx = int(np.argmin(losses))
best_lr = lrs[min_idx] / 10  # 10x smaller than where loss is lowest
print(f"\n✅ Suggested LR: {best_lr:.6f}")
