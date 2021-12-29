import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", '--image', required=True, help="Path to image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(blue, green, red) = image[0,0]
print(f'Pixel at (0, 0) - Red: {red},\n Green: {green},\n Blue: {blue}')

image[0, 0] = (0, 0, 225)
(blue, green, red) = image[0, 0]
print(f'Pixel at (0, 0) - Red: {red},\n Green: {green},\n Blue: {blue}')

corner = image[0:100, 0:100]

cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)