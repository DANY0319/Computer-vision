
import cv2

img = cv2.imread("C:/Users/bolla/Downloads/tree_image.jpg")

roi = img[50:200, 50:200]

result = img.copy()

result[250:400, 250:400] = roi

cv2.imshow("Original Image", img)

cv2.imshow("ROI Image", roi)

cv2.imshow("Modified Image", result)

cv2.imwrite("roi.jpg", result)

cv2.waitKey(0)

cv2.destroyAllWindows()
