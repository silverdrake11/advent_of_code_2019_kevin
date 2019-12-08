import pdb
import matplotlib
with open('input.txt') as fh:
    text = fh.read().strip()

print(text)

import numpy as np
nums = list(map(int, text))
length = len(nums)

m,n = (6, 25)
#m,n = (2,2)
l = length / int(m * n)
l = int(l)

hello = np.asarray(nums).reshape(l, n, m)



nonzeros = []
for i in range(l):
    nz = np.count_nonzero(hello[i])
    print(i, nz, hello[i].shape)
    nonzeros.append(nz)
print(max(nonzeros))

'''print(hello[5])

#print(hello[100])
#print(hello[100].flatten())
unique, counts = np.unique(hello[5].flatten(), return_counts=True)
numbers = hello[5].flatten().tolist()
print(numbers.count(1))
print(numbers.count(2))
print(hello)
print(dict(zip(unique, counts)))'''

#hello[hello == 2] = 0
#hello[hello == 1] = 0
#hello.sum(axis=0)
#print(hello)
#pdb.set_trace()
#print(hello)
new_list = np.zeros((m,n), dtype=int) + 2
prev = new_list.flatten().tolist()
#print(prev)
#new_list = [0 * len(prev)]
for i in reversed(range(l)):
    cur = hello[i].flatten().tolist()
    for idx, (c,p) in enumerate(zip(cur, prev)):
        if c == 1 or c == 0:
            prev[idx] = c
        else:
            prev[idx] = p
    #pdb.set_trace()
print(prev)
new = np.asarray(prev).reshape((m,n))
print(new)
    #print(i)
    #print(hello[i])
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
imgplot = plt.imshow(new)
plt.show()
