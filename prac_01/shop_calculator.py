
total_price = 0
item_prices = []
count = 1
amount_items = int(input("Please enter the amount of items for checkout: "))
while amount_items < 0:
    amount_items = int(input("Number of items must be greater then 0. Try again: "))

for i in range(1, amount_items + 1):
    item_price = float(input("Please enter price of item {}: ".format(i)))
    item_prices.append(item_price)
    total_price = total_price + item_price

for i in item_prices:
    print("Price for item {}: ${}".format(count, item_prices[count - 1]))
    count += 1
if total_price > 100:
    total_price = total_price - (total_price * 0.10)
else:
    pass

print("Total price for {} items is ${}".format(amount_items, total_price))
