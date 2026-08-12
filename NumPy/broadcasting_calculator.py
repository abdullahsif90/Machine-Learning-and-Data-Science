import numpy as np

print("Broadcasting Calculator")

prices = np.array([100, 350, 1000, 430, 500, 750, 870])

tax = 0.10          # 10%
discount = 0.05     # 5%


tax_price = prices * tax


price_after_tax = prices + tax_price


discount_price = price_after_tax * discount


final_price = price_after_tax - discount_price

print("\nOriginal Prices:", prices)
print("Tax Amount:", tax_price)
print("Price After Tax:", price_after_tax)
print("Discount Amount:", discount_price)
print("Final Price:", final_price)