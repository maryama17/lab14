"""
Program: Lab14_mhasan6_1.py
Author: Maryama Hasan
Purpose: This program plots a sine wave using the matplotlib and math modules.
Date: August 5, 2025
"""

import math
import matplotlib.pyplot as plt

x_values = list(range(0, 361))  
y_values = [math.sin(math.radians(x)) for x in x_values]

plt.plot(x_values, y_values, label='sin(x)', color='blue', linewidth=4)


plt.title("Sine Wave")
plt.xlabel("Degrees")
plt.ylabel("Sine Value")
plt.grid(True)
plt.legend()


plt.show()
