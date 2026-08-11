print("Array Cleaner")

import numpy as np

data = np.array([
    57, 45, np.nan, 40,
    np.inf, 69, 77, np.nan,
    21, -np.inf
])

print("\nThe data is:", data)

valid_values = data[np.isfinite(data)]
print("The valid values are: ",valid_values)

print("\nNote: True means the value is present")

print("\nNaN present in array:")
print(np.isnan(data))

print("\nInfinity present in array:")
print(np.isinf(data))


print("\nCleaning the data")

cleaned_data = np.nan_to_num(
    data,
    nan=9,
    posinf=1000,
    neginf=-1000
)

print("Cleaned data:", cleaned_data)

print("\nMedian of cleaned data:", np.median(cleaned_data))
print("Mean of cleaned data:", np.mean(cleaned_data))