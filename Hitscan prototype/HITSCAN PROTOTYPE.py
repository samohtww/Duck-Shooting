# HITSCAN PROTOTYPE
from os.path import exists

import cv2

img = cv2.imread('C:/Users/Matthew/Documents/GitHub/Duck_shooting_shared/Duck-Shooting/Images/TEST2.jpg', 0)
img = cv2.resize(img, (1920,1080))
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# import os

# # Specifying path

# path = 'C:/Users/Matthew/Documents/GitHub/Duck_shooting_shared/Duck-Shooting/Images/TEST1.jpg'

# # Checking whether the specified path exists

# isExisting = os.path.exists(path)

# print(isExisting)

# # Specifying path

# path = 'C:/Users/Matthew/Documents/GitHub/Duck_shooting_shared/Duck-Shooting/Hitscan prototype/HITSCAN TEST IMAGES/HITSCAN TEST IMAGES/TEST2'

# # Checking whether the specified path exists

# isExisting = os.path.exists(path)

# print(isExisting)