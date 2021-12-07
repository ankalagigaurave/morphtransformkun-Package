# -*- coding: utf-8 -*-


import cv2 
import numpy as np

def erosion(img,kernel_size,iteration):
  img = img
  kernel = np.ones((kernel_size,kernel_size),np.uint8)
  erosion = cv2.erode(img,kernel,iterations = iteration)
  return erosion

def dilation(img,kernel_size,iteration):
  img = img
  kernel = np.ones((kernel_size,kernel_size),np.uint8)
  dilation = cv2.dilate(img,kernel,iterations = 1)
  return dilation

def opening(img,kernel_size,iteration):
  img = img
  kernel = np.ones((kernel_size,kernel_size),np.uint8)
  opening = cv2.morphologyEx(img, cv.MORPH_OPEN, kernel)
  return opening

def closing(img,kernel_size,iteration):
  img = img
  kernel = np.ones((kernel_size,kernel_size),np.uint8)
  closing = cv2.morphologyEx(img, cv.MORPH_CLOSE, kernel)
  return closing

