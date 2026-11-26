
import cv2
import numpy as np

img = cv2.imread("C:/Users/bolla/Downloads/tree_image.jpg")

pts1 = np.float32([
    [50, 50],
    [300, 50],
    [300, 300],
    [50, 300]
])

pts2 = np.float32([
    [0, 0],
    [500, 0],
    [500, 400],
    [0, 400]
])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(img, matrix, (500, 400))

cv2.imshow("Original Image", img)

cv2.imshow("Transformed Image", result)

cv2.imwrite("perspective.jpg", result)

cv2.waitKey(0)

cv2.destroyAllWindows()
