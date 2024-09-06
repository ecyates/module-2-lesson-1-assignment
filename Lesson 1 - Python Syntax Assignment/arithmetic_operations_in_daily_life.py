# Task 1: Grocery Store Math 
# Calculate the total cost of three items you'd commonly find in a grocery store, 
# given their individual prices. For example, what would be the cost of bread, 
# peanut butter, and jelly be? Prices don't need to be realistic!

# First, let's define the items. 
milk_price, butter_price, eggs_price = 6.50, 4.25, 7.00
# Then let's add them together
totalBill = milk_price + butter_price + eggs_price
# Finally, let's announce the grocery bill
print("Your total grocery bill is $" + str(totalBill) + "!")


# Task 2: Bank Interest 
# If you have a savings account with a particular initial amount and a fixed yearly interest rate, 
# calculate the total amount in your account after a year. 
# So if you had $10,000 at a 7% interest, write code that would tell us the amount at the end of the year. 
# For the example the expected outcome would be $10,700.

# Define initial amount in savings account
amount = 10000
# Define annual interest
annualInterest = 0.07
# Multiply them to get the amount earned in a year and add it back to the initial amount
amount += amount * annualInterest
# Report the end of year amount in the savings account
print("Your savings account will have $" + str(amount) + " by the end of the year!")
