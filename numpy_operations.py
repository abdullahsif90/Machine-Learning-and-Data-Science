import numpy as np

list_of_numbers = int(input("How many numbers you want to enter: "))
numbers = []
for i in range(list_of_numbers):
    num = int(input("Enter the number: "))
    numbers.append(num)
array = np.array(numbers)
print("The minimum value in the array is:", np.min(array))
print("The maximum value in the array is:" , np.max(array))
print("The mean value of the array is:", np.mean(array))
print("The standard deviation of the array is:", np.std(array))
print("The sum of the array is:", np.sum(array))
print("The vairance of array: ",np.var(array))