import numpy as np
import argparse 
import imutils
import dlib
import cv2
from imutils import face_utils
from violaJones import ViolaJonesSD



def neutralFace(image, models):

	#initialize dlib face detector as well as predictor
	detector = dlib.get_frontal_face_detector()
	#the predictor needs the training data
	predictor = dlib.shape_predictor(models)

	# load the input image, resize it, and convert it to grayscale
	image = cv2.imread(image)
	image = imutils.resize(image, width=900)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
	# detect faces in the grayscale image
	rects = detector(gray, 1)

	#from the face detected, now iterate through the face and find the features
	for (i,rect) in enumerate(rects):
		shape = predictor(gray, rect)		     #gets all 68 (x,y) coordinates corresponding to the features
		shape = face_utils.shape_to_np(shape)    #turns the 68 coordinates into a numpy array

		#now convert the dlib rectangle to the (x,y,width, height) rectangles we like in python
		(x,y,width,height) = face_utils.rect_to_bb(rect)
		#cv2.rectangle(image, (x,y), (x+width, y+height), (0,255,0),2)

		# loop over the (x, y)-coordinates for the facial landmarks
		# and draw them on the image

		for (x, y) in shape:
			cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
		(xmouth,ymouth) = shape[66]

		# #blur the image
		blurredImage = cv2.GaussianBlur(gray,(3,3),0.5)
		# mouthOpenSection = gray[ymouth-10:ymouth+10,xmouth-10:xmouth+10]
		# height,width = mouthOpenSection.shape
		# print height/2-2
		# laplacian = cv2.Laplacian(mouthOpenSection,cv2.CV_64F)
		# sobely = cv2.Sobel(mouthOpenSection,cv2.CV_64F,0,1,ksize=5)
		# print laplacian[height/2+1-3:height/2+1+3,11]
		# print laplacian[11,11]
		# print sobely[height/2+1-3:height/2+1+3,11]
		# print sobely[11,11]
		# if(abs(laplacian[11,11])+abs(laplacian[10,11])>=13 or shape[67,1]-shape[63,1]>3 ):
		# 	(secx,secy) = shape[62]
		# 	cv2.circle(image,(xmouth,ymouth),1,(255,0,0),-1)
		# 	cv2.circle(image,(secx,secy),1,(255,0,0),-1)

		# #check if mouth is open
		# if(not isMouthOpen(shape,blurredImage)):
		# 	print 'Mouth open'
		# 	#return 'Mouth is open!!!!!'

		# (secx,secy) = shape[62]
		# cv2.circle(image,(xmouth,ymouth),1,(255,0,0),-1)
		# cv2.circle(image,(secx,secy),1,(255,0,0),-1)

		(xwtv,ylow) = shape[50]
		(xlow,ywtv) = shape[48]
		(xwtv2,yhigh) = shape[57]
		(xhigh,ywtv2) = shape[54]

		#blur the image
		#blurredImage = cv2.GaussianBlur(gray,3,0.5)
		roi_gray = gray[ylow-10:yhigh+10,xlow-10:xhigh+10]
		cv2.imshow("hello",roi_gray)

		# if(ViolaJonesSD(gray)):
		# 	print 'Smile'
		# 	#return 'Do not be happy'
		# else:
		# 	print 'thanks for not smiling'

		# isWeirdEyebrow(shape,gray)
		



 
	# show the output image with the face detections + facial landmarks
	cv2.imshow("Output", image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

# def isMouthOpen(featurePoints,image):
# 	(xmouth,ymouth) = featurePoints[66]

# 	#blur the image
# 	#blurredImage = cv2.GaussianBlur(gray,3,0.5)
# 	mouthOpenSection = image[ymouth-25:ymouth+25,xmouth-25:xmouth+25]
# 	height,width = mouthOpenSection.shape
# 	laplacian = cv2.Laplacian(mouthOpenSection,cv2.CV_64F)
# 	# sobely = cv2.Sobel(mouthOpenSection,cv2.CV_64F,0,1,ksize=5)
# 	# print laplacian[height/2+1-3:height/2+1+3,11]
# 	# print laplacian[11,11]
# 	# print sobely[height/2+1-3:height/2+1+3,11]
# 	# print sobely[11,11]
# 	#print abs(laplacian[11,11]-laplacian[10,11])
# 	if(abs(laplacian[11,11]-laplacian[10,11])>=13 or featurePoints[66,1]-featurePoints[62,1]>7 ):
# 		# (secx,secy) = featurePoints[62]
# 		# cv2.circle(image,(xmouth,ymouth),1,(255,0,0),-1)
# 		# cv2.circle(image,(secx,secy),1,(255,0,0),-1)
# 		#print abs(laplacian[11,11]-laplacian[10,11])
# 		# print featurePoints[66,1]-featurePoints[62,1]
# 		return False
# 	else:
# 		return True

# def isWeirdEyebrow(featurePoints,image):
# 	height,width = image.shape

# 	(x1,y1) = featurePoints[21]
# 	(x2,y2) = featurePoints[20]
# 	(x3,y3) = featurePoints[19]

# 	(x4,y4) = featurePoints[22]
# 	(x5,y5) = featurePoints[23]
# 	(x6,y6) = featurePoints[24]

# 	#Get the eye position
# 	(ex1,ey1) = featurePoints[37]
# 	(ex2,ey2) = featurePoints[38]

# 	(ex3,ey3) = featurePoints[43]
# 	(ex4,ey4) = featurePoints[44]


# 	rightbrowPoint = max(y1,y2,y3)
# 	print rightbrowPoint
# 	leftbrowPoint = max(y4,y5,y6)

# 	leftEyePoint = min(ey3,ey4)
# 	rightEyePoint = min(ey1,ey1)
# 	print rightEyePoint

# 	a = (rightEyePoint-rightbrowPoint)/float(height)
# 	print 'diff'
# 	print a
# 	(nosex,nosey) = featurePoints[27]
# 	b = (nosey - rightbrowPoint)/float(height)
# 	print b

# 	threshold = 25

# 	if((rightEyePoint-rightbrowPoint)/height <threshold or (leftEyePoint-rightbrowPoint)<threshold):
# 		return False
# 	else:
# 		return True



neutralFace('./testImages/frown.jpg','./shape_predictor_68_face_landmarks.dat')