
input_name = open('name.txt', 'w')
name = input("Enter name: ")
print('name', file=input_name)
input_name.close()

name_read = open('name.txt', 'r')
print("Your name is {}".format(name))
name_read.close()

numbers_open = open('numbers.txt', 'r')
number1 = int(numbers_open.readline())
number2 = int(numbers_open.readline())
print(number1 + number2)
numbers_open.close()


