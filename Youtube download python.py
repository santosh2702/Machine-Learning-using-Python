##import cv2
##import numpy as np
##cap=cv2.VideoCapture('Alan.mp4')
##
##
##
##while(1):
##    _,frame=cap.read()
##    cv2.imshow('frame',frame)

##   TO DOWNLOAD A VIDEO FROM YOUTUBE USING PYTHON
##
import pytube
link="https://www.youtube.com/watch?time_continue=4&v=ChA_zph7aao"
yt=pytube.YouTube(link)
stream=yt.streams.first()
stream.download()
