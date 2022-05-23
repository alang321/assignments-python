import pickle
from matplotlib import pyplot as plt
import numpy as np
import pygame as pg


def show_templates(average_templates):
    n_templates = len(average_templates)
    fig, axs = plt.subplots(n_templates)

    for i in range(n_templates):
        axs[i].imshow(average_templates[i], cmap=plt.get_cmap('gray'))

    plt.show()


# load the database of labeled number images:
# original dataset: http://yann.lecun.com/exdb/mnist/
file = open('MNIST.dat', 'rb')
MNIST = pickle.load(file)
file.close()
images = MNIST[0]
labels = MNIST[1]
shape_image = images[0].shape
# show a single number image plus label:
plt.figure()
plt.imshow(images[0], cmap=plt.get_cmap('gray'))
plt.title(labels[0])
plt.show()

# step 1
averaged = np.zeros((9, 28, 28))

for i in range(9):
    ii = np.where(labels == i)[0]
    count = ii.size
    for j in ii:
        averaged[i] = np.add(averaged[i], images[j])
    averaged[i] = averaged[i] / count

show_templates(averaged)

#step 2

img = pg.image.load('secret.png')
secret_rgb = pg.surfarray.array3d(img)
greyscale = np.zeros(secret_rgb.shape[0:2])
# [0.216, 0.587, 0.144]
print()
greyscale = np.dot
print(pg.surfarray.array3d(img))