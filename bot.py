
import numpy as np

# genetic algo

def sigmoid(num, deriv=False):
    if deriv == True:
        return x * (1 - x)
    return 1 / (1 + np.exp(-num))

# input
def import_input(snk_tail, fd):
    return np.array([[snk_tail[0][0], snk_tail[0][1], fd[0], fd[1]]])

def return_network(snk, fd):
    return {"layers": import_input(snk.tail, fd), \
    "synapses": [2 * np.random.random((4, 10)) - 1, \
    2 * np.random.random((10, 2)) - 1]}

def loss(guess, output):
    return output - guess

def predict(network, layer_index):
    return sigmoid(np.dot(network["layers"][layer_index], \
    network["synapses"][layer_index]))
