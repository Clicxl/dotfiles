import cv2

"""Imread Reads the image in 3 different type:
1. GreayScale - cv2.IMREAD_GRAYSCALE : 0
2. Regular Colour image - cv.IMREAD_UNCHANGED : 1
3. WIthout alpha values - cv.IMREAD.COLOR : -1"""
img = cv2.imread('Assests/img1.jpg',cv2.IMREAD_COLOR)

cv2.imshow('Showing Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
