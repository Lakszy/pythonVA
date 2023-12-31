import cv2
import numpy as np
import matplotlib.pyplot as plt
 
image =  cv2.imread("c:\\Users\\laksh\\OneDrive\\Desktop\\NEWNEW\\start\\projects\\image\\avatar.jpeg") 
width = 1800
height = 200

# Resize the image using the new dimensions
res = cv2.resize(image, (width, height))

# Save the resized image to a file
cv2.imwrite('res.png', res)

# Display the resized image (optional)
cv2.imshow('Resized Image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
