# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:15:56 2019

@author: Pc
"""

import cv2
import dlib
import time
import threading
import math

# Haarcascade classifier to identify vehicles
carCascade = cv2.CascadeClassifier('myhaar.xml')
video = cv2.VideoCapture('4.mp4') #video


WIDTH = 1280
HEIGHT = 720

#define points to calculate speed
def estimateSpeed(location1, location2):
    #calculating pixels between two points
	d_pixels = math.sqrt(math.pow(location2[0] - location1[0], 2) + math.pow(location2[1] - location1[1], 2))
	# ppm = location2[2] / carWidht
	ppm = 8.8 #pixels per metre
	d_meters = d_pixels / ppm #distance in metres
	#print("d_pixels=" + str(d_pixels), "d_meters=" + str(d_meters))
	fps = 18 #frames per second
	speed = d_meters * fps * 3.6
	return speed
def trackMultipleObjects():
	rectangleColor = (0, 255, 0)
	frameCounter = 0
	currentCarID = 0
	fps = 0
	
	carTracker = {}
	carNumbers = {}
	carLocation1 = {}
	carLocation2 = {}
	speed = [None] * 1000
	
	# Write output to video file
	out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (WIDTH,HEIGHT))
    


	while True:
		start_time = time.time()
		rc, image = video.read()
		if type(image) == type(None):
			break
		
		image = cv2.resize(image, (WIDTH, HEIGHT))
		resultImage = image.copy()
		
		frameCounter = frameCounter + 1
        
        if not (frameCounter % 10):
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			cars = carCascade.detectMultiScale(gray, 1.1, 13, 18, (24, 24))
            
            for (_x, _y, _w, _h) in cars:
				x = int(_x)
				y = int(_y)
				w = int(_w)
				h = int(_h)
			
				x_bar = x + 0.5 * w
				y_bar = y + 0.5 * h