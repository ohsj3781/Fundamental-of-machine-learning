import torch
import math

def matMul(A,B):
    # Get the dimensions of the matrices
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # Check if multiplication is possible
    if cols_A != rows_B:
        return None

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

def f(x,w):
    return w[2]*x+math.cos(w[1])*x+w[0]
x=[-1,0,1,1]
y=[1,1,1,0]
w=[1,1,1]

e=[0 for _ in range(len(x))]
for i in range(len(x)):
    e[i]=y[i]-f(x[i],w)

gradient_w0=-2*sum(e)
gradient_w1=0
for i in range(len(x)):
    gradient_w1+=2*e[i]*x[i]*math.sin(w[1]*x[i])
gradient_w2=0
for i in range(len(x)):
    gradient_w2+=-2*e[i]*x[i]
print("Gradient w0: ",gradient_w0)
print("Gradient w1: ",gradient_w1)
print("Gradient w2: ",gradient_w2)