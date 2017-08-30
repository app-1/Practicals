
numbers = []


for number in range(5):
    start = float(input('Number: '))
    numbers.append(start)

average = sum(numbers) / len(numbers)

print('The last number is {}'.format(numbers[4]))
print('The first number is {}'.format(numbers[0]))
print('The smallest number is {}'.format(min(numbers)))
print('The largest number is {}'.format(max(numbers)))
print('The average of the numbers {}'.format(average))



