# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:18:18 2019

@author: Abhishek
"""

import tensorflow as tf
import tensornets as nets
import cv2
import numpy as np
import time

nputs = tf.placeholder(tf.float32, [None, 416, 416, 3])
model = nets.YOLOv3COCO(inputs, nets.Darknet19)


classes={'0':'person','1':'bicycle','2':'car','3':'bike','5':'bus','7':'truck'}
list_of_classes=[0,1,2,3,5,7]
with tf.Session() as sess:
    sess.run(model.pretrained())

    cap = cv2.VideoCapture("C://Users//Abhishek//Desktop//VehicleTracking//cars.mp4")
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        img=cv2.resize(frame,(416,416))
        imge=np.array(img).reshape(-1,416,416,3)
        start_time=time.time()
        preds = sess.run(model.preds, {inputs: model.preprocess(imge)})
    
        print("--- %s seconds ---" % (time.time() - start_time)) 
        boxes = model.get_boxes(preds, imge.shape[1:3])
        cv2.namedWindow('image',cv2.WINDOW_NORMAL)

        cv2.resizeWindow('image', 700,700)