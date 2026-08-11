print("Temperature analyzer")

import numpy as np 

temperatures = np.array([
    30.5, 32.1, 29.8, 35.6,
    31.2, 28.9, 40.5, 33.7,
    27.5, 36.2])

print("\nthe average temperature is: ",np.average(temperatures))
print("the maximum temperature is: ",np.max(temperatures))
print("The index no of maximum temperature is: ",np.argmax(temperatures))
print("the minimum temperature is: ",np.min(temperatures))
print("the index no of minimum temperarure is :",np.argmin(temperatures))
print("the median temperature is: ",np.median(temperatures))
print("the standard deviation of temperature is: ",np.std(temperatures))
print("the variance temperature is: ",np.var(temperatures))

print("The temperature greater than 35 are: ",np.sum(temperatures > 35))
print("The temperature less than 35 are: ",np.sum(temperatures < 30))
