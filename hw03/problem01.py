import random

w= [random.uniform(-1, 1) for _ in range(2)]
num_epochs = 100
learning_rate = 0.1
temp_w=w.copy()
for epoch in range(num_epochs):
    temp_w[0]=w[0]-learning_rate*(4*w[1]+6*w[0]-6)
    temp_w[1]=w[1]-learning_rate*(4*w[1]+4*w[0]-6)
    w=temp_w.copy()
    # print(w)
w=temp_w
print(w)