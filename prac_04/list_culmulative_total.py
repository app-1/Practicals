month = 0
incomes = []
months = int(input('how many months?: '))

for i in range(months):
    month += 1
    income = float(input('Enter income for month {}: $ '.format(month)))
    incomes.append(income)

print('\nIncome Report\n--------')

total = 0
for month in range(months):
    income = incomes[month - 1]
    total += income
    print('Month {} - Income ${:.2f} Total: ${:.2f} '.format(month, income, total))





