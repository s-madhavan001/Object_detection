from ultralytics import YOLO

model = YOLO("yolo26n.pt")

results = model("bus.jpg")
