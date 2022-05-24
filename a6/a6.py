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

# step 1
averaged = np.zeros((10, 28, 28))

for i in range(10):
    ii = np.where(labels == i)[0]
    count = ii.size
    for j in ii:
        averaged[i] = np.add(averaged[i], images[j])
    averaged[i] = averaged[i] / count

show_templates(averaged)

#step 2

img = pg.image.load('secret.png')
secret_rgb = pg.surfarray.array3d(img)
greyscale = np.mean(secret_rgb, axis=2).transpose()
greyscale_split = np.array(np.hsplit(greyscale, list(range(28, greyscale.shape[1], 28))))

best_guesses = []

for i in range(greyscale_split.shape[0]):
    min = -1
    best_guess = -1
    for j in range(10):
        euclidian_dist = np.sqrt(sum(np.square(greyscale_split[i].flatten() - averaged[j].flatten())))
        if min == -1 or euclidian_dist < min:
            min = euclidian_dist
            best_guess = j
    best_guesses.append(best_guess)

# step 4
txt = ""
for i in best_guesses:
    txt += chr(i + ord('A'))
print(best_guesses)
print(txt)