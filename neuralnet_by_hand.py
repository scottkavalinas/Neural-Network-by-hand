
import numpy as np
import math

#forward pass
x_0 = 10.00
y_0 = 200.00

target_1 = 1
target_2 = 2

input_layer =  np.array([x_0,y_0])
weight_input = np.array([[0.16,0.16,0.16],[0.16,0.16,0.16]])
bias_input = np.array([0.0,0.0,0.0])

hidden_layer = np.matmul(input_layer,weight_input)
hidden_activated = np.array([1/(1+math.exp(-(hidden_layer[0]))),1/(1+math.exp(-(hidden_layer[1]))),
                             1/(1+math.exp(-(hidden_layer[2])))])

weight_hidden = np.array([[0.1,0.1],[0.1,0.1],[0.1,0.1]])
bias_hidden = np.array([0.0,0.0,0.0])

output_layer = np.matmul(hidden_layer,weight_hidden)
output_activated = np.array([1/(1+math.exp(-(output_layer[0]))),1/(1+math.exp(-(output_layer[1])))])

x_1 = output_activated[0]
y_1 = output_activated[1]

#error calculation

error_term_1 = (target_1-x_1)**2
error_term_2 = (target_2-y_1)**2 

total_error = 0.5*(error_term_1+error_term_2)

#backpropagation
