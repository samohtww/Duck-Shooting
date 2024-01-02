# HITSCAN PROTOTYPE

import numpy as np
import cv2


img = cv2.imread('C:/Users/Matthew/Documents/GitHub/Duck_shooting_shared/Duck-Shooting/images/TEST2.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(img, 4, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)







cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# import os

# # Specifying path

# path = 'C:/Users/Matthew/Documents/GitHub/Duck_shooting_shared/Duck-Shooting/Images/Red_Ring.png'

# # Checking whether the specified path exists

# isExisting = os.path.exists(path)

# print(isExisting)

# # Specifying path

# path = 'C:/Users/Matthew/Documents/GitHub/Duck_shooting_shared/Duck-Shooting/Hitscan prototype/HITSCAN TEST IMAGES/HITSCAN TEST IMAGES/TEST2.jpg'

# # Checking whether the specified path exists

# isExisting = os.path.exists(path)

# # print(isExisting)