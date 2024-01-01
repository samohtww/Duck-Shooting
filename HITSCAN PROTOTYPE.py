# HITSCAN PROTOTYPE


import cv2

img = cv2.imread('C:/Users/Matthew/Documents/GitHub/Duck_shooting_shared/Duck-Shooting/Hitscan prototype/HITSCAN TEST IMAGES/HITSCAN TEST IMAGES/TEST2.jpg', 0)

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