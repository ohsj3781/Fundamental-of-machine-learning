import random
import math

def f(x,w):
    return w[2]*x+math.cos(w[1])*x+w[0]

x=[-1,0,1,1]
y=[1,1,1,0]

w=[random.uniform(-1, 1) for _ in range(3)]
num_epochs = 100000
learning_rate = 0.01


for epoch in range(num_epochs):
    gradient=[0,0,0]
    for i in range(len(x)):
        e=y[i]-f(x[i],w)
        gradient[0] += -2 * e
        gradient[1] += 2 * e * x[i] * math.sin(w[1])
        gradient[2] += -2 * e * x[i]
    w[0] = w[0] - learning_rate * gradient[0]
    w[1] = w[1] - learning_rate * gradient[1]
    w[2] = w[2] - learning_rate * gradient[2]
print("After training: ", w)
print("Error: ",e**2)  
