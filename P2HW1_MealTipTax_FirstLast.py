## this will create a program that calculates the total amount of a meal purchased at a restaurant.
## 9/24/2019
##CTI-110 P2HW1-Meal Tip Tax Calculator
##Alex Rodriguez
#

meal=float(input("How much did your meal cost: "))

tip=float(input("Please enter a tip (remember that this is in decimal form): "))

tax=float(input("Please enter the tax amount(remember that this is in decimal form): "))

total_cost = meal+(meal * tip) + (meal * tax)

print("Your total meal cost is:$ %.2f" %total_cost)
