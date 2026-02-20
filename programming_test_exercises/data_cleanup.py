# Below is a list of stock data. Note the mess: some prices are strings, one is None, and the dates are just there for context.

# Your Goal: Write a Python for loop that iterates through messy_data and builds a new list called clean_data.

# The Rule: Every price in clean_data must be a float.

# The Memory: If the price is None, use the last valid price you saw.

import array
import copy

messy_data = [
    {"date": "2023-10-01", "price": "150.00"},
    {"date": "2023-10-02", "price": "152.50"},
    {"date": "2023-10-03", "price": None},
    {"date": "2023-10-04", "price": "153.25"}
]

# --- YOUR CODE STARTS HERE ---
last_known_price = 0.0
clean_data = []

# Write your loop here...

for data in messy_data:
  cleaned_data = copy.deepcopy(data)
  if isinstance (cleaned_data["price"], str):
    last_known_price = float(cleaned_data["price"])
  cleaned_data["price"] = last_known_price
  clean_data.append(cleaned_data)

print ("This is the clean data")
print (clean_data)

