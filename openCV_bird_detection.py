import cv2 as cv
import numpy as np
import tensorflow as tf

model = tf.saved_model.load("ssd_mobilenet_v2_320x320_coco17_tpu-8/saved_model")
capture = cv.VideoCapture("bird.mp4")

while True:
    ret, frame = capture.read()
    
    if capture.get(cv.CAP_PROP_POS_FRAMES) == capture.get(cv.CAP_PROP_FRAME_COUNT):
        break
    
    input_img = cv.Color(frame, cv.COLOR_BGR2RGB)
    input_tensor = tf.convert_to_tensor(input_img)
    input_tensor = input_tensor[tf.newaxis, ...]
    
    output_dict = model.signatures["serving_default"](input_tensor)
    
    classes = output_dict["detection_classes"][0]
    scores = output_dict["detections_scores"][0]
    boxes = output_dict["detection_boxes"][0]
    
    height, width, _ = frame.shape
    
    for idx in enumerate(scores):
        if score > 0.7:
            class_id = int(classes[idx])
            box = boxes[idx]
            x1 = int(box[1] * width)
            y1 = int(box[0] * height)
            x2 = int(box[3] * width)
            y2 = int(box[2] * height)
            
            cv.rectangle(frame, (x1, y1), (x2, y2), 255, 1)
            cv.putText(frame, str(class_id) + ":" + str(float(score)), (x1, y1 - 5),
                       cv.FONT_HERESY_COMPLEX, 1.5, (0, 255, 255), 1)
            
    cv.imshow("object_detection", frame)
    if cv.waitKey(33) == ord("q"):
        break
    