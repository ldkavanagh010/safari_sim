__author__ = 'lkavanagh010'
import numpy as np


class NeuralNetwork():

    def __init__(self, inputs, hidden, outputs):
        # number of neurons in each layer
        self.inputs = inputs + 1
        self.hidden = hidden
        self.outputs = outputs

        # arrays of activations
        self.ai = [1.0] * self.inputs
        self.ah = [1.0] * self.hidden
        self.ao = [1.0] * self.outputs

        # weights for layers
        self.theta_in = np.random.randn(self.inputs, self.hidden)
        self.theta_out = np.random.randn(self.hidden, self.outputs)

        # Delta arrays for changes to theta, only for backpropgation
        # self.delta_in = np.zeros((self.inputs, self.hidden))
        # self.delta_out = np.zeros((self.hidden, self.outputs))

    def feedForward(self, inputs):
        if len(inputs) != self.inputs-1:
            raise ValueError('Wrong number of inputs you silly goose!')
        # input activations
        for i in range(self.inputs -1): # -1 is to avoid the bias
            self.ai[i] = inputs[i]
        # hidden activations
        for j in range(self.hidden):
            sum = 0.0
            for i in range(self.inputs):
                sum += self.ai[i] * self.theta_in[i][j]
            self.ah[j] = self.sigmoid(sum)
        # output activations
        for k in range(self.outputs):
            sum = 0.0
            for j in range(self.hidden):
                sum += self.ah[j] * self.theta_out[j][k]
            self.ao[k] = self.sigmoid(sum)
        return self.ao[:]

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))