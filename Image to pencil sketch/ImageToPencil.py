#Import libraries
import sys
sys.path.append(r"C:\Users\selim\AppData\Local\Programs\Python\Python311\Lib\site-packages")
import cv2

#Import the image
image = cv2.imread(r"C:\Users\selim\Desktop\python\Image to pencil sketch\Parrot.jpg")

#Convert to grey
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Invert
invert = cv2.bitwise_not(grey_img)
#Blur the picture
blur = cv2.GaussianBlur(invert, (21, 21), 0)
#Invert again
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

#Export result
cv2.imwrite("Sketch.jpg", sketch)