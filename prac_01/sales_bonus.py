"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
user_sales = float(input("Please enter the users sales: "))
while user_sales > 0:
    if user_sales >= 1000:
        user_bonus = user_sales * 0.15
        print("Your total sales is over $1000 netting you a 15% bonus totaling ${}".format(user_bonus))
        user_sales = float(input("Please enter the users sales: "))

    else:
        user_bonus = user_sales * 0.10
        print("Your total sales is less than $1000 netting you a 10% bonus totaling ${}".format(user_bonus))
        user_sales = float(input("Please enter the users sales: "))

print("You have entered an incorrect value. Goodbye.")



