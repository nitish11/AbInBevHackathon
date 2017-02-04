__author__ = "Abhijay, Neeraj and Nitish"
__credits__ = ["Abhijay, Neeraj and Nitish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Neeraj"
__status__ = "Development"


import glob
import cv2
import pandas as pd
import os
from extract_max_contours import extract_price_tag


# image = cv2.imread('/home/neeraj/learn/ABInBev/Focus Area - Image Processing/Shelf Image Dataset/Supermarket_2015-01-04.jpg')

debug = False

df = pd.read_csv('ROI.csv').dropna()
roi_info = df.values

img_list = glob.glob('../Focus Area - Image Processing/Shelf Image Dataset/*.jpg')

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
        pricetag = directory+'/pricetag'
        if not os.path.exists(directory):
            os.makedirs(directory)
            os.makedirs(beer)
            os.makedirs(label)
            os.makedirs(pricetag)
        
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

        extracted_price_tag = extract_price_tag(label_img)
        if extracted_price_tag is not None:
            cv2.imwrite(pricetag+'/Picture_'+img_suffix+'.jpg',extracted_price_tag)
        else:
            print label+'/Picture_'+img_suffix+'.jpg'

    print "Done with %s image "%(img_no)