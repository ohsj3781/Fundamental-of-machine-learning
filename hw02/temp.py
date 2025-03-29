import numpy as np

X=np.array([[1,2],[1,3],[1,6],[1,7],[1,8],[1,10],[1,14],[1,15],[1,16],[1,17],[1,18]])

Y=np.array([2,4,4,9,10,6,10,13,18,14,16])

A=X.T.dot(X)
B=X.T.dot(Y)

w=np.linalg.inv(A).dot(B)

print(w)