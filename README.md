# 🎯 Object Detection with YOLOv8

A minimal yet powerful object detection project using **YOLO** (Ultralytics) and **Supervision** for annotating detected objects in images.


## 🛠️ Installation

This project uses [**uv**](https://github.com/astral-sh/uv) for fast dependency management.

### Prerequisites

- Python >= 3.12
- [uv](https://github.com/astral-sh/uv) package manager

### Setup
Try this on CPU only
```bash
# Install uv (if not already installed)
pip install uv

# Create a virtual environment and install dependencies
uv sync
```

Or with pip:

```bash
pip install ultralytics supervision
```

#### If you want to try this on GPU refer here

[Pytorch install guide for GPU](https://pytorch.org/get-started/locally/)

---

## ▶️ Usage

### Run basic detection

```bash
python object_detection.py
```

### Run with annotation (saves output to `Image.jpg`)

```bash
python Object_detection_with_anatation.py
```

---

## 📦 Dependencies

| Package | Version |
|---|---|
| `ultralytics` | `>=8.4.66` |
| `supervision` | `>=0.28.0` |
| `torch` | `>=2.12.0` |
| `torchvision` | `>=0.27.0` |

---

## 📌 Notes

- The model file `yolo26n.pt` is a custom/pre-trained YOLO nano weights file. Make sure it exists in the project root before running.
- You can swap `bus.jpg` with any image of your choice — just update the filename in the script.
- The annotated output is saved as `Image.jpg` in the project root.

---

## 📄 License

This project is for learning and experimentation purposes.
