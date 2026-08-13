import numpy as np

temperatures = np.array([
    [28.5, 30.2, 31.8, -np.inf, 27.9, 32.1, 33.5],
    [25.4, 26.8, np.nan, 30.5, 31.2, 28.7, 27.5],
    [np.nan, 36.8, 38.1, 37.5, 39.2, np.nan, 41.3],
    [22.5, 24.1, np.inf, 25.6, 26.2, 27.4, 28.0],
    [30.1, 31.5, np.nan, 34.2, 35.8, np.inf, 37.1],
    [18.5, 20.2, 21.8, np.nan, 23.4, 24.1, -np.inf],
    [np.nan, 31.2, 250.0, 30.8, np.inf, 33.1, 34.0]
])

print("       TEMPERATURE ANALYTICS SYSTEM")

print("\nOriginal Temperature Data:")
print(temperatures)

print("\n********** BASIC INFORMATION **********")

print("Shape:", temperatures.shape)
print("Size:", temperatures.size)
print("Dimensions:", temperatures.ndim)

print("\n********** DATA QUALITY **********")

nan_mask = np.isnan(temperatures)
inf_mask = np.isinf(temperatures)

print("\nNaN locations:")
print(nan_mask)

print("\nInfinity locations:")
print(inf_mask)

total_nan = np.sum(nan_mask)
total_inf = np.sum(inf_mask)

print("\nTotal NaN values:", total_nan)
print("Total Infinity values:", total_inf)

print("\n********* VALID TEMPERATURES *********")

finite_mask = np.isfinite(temperatures)

valid_temperatures = temperatures[finite_mask]

print("Valid temperatures:")
print(valid_temperatures)

print("\nValid Mean:", np.mean(valid_temperatures))
print("Valid Median:", np.median(valid_temperatures))
print("Valid Maximum:", np.max(valid_temperatures))
print("Valid Minimum:", np.min(valid_temperatures))
print("Valid Standard Deviation:", np.std(valid_temperatures))
print("Valid Variance:", np.var(valid_temperatures))

print("\n********** OUTLIER DETECTION **********")

outlier_mask = temperatures > 50

print("Values greater than 50:")
print(temperatures[outlier_mask])

outlier_indices = np.where(outlier_mask)

print("\nOutlier indices:")
print(outlier_indices)

print("\n********** TEMPERATURE FILTERING **********")

above_35 = temperatures[temperatures > 35]
below_25 = temperatures[temperatures < 25]
above_30 = temperatures[temperatures >= 30]

between_25_35 = temperatures[
    (temperatures >= 25) & (temperatures <= 35)
]

print("Temperatures above 35:")
print(above_35)

print("\nTemperatures below 25:")
print(below_25)

print("\nTemperatures 30 or above:")
print(above_30)

print("\nTemperatures between 25 and 35:")
print(between_25_35)


print("\n********** DATA CLEANING **********")

# Mean of all finite values except the outlier
normal_values = valid_temperatures[valid_temperatures <= 50]

normal_mean = np.mean(normal_values)

print("Normal temperature mean:", normal_mean)


# Replace NaN and infinity
cleaned_temperatures = np.nan_to_num(
    temperatures,
    nan=normal_mean,
    posinf=normal_mean,
    neginf=normal_mean
)


# Replace outliers (> 50) with normal mean
cleaned_temperatures = np.where(
    cleaned_temperatures > 50,
    normal_mean,
    cleaned_temperatures
)


print("\nCleaned Temperature Data:")
print(cleaned_temperatures)


print("\n********** BEFORE VS AFTER **********")

print("\nBefore Cleaning:")
print("Mean:", np.mean(valid_temperatures))
print("Median:", np.median(valid_temperatures))
print("Maximum:", np.max(valid_temperatures))
print("Minimum:", np.min(valid_temperatures))

print("\nAfter Cleaning:")
print("Mean:", np.mean(cleaned_temperatures))
print("Median:", np.median(cleaned_temperatures))
print("Maximum:", np.max(cleaned_temperatures))
print("Minimum:", np.min(cleaned_temperatures))


print("\n********** CITY ANALYSIS **********")

city_average = np.mean(cleaned_temperatures, axis=1)
city_maximum = np.max(cleaned_temperatures, axis=1)
city_minimum = np.min(cleaned_temperatures, axis=1)

print("Average temperature of each city:")
print(city_average)

print("\nMaximum temperature of each city:")
print(city_maximum)

print("\nMinimum temperature of each city:")
print(city_minimum)

