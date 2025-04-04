import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import os

class OneLayerNet(nn.Module):
    def __init__(self, input_size, output_size):
        super(OneLayerNet, self).__init__()
        self.fc = nn.Linear(input_size, output_size,bias=True)
        self.fc.activation=nn.Sigmoid()

    def forward(self, x):
        return self.fc.activation(self.fc(x))
    

os.chdir(os.path.dirname(__file__))    
# Hyperparameters
input_size=2
output_size=1
num_epochs=100000
learning_rate=0.01

# Get data from data.txt
data=np.loadtxt('Howework 4.data.txt', delimiter=',')
x=data[:, :2]
y=data[:, 2]
x=torch.tensor(x, dtype=torch.float32)
y=torch.tensor(y, dtype=torch.float32).unsqueeze(1)

# Create model
model = OneLayerNet(input_size, output_size)
criterion=nn.BCELoss()
optimizer=optim.SGD(model.parameters(), lr=0.01)

for epoch in range(num_epochs):
    optimizer.zero_grad()
    outputs=model(x)
    loss=criterion(outputs, y)
    loss.backward()
    optimizer.step()
print("Gradient of w0 :",model.fc.bias.grad[0].item())
print("Gradient of w1 :",model.fc.weight.grad[0][0].item())
print("Gradient of w2 :",model.fc.weight.grad[0][1].item())

print("output :",outputs[0].item())
x=torch.tensor([33,81], dtype=torch.float32)
outputs=model(x)

print(outputs.item())

