import numpy as np

img = np.array([2,4,5,6,7,8,8])
img[img == 8] = 0

print(type(img))