hottest_city_index = np.argmax(city_average)
coldest_city_index = np.argmin(city_average)

print("\nHottest city index:", hottest_city_index)
print("Coldest city index:", coldest_city_index)


print("\n********** DAY ANALYSIS **********")

day_average = np.mean(cleaned_temperatures, axis=0)
day_maximum = np.max(cleaned_temperatures, axis=0)
day_minimum = np.min(cleaned_temperatures, axis=0)

print("Average temperature of each day:")
print(day_average)

print("\nMaximum temperature of each day:")
print(day_maximum)

print("\nMinimum temperature of each day:")
print(day_minimum)

hottest_day_index = np.argmax(day_average)
coldest_day_index = np.argmin(day_average)

print("\nHottest day index:", hottest_day_index)
print("Coldest day index:", coldest_day_index)



print("\n********** TEMPERATURE COUNTS **********")

count_above_35 = np.sum(cleaned_temperatures > 35)
count_below_25 = np.sum(cleaned_temperatures < 25)

print("Temperatures above 35:", count_above_35)
print("Temperatures below 25:", count_below_25)



print("\n********** CELSIUS TO FAHRENHEIT **********")

fahrenheit = cleaned_temperatures * 9 / 5 + 32

print("Temperature in Fahrenheit:")
print(fahrenheit)



print("\n********** BROADCASTING **********")

adjustments = np.array([
    1.5,
    -0.5,
    2.0,
    1.0,
    -1.0,
    0.5,
    0.0
])

adjusted_temperatures = (
    cleaned_temperatures + adjustments[:, np.newaxis]
)

print("Adjustments:")
print(adjustments)

print("\nAdjusted temperatures:")
print(adjusted_temperatures)



print("\n********** DAILY TEMPERATURE CHANGE **********")

daily_change = np.diff(cleaned_temperatures, axis=1)

print("Daily temperature changes:")
print(daily_change)

print("\nTemperature increased:")
print(daily_change > 0)

print("\nTemperature decreased:")
print(daily_change < 0)

print("\nTemperature unchanged:")
print(daily_change == 0)



print("\n********* NORMALIZATION *********")

mean_temperature = np.mean(cleaned_temperatures)
std_temperature = np.std(cleaned_temperatures)

normalized_temperatures = (
    (cleaned_temperatures - mean_temperature)
    / std_temperature
)

print("Normalized temperatures:")
print(normalized_temperatures)



print("\n********** ADVANCED INDEXING **********")

print("\nFirst 2 cities:")
print(cleaned_temperatures[:2])

print("\nLast 2 cities:")
print(cleaned_temperatures[-2:])

print("\nFirst 3 days:")
print(cleaned_temperatures[:, :3])

print("\nLast 3 days:")
print(cleaned_temperatures[:, -3:])

print("\nAlternate cities:")
print(cleaned_temperatures[::2])

print("\nAlternate days:")
print(cleaned_temperatures[:, ::2])

print("\nTop-left 3x3:")
print(cleaned_temperatures[:3, :3])

print("\nBottom-right 2x3:")
print(cleaned_temperatures[-2:, -3:])



print("\n********** TOP 5 TEMPERATURES **********")

sorted_temperatures = np.sort(
    cleaned_temperatures.flatten()
)

top_5 = sorted_temperatures[-5:][::-1]

print("Top 5 temperatures:")
print(top_5)


print("\n*************************")
print("  FINAL TEMPERATURE REPORT")
print("  ************************* ")

print("Dataset Shape:", temperatures.shape)
print("Total Readings:", temperatures.size)

print("Missing Values:", total_nan)
print("Infinity Values:", total_inf)
print("Outliers:", len(temperatures[outlier_mask]))

print("Original Mean:", np.mean(valid_temperatures))
print("Cleaned Mean:", np.mean(cleaned_temperatures))

print("Original Maximum:", np.max(valid_temperatures))
print("Cleaned Maximum:", np.max(cleaned_temperatures))

print("Original Minimum:", np.min(valid_temperatures))
print("Cleaned Minimum:", np.min(cleaned_temperatures))

print("Hottest City Index:", hottest_city_index)
print("Coldest City Index:", coldest_city_index)

print("Hottest Day Index:", hottest_day_index)
print("Coldest Day Index:", coldest_day_index)

print("Temperatures Above 35°C:", count_above_35)
print("Temperatures Below 25°C:", count_below_25)

print("Top 5 Temperatures:", top_5)
