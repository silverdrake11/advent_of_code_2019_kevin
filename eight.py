import numpy as np
import pdb


with open('input.txt') as fh:
    text = fh.read().strip()

nums = list(map(int, text))
length = len(nums)

m,n = (6, 25)
#m,n = (2,2) # DEBUG
num_layers = int(length / (m * n))

matrices = np.asarray(nums).reshape(num_layers, m, n)

min_zero_layer = np.sum(matrices.reshape(num_layers, m*n)==0, axis=1).argmin()
min_matrix = matrices[min_zero_layer]
answer = np.sum(min_matrix==1) * np.sum(min_matrix==2)
print('Part1', answer)

image = np.zeros((m,n), dtype=int) + 2 # Initialize to transparent layer
for i in reversed(range(num_layers)):
    cur = matrices[i]

    # Zeros where black and white pixels are
    mask = 1 * cur
    mask[mask == 1] = 0
    mask[mask == 2] = 1

    # Zero out black and white pixels in image, then add nontransparent pixels
    image = (image * mask) + (cur * (1-mask))

# For pretty printing
import matplotlib.pyplot as plt
imgplot = plt.imshow(image)
plt.show()
