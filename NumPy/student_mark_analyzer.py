print("Student Marks Analyzer")

import numpy as np
marks = np.array([78, 65, 92, 37, 88, 73, 49, 95, 81, 67])

print("\nThe total marks are: ",np.sum(marks))
print("The average marks are: ",np.average(marks))
print("The maximum marks are: ",np.max(marks))
print("The minimum marks are: ",np.min(marks))
print("The median of marks is: ",np.median(marks))

print("The standard deviation of marks are: ",np.std(marks))
print("The variance of marks are: ",np.var(marks))

passed = marks[marks >= 50]
failed = marks[marks < 50]

print("The passed student marks are:", passed)
print("The failed student marks are:", failed)

print("Number of passed students:", np.sum(marks >= 50))
print("Number of failed students:", np.sum(marks < 50))