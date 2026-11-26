
import cv2

img = cv2.imread("C:/Users/bolla/Downloads/tree_image.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Original Image", img)

cv2.imshow("Edge Image", edges)

cv2.imwrite("edges.jpg", edges)

cv2.waitKey(0)

cv2.destroyAllWindows()
