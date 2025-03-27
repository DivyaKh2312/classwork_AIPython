import matplotlib.pyplot as plt
import numpy as np

x=np.array([2020,2021,2022,2023,2024,2025])
y = np.array([7,8,9,10,14,20])
y_fah = (y * 9/5) + 32
k = x + 273.15
#lables of graph
  #plt.xlabel('X-axis (Years)')  # Correct way to label X-axis
  #plt.ylabel('Y-axis (Temperature)')
  #plt.title('Temperature in celsius')

#graph line with attribute of color and marker etc.
  #plt.plot(x,y_fah, color='red', marker='*', markersize=10, label='celsius', linewidth=4, linestyle='--')
  #plt.plot(x,y, color='blue', marker='*', markersize=10, label='Fahrenhite', linewidth=4, linestyle='-.')

plt.title('Temperature in helsinki in last 6 years')


# First subplot (Celsius)
plt.subplot(1, 3, 1)
plt.plot(x,y, 'bo--', label = 'celsius')
plt.xlabel('Years')
plt.ylabel('Temperature (°C)')
plt.legend()

# Second subplot (Fahrenheit)
plt.subplot(1, 3, 2)
plt.plot(x,y_fah, 'r*-',label = 'fahrenheit')
plt.xlabel('Years')
plt.ylabel('Temperature (°F)')
#it gives lable to lines
plt.legend()

#Third subplot (Kelvin)
plt.subplot(1, 3, 3)
plt.plot(x,k, 'bo--', label = 'kelwin')
plt.xlabel('Years')
plt.ylabel('Temperature (°K)')
plt.legend()

#plt.subplots_adjust(wspace=0.6)
plt.tight_layout()

#for saving graph as picture in folder also can be save as pdf
plt.savefig('pic.png')
#printing of graph
plt.show()
