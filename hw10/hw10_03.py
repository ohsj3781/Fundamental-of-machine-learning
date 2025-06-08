import torch 
import torch.nn as nn
import torch.optim as optim

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size, bias=False)
        self.fc2 = nn.Linear(hidden_size, output_size, bias=False)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        return x

    def get_weights(self):
        """Get current weights as a tuple (w1, w2)"""
        w1 = self.fc1.weight.data
        w2 = self.fc2.weight.data
        return w1, w2
    
def train_model(model, train_loader, criterion, optimizer, num_epochs=5):
    model.train()
    for epoch in range(num_epochs):
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = 0.5*criterion(outputs, labels)
            print(f'Loss before backward pass: {loss.item():.4f}')
            loss.backward()
            optimizer.step()
        # Print weights after each epoch
        w1, w2 = model.get_weights()
        print(f'Epoch {epoch+1}/{num_epochs}, Weights: w1={w1.tolist()}, w2={w2.tolist()}')
    

x=torch.tensor([1.0])
y=torch.tensor([1.0])

model=NeuralNetwork(input_size=1, hidden_size=2, output_size=1)
with torch.no_grad():
    model.fc1.weight.fill_(1.0)
    model.fc2.weight.fill_(1.0)
train_loader = [(x, y)]  # Dummy data loader for demonstration
criterion = nn.MSELoss(reduction="sum")
optimizer = optim.SGD(model.parameters(), lr=0.1)

train_model(model, train_loader, criterion, optimizer, num_epochs=1)