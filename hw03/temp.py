import torch
import torch.optim as optim

# Data samples: (x, t)
X = torch.tensor([-1.0, 0.0, 1.0, 1.0])
T = torch.tensor([1.0, 1.0, 1.0, 0.0])

# Initialize parameters as torch.nn.Parameter so gradients are tracked.
# We use:
#   w0  -> bias (w")
#   w1  -> coefficient multiplying x (w#)
#   w2  -> parameter inside cosine (w!), note that cos(w2) is a constant multiplier.
w0 = torch.nn.Parameter(torch.randn(1))  # Random initialization
w1 = torch.nn.Parameter(torch.randn(1))  # Random initialization
w2 = torch.nn.Parameter(torch.randn(1))  # Random initialization

# Set up an optimizer (using SGD) with a chosen learning rate.
optimizer = optim.SGD([w0, w1, w2], lr=0.01)

iterations = 10000

for i in range(iterations):
    optimizer.zero_grad()  # reset gradients
    
    # Define the model:
    # f(x) = w1 * x + cos(w2) * x + w0 = x * (w1 + cos(w2)) + w0
    y_pred = X * (w1 + torch.cos(w2)) + w0
    
    # Compute the loss: sum of squared errors.
    loss = torch.sum((T - y_pred) ** 2)
    
    # Backpropagation: compute gradients
    loss.backward()
    
    # Update parameters using the optimizer (batch gradient descent).
    optimizer.step()
    
    # Print progress every 1000 iterations to observe convergence.
    if i % 1000 == 0:
        print(f"Iteration {i:4d}: Loss = {loss.item():.5f}, w0 = {w0.item():.5f}, w1 = {w1.item():.5f}, w2 = {w2.item():.5f}")

print("Final parameters:")
print(f"w0 = {w0.item():.5f}, w1 = {w1.item():.5f}, w2 = {w2.item():.5f}")
print(f"Final loss: {loss.item():.5f}")

# Plot the resulting function (optional):
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x * (w1.item() + np.cos(w2.item())) + w0.item()

x_plot = np.linspace(-2, 2, 200)
y_plot = [f(x) for x in x_plot]

plt.figure(figsize=(7,5))
plt.plot(x_plot, y_plot, label="Learned f(x)")
plt.scatter(X.numpy(), T.numpy(), color="red", s=60, label="Data points")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Learned Function vs. Data")
plt.legend()
plt.grid(True)
plt.show()
