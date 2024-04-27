import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

# strategy 0: mantieni i pixel in comune tra le due immagini, e gli altri li fai oppure no al 50%

fig = plt.figure()


def generate_new_letter_with_strategy_0(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
    new_image1 = image1.copy()
    new_image1[image1 >= 128] = 255
    new_image1[image2 < 128] = 0 

    new_image2 = image2.copy()
    new_image2[image2 >= 128] = 255
    new_image2[image2 < 128] = 0

    return new_image1, new_image2 
    



image1 = img.imread("E:/Local Code Workspace/pyhton/calligraphy-generator-/MNIST dataset for test/2.jpg")
image2 = img.imread("E:/Local Code Workspace/pyhton/calligraphy-generator-/MNIST dataset for test/1.jpg")

i1, i2 = generate_new_letter_with_strategy_0(image1, image2)
fig.add_subplot(2,2,1)
plt.imshow(image1)
fig.add_subplot(2,2,2)
plt.imshow(image2)
fig.add_subplot(2,2,3)
plt.imshow(i1)
fig.add_subplot(2,2,4)
plt.imshow(i2)
plt.show()
