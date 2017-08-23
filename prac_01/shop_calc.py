total = 0
items = int(input("Number of items: "))

while items < 0:
    print('Invalid number of items! Re-enter:')
    items = int(input("Number of items: "))

for i in range(items):
    price = float(input('Price of item: $'))
    total += price
if total > 100:
    discount = total * 0.1
    Total_discount = total - discount
    print('Total exceeds $100. Therefore discount applied. New total comes to ${:.2f}'.format(Total_discount))
else:
    print('Total cost of items comes to ${:.2f}'.format(total))
