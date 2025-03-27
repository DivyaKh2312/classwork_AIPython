import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.hstack((a, b))
result1 = np.vstack((a, b))
print(result)
print(result1)

result2 = np.vstack((a, b))

# Traverse through all elements using two  i, j
#for i in range(result2.shape[0]):  # Loop through rows
    #for j in range(result2.shape[1]):  # Loop through columns
        #print(f"Element ({i}, {j}): {result2[i, j]}")

plt.hist(result2)
plt.show()

plt.bar(a,b,color="green")
plt.show()

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a = a.reshape(4,3)
n,m = np.shape(a)
print(a)
for i in range(n):
    for j in range(m):
        print("Element",i,j, "is" , a[i,j])

result3 = np.vstack((a))
print("Before deletion",result3)
a_new = np.delete(result3, 0, axis=1)
print("Array after deletion:")
print(a_new)

for index in np.nditer(a):
    print(index)


