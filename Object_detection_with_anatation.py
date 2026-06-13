import cv2
import supervision as sv
from ultralytics import YOLO

model = YOLO("yolo26n.pt")

image = cv2.imread("bus.jpg")
results = model(image)[0]


detections = sv.Detections.from_ultralytics(results)

box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

annotated_image = box_annotator.annotate(
    scene=image, detections=detections)
annotated_image = label_annotator.annotate(
    scene=annotated_image, detections=detections)

cv2.imwrite("Image.jpg", annotated_image)

