
import numpy as np

# genetic algo

def sigmoid(num):
    return 1 / (1 + np.exp(-num))

# input
def import_input(snk_tail, fd):
    return np.array([[snk_tail[0][0]],
                     [snk_tail[0][1]],
                     [fd[0]],
                     [fd[1]]])

# synapses
syn0 = 2 * np.random.random((4, 4)) - 1
syn1 = 2 * np.random.random((1, 2)) - 1

print np.random.random((4, 1)).dot(np.random.random((1, 10)))
