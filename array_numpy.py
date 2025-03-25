import numpy as np
#x = np.array([1,2,3,4,5,6])
#y = np.array([1,2,3,4,5,6])
#print(x)
#print(y)
#print(np.shape(x))
#print(np.shape(y))

#y =np.array([[1,2,3],[4,5,6]])
#print(y)
#print(y[1,1])

x=np.array(
    [
        [
        [1,2,3],[3,4,5]
        ],
        [
        [6,7,8],[9,10,11]
        ]
    ] )

print(x)
print(x[0,1,1])
print(x[0,1,2])
print(np.shape(x))
print(np.ndim(x))