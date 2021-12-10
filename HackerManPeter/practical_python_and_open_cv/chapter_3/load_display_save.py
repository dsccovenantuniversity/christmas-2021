import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required=True, help="Path to the image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

print(f'width: {image.shape[1]} pixels')
print(f'height: {image.shape[0]} pixels')
print(f'channels: {image.shape[2]} pixels')

cv2.imshow("image", image)
cv2.waitKey(0)

cv2.imwrite("newimage.jpg", image)