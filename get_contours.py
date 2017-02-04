__author__ = "Abhijay, Neeraj and Nitish"
__credits__ = ["Abhijay, Neeraj and Nitish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Nitish (Git: @nitish11)"
__status__ = "Development"


import cv2

#variables
tresh_min = 128
tresh_max = 255
file_name = 'test.jpg'

#Reading images
image = cv2.imread(file_name)
im_bw = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#Setting the threshold
(thresh, im_bw) = cv2.threshold(im_bw, tresh_min, tresh_max, 0)
cv2.imwrite('bw_'+file_name, im_bw)


#Extracting and storing the contours
im2, contours, hierarchy  = cv2.findContours(im_bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0,255,0), 3)
cv2.imwrite('cnt_'+file_name, image)
