""""Program to calculate and display a users bonus bonus based on sales.
If sales are under $1000, the user gets a 10% bonus.
If sales are $1000 or over, bonus is 15%"""

sales = float(input("Enter sales: $"))

while sales < 0:
    print('Invalid number. Please enter valid number to obtain bonus')
    sales = float(input("Enter sales: $"))

if sales < 1000:
    bonus = sales * 0.1
else:
    bonus = sales * 0.15
print("Bonus comes to: $%.2f" % bonus)
