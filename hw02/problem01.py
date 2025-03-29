import numpy as np
import math

np.set_printoptions(precision=4, suppress=True)
# Data: [ID, Age, HP, Brand, MPG, Price]
Data=np.array([[1,2,200,4,27,30000],[2,5,150,3,35,20000],[3,3,180,4,25,25000],[4,1,230,2,10,21000],[5,5,180,5,40,38000],[6,4,210,3,30,31000]])

# Model: Price=w3*HP/Age+w2*log(HP)+w1*Brand*sqrt(MPG)+w0
H=np.array([])
H = []
for i in range(0, len(Data)):
    H.append([1, Data[i][3] * math.sqrt(Data[i][4]), math.log(Data[i][2]), Data[i][2] / Data[i][1]])
H = np.array(H)
print("H: ", H)
Y=np.array([])
for i in range(0, len(Data)):
    Y=np.append(Y, Data[i][5])

print("Y: ", Y)

A=H.T.dot(H)
print("A: ", A)

B=H.T.dot(Y)
print("B: ", B)

w=np.linalg.inv(A).dot(B)
# np.set_printoptions(precision=2, suppress=True)
print("w: ", w)