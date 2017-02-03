import glob
import cv2
import pandas as pd
import os

# image = cv2.imread('/home/neeraj/learn/ABInBev/Focus Area - Image Processing/Shelf Image Dataset/Supermarket_2015-01-04.jpg')

debug = False

df = pd.read_csv('/home/neeraj/learn/ABInBev/extra_data/ROI.csv').dropna()
roi_info = df.values

img_list = glob.glob('/home/neeraj/learn/ABInBev/Focus Area - Image Processing/Shelf Image Dataset/*.jpg')

for img_no, img_path in enumerate(img_list):

	image = cv2.imread(img_path)
	img_suffix = img_path.split('/')[-1].split('.')[0].split('_')[-1]
	if debug:	
		cv2.imshow('fig',cv2.resize(image,(640,480)))
		key = cv2.waitKey(0)
		if key == 27:
			exit()
	for roi in roi_info:

		directory = 'data/'+str(roi[1])+'_'+str(roi[2])
		beer = directory+'/beer'
		label = directory+'/label'
		if not os.path.exists(directory):
		    os.makedirs(directory)
		    os.makedirs(beer)
		    os.makedirs(label)
		
		beer_img = image[roi[4]:roi[6],roi[3]:roi[5]]
		cv2.imwrite(beer+'/Picture_'+img_suffix+'.jpg',beer_img)
		if debug:	
			cv2.imshow('fig',beer_img)
			key = cv2.waitKey(0)
			if key == 27:
				pass

		label_img = image[roi[8]:roi[10],roi[7]:roi[9]]
		cv2.imwrite(label+'/Picture_'+img_suffix+'.jpg',label_img)
		if debug:	
			cv2.imshow('fig',label_img)
			key = cv2.waitKey(0)
			if key == 27:
				pass
	print "Done with %s image "%(img_no)