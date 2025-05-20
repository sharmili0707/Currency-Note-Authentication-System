import cv2
import numpy as np
currency_img = cv2.imread('curren.jpg', cv2.IMREAD_GRAYSCALE)
genuine_img = cv2.imread('currency.jpg', cv2.IMREAD_GRAYSCALE)
orb = cv2.ORB_create()
keypoints_currency, descriptors_currency = orb.detectAndCompute(currency_img, None)
keypoints_genuine, descriptors_genuine = orb.detectAndCompute(genuine_img, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(descriptors_currency, descriptors_genuine)
matches = sorted(matches, key=lambda x: x.distance)
matched_image = cv2.drawMatches(currency_img, keypoints_currency, genuine_img, keypoints_genuine, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imshow("Matched Features", matched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
match_threshold = 30  
if len(matches) > match_threshold:
    print(" Currency note is likely genuine.")
else:
    print(" Potentially counterfeit currency detected.")