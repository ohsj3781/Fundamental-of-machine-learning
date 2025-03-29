import random
import math

def model_a(x,w):
    return w[1] * x + w[0]
def model_b(x,w):
    return w[1]*math.cos(math.pi*x)+w[0]

X=[-1,0,1,1]
Y=[1,1,1,0]
w=[random.uniform(-1, 1) for _ in range(2)]
print("Problem 2a")
num_epochs = 100
learning_rate = 0.1
gradient=[0,0]

for epoch in range(num_epochs):
    gradient=[0,0]
    for i in range(len(X)):
        gradient[0] -= 2 * (Y[i]-model_a(X[i],w))
        gradient[1] -= 2 * (Y[i]-model_a(X[i],w)) * X[i]
    # print(gradient)
    w[0] = w[0] - learning_rate * gradient[0]
    w[1] = w[1] - learning_rate * gradient[1]
    # print(w)
print("After training: ", w)

print("Problem 2b")
w=[random.uniform(-1, 1) for _ in range(2)]
num_epochs = 100
learning_rate = 0.1

for epoch in range(num_epochs):
    gradient=[0,0]
    for i in range(len(X)):
        gradient[0] -= 2 * (Y[i]-model_b(X[i],w))
        gradient[1] -= 2 * (Y[i]-model_b(X[i],w)) * math.cos(math.pi*X[i])
    # print(gradient)
    w[0] = w[0] - learning_rate * gradient[0]
    w[1] = w[1] - learning_rate * gradient[1]
    # print(w)
print("After training: ", w)

