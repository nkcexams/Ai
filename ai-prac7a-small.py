'''
import numpy as np

def unit_step(v):
    return 1 if v >= 0 else 0

def perceptron_model(x, w, b):
    return unit_step(np.dot(w, x) + b)

def or_logic(x):
    return perceptron_model(x, np.array([1, 1]), -0.5)

def and_logic(x):
    return perceptron_model(x, np.array([1, 1]), -1.5)

test_cases = [np.array([0,0]), np.array([0,1]), np.array([1,0]), np.array([1,1])]
for x in test_cases:
    print(f"OR({x[0]},{x[1]})={or_logic(x)}")
    print(f"AND({x[0]},{x[1]})={and_logic(x)}")


'''
import numpy as np
percep = lambda x, w, b: 1 if np.dot(w,x) + b >= 0 else 0

for x in [[0,0], [0,1], [1,0], [1,1]]:
    print(f"OR{x}={percep(x, [1, 1], -0.5)} AND{x}={percep(x, [1, 1], -1.5)}")
    



