# Name: Barbara Payne
# Assignment 3.1
# Purpose: Gather information from user and provide cost for fiber optic cable installation

# Start of Program - Gather information
from pip._vendor.distlib.compat import raw_input

print("Welcome!")
name = input('What is the name of your company?\n')
print("Price per foot:\n"
      "100 feet or less - $0.87/ft\n"
      "Over 100 feet - $0.80/ft\n"
      "Over 250 feet - $0.70/ft\n"
      "Over 500 feet - $0.50/ft\n")
feet = raw_input("How many feet of fiber optic cable needs to be installed?\n")
try:
    float(feet)
except ValueError:
    print("Only numbers please")

# Price depending on how many feet
if 250 > int(feet) > 100:
    price = .80
elif 500 > int(feet) > 250:
    price = .70
elif int(feet) > 500:
    price = .50
else:
    price = .87

# Sales tax - 6% & Calculated Cost before tax
tax = ((int(feet) * price) * .06) + (int(feet) * price)
calculatedCost = int(feet) * price

# Print the user's receipt
print("\nReceipt for " + name + "\n")
print("Total feet of fiber optic cable: " + feet + "\n")
print("Calculated cost: $" + str(round(calculatedCost, 2)) + "\n")
print("Total Cost: $" + str(round(tax, 2)))
