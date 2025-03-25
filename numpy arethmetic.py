import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

#sum
c = a + b
print("sumation is:", c)

#sub
c = a - b
print("substraction is:",c)

#multiply
c = a * b
print("multiplication is:",c)

#divide
c = a / b
print("division is :", c)

#sin
c = np.sin(a)
print("sin is : ", c)

#cos
c = np.cos(a)
print("cos is :" ,c)

#tan
c = np.tan(a)
print("tan is : ", c)

#square
c = np.square(a)
print("square is :", c)

# Minus 1
c = a - 1
print("a -1:" ,c)


# Add 2 to each element
c = a + 2
print("a + 2:", c)

# elements that are greater than or equal to 1
y1 = a >= 1
print("a >= 1:", y1)

# elements that are less than or equal to 1
y2 = a <= 1
print("a <= 1:", y2)

Matmul =a@b
Matmul1 =np.matmul(a,b)
Matmul2 = np.dot(a,b)
print("Matmul is:", Matmul)
print("Matmul1 is:", Matmul1)
print("Matmul2 is:", Matmul2)

n = np.arange(1, 13)
reshape = np.reshape(n, (3, 4))
rows,cols = np.shape(reshape)
print(rows, cols)
