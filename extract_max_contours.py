__author__ = "Abhijay, Neeraj and Nitish"
__credits__ = ["Abhijay, Neeraj and Nitish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Nitish (Git: @nitish11)"
__status__ = "Development"


import cv2


def extract_price_tag(extracted_image):
    #Variables
    max_contour_area = -1
    contour_with_max_area = []

    min_area_threshold = 8000
    max_area_threshold = 23000
    extracted_price_tag = None

    #Extraction of contours
    # extracted_image = cv2.imread(file_name)
    extracted_image_grey = cv2.cvtColor(extracted_image, cv2.COLOR_BGR2GRAY)

    #Setting the threshold
    (thresh, extracted_image_grey) = cv2.threshold(extracted_image_grey, 190, 255, 0)

    #Extraction of contours
    im2, contours, hierarchy = cv2.findContours(extracted_image_grey, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(extracted_image, contours, -1, (0,255,0), 3)
    # cv2.imwrite('cnt_'+file_name, extracted_image)


    #Finding the max contour
    for c in range(len(contours)):
        contour_area = cv2.contourArea(contours[c])
        if min_area_threshold < contour_area < max_area_threshold:
            max_contour_area = contour_area
            contour_with_max_area = contours[c]
        
    #Extraction of price tag
    if len(contour_with_max_area) > 0:
        x, y, width, height = cv2.boundingRect(contour_with_max_area)
        extracted_price_tag = extracted_image[y : y + height, x : x + width]

    return extracted_price_tag


