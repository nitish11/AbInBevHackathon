__author__ = "Abhijay, Neeraj and Nitish"
__credits__ = ["Abhijay, Neeraj and Nitish"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Nitish (Git: @nitish11)"
__status__ = "Development"


import cv2
import numpy as np
from matplotlib import pyplot as plt


def get_template_matching(test_image, template_image):
    img_rgb = cv2.imread(test_image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_image,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    cv2.imwrite('result.png',img_rgb)
    return loc
