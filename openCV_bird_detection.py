import cv2 as cv
import numpy as np
import tensorflow as tf
'''below is the code for fixing error type:
2022-08-21 18:38:46.709593: I tensorflow/core/platform/cpu_feature_guard.cc:142] 
This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following C_feature_guard.cc:142] 
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.'''
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = tf.saved_model.load("./ssd_mobilenet_v2_320x320_coco17_tpu-8/saved_model")
capture = cv.VideoCapture("bird.MP4") #another test with MP4 file "Eng_GK_training.MP4", which contains multiple people
# test result: able to detect multiplie people

while True:
    ret, frame = capture.read()
    
    if capture.get(cv.CAP_PROP_POS_FRAMES) == capture.get(cv.CAP_PROP_FRAME_COUNT):
        break
    
    input_img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    input_tensor = tf.convert_to_tensor(input_img)
    input_tensor = input_tensor[tf.newaxis, ...]
    
    output_dict = model.signatures["serving_default"](input_tensor)
    
    classes = output_dict["detection_classes"][0]
    scores = output_dict["detection_scores"][0]
    boxes = output_dict["detection_boxes"][0]
    
    height, width, _ = frame.shape
    
    for idx, score in enumerate(scores):   
        if score > 0.7:
            class_id = int(classes[idx])
            box = boxes[idx]
            x1 = int(box[1] * width)
            y1 = int(box[0] * height)
            x2 = int(box[3] * width)
            y2 = int(box[2] * height)
            
            cv.rectangle(frame, (x1, y1), (x2, y2), 255, 1)
            cv.putText(frame, str(class_id) + ":" + str(float(score)), (x1, y1 - 5),
                       cv.FONT_HERSHEY_COMPLEX, 1.5, (0, 255, 255), 1)
    
    #print "frame_check" in order to check whether the code functions without any problem
    print("frame_check")
    cv.imshow("object_detection", frame)
    if cv.waitKey(33) == ord("q"):
        break
    