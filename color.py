#!/usr/bin/env python3
import cv2
import numpy as np

lower = np.array([15,150,20])
upper = np.array([15,150,20])

video = cv2.VideoCapture(0)

while True:
    succes=2
