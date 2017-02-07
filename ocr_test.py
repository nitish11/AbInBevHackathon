"""OCR in Python using the Tesseract engine from Google
http://code.google.com/p/pytesser/
by Michael J.T. O'Kelly
V 0.0.1, 3/10/07"""

import Image
import subprocess
import glob
import cv2
import pandas as pd 
import re
import cv2
from base64 import b64encode  
from os import makedirs  
from os.path import join, basename  
from sys import argv  
import json  
import requests
from matplotlib import pyplot as plt
import pickle

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'  
RESULTS_DIR = 'jsons'

#API_KEY = 'AIzaSyD-S4VpFHwMQcvweVrx03g6YywP5iYtGLA'

API_KEY = 'AIzaSyCzemskXK5JabNNLy6fnwMD-hQfws0jFE4'

API_KEY = 'AIzaSyC2Z6fymVj-StfrX7AeTJKp3l7Mo0ELc7I'



def make_image_data_list(image_filenames):  
    """
    image_filenames is a list of filename strings
    Returns a list of dicts formatted as the Vision API
        needs them to be
    """
    img_requests = []
    for imgname in image_filenames:
        with open(imgname, 'rb') as f:
            ctxt = b64encode(f.read()).decode()
            img_requests.append({
                    'image': {'content': ctxt},
                    'features': [{
                        'type': 'TEXT_DETECTION',
                        'maxResults': 1
                    }]
            })
    return img_requests

def make_image_data(image_filenames):  
    """Returns the image data lists as bytes"""
    imgdict = make_image_data_list(image_filenames)
    return json.dumps({"requests": imgdict }).encode()


def request_ocr(api_key, image_filenames):  
    response = requests.post(ENDPOINT_URL,
                            data=make_image_data(image_filenames),
                            params={'key': api_key},
                            headers={'Content-Type': 'application/json'})
    return response

if __name__=='__main__':
    debug = False
    dir_names = glob.glob(data)
    
    data_folder_name = 'data_nitish'
    data =  data_folder_name+'/*'
    ocr_folder_name = 'pricetag' 
    price_tag_data = []
    annotations = []
    dir_name = [dir_names[19]]
    count = 0
    for beer_name in dir_name:
        img_path_list = glob.glob(beer_name+'/'+ocr_folder_name+'/*.jpg')
        for img_path in img_path_list:
            count += 1
            print count
            print img_path
            date_of_the_day =  img_path.split('/')[-1].split('_')[1].split('.')[0]
            brand_name = img_path.split(data_folder_name+'/')[1].split('/')[0].split('_')[0]
            brand_type = img_path.split(data_folder_name+'/')[1].split('/')[0].split('_')[1]
            
            response = request_ocr(API_KEY, [img_path])
            
            if response.status_code != 200 or response.json().get('error'):
                print(response.text)
            else:
                resp = response.json()['responses'][0]
                
                t = resp['textAnnotations'][0]
            
                description = t['description']
                                
                price_tag_data.append([date_of_the_day,brand_name,brand_type,description])                
                
                annotations.append([img_path,resp[u'textAnnotations']])
#                img = cv2.imread(img_path)
#                for t in resp[u'textAnnotations']:
#                    cv2.imwrite("",cv2.rectangle(img, ( t['boundingPoly']['vertices'][0]['x'], t['boundingPoly']['vertices'][0]['y']), ( t['boundingPoly']['vertices'][2]['x'], t['boundingPoly']['vertices'][2]['y']), (0,255,0),1))
                    
            if debug:
                cv2.imshow('fig',cv2.imread(img_path))
                key = cv2.waitKey(0)
                if key == 27:
                    exit()
    
    df = pd.DataFrame(price_tag_data)
    df.columns = ['Date','Brand', 'SKU', 'OCR_data']
    
    with open(beer_name+'/df_'+brand_name+'.pickle', 'wb') as handle:
        pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)    
    
    with open(beer_name+'/annotations_'+brand_name+'.pickle', 'wb') as handle:
        pickle.dump(annotations, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
    df.to_csv(beer_name+'/price_tag_'+brand_name+'.csv')
    
    
    
    
#    with open(beer_name+'/df_'+brand_name+'.pickle', 'wb') as handle:
#        pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
#with open(beer_name+'/df_'+brand_name+'.pickle', 'rb') as handle:
#     b = pickle.load(handle)
    
    
    
    
#import csv
#import os
#
#def WriteListToCSV(csv_file,csv_columns,data_list):
#    try:
#        with open(csv_file, 'w') as csvfile:
#            writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
#            writer.writerow(csv_columns)
#            for data in data_list:
#                writer.writerow(data)
#    except IOError as (errno, strerror):
#            print("I/O error({0}): {1}".format(errno, strerror))    
#    return              
#
#
#WriteListToCSV('abc.csv',['Date','Brand', 'SKU', 'OCR_data'],price_tag_data)