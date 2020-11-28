def line():
	print('*'*50)


#Task 1
my_list = [1,2,3,4,5,6,7,8]

for i in range(len(my_list)):
	my_list[i] += 2

print(my_list)
line()

#Task 2

def pattern(num):
	if num == 0:
		return 
	for i in range(num,0,-1):
		print(i,end='')
	print()
	pattern(num - 1)


pattern(5)

line()


#Task 3

def fib(nterms):
	count = 0
	n1, n2 = 1,1
	while count < nterms:
		print(n1)
		nth = n1 + n2
		n1 = n2
		n2 = nth
		count += 1

fib(10)
line()

#Task 4
num = 153
sum = 0
temp = num

while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


line()

#Task 5

for i in range(13):
	print(f'9 x {i} = {9 * i}')

line()

#Task 6

number = -5

print('positive' if number >= 0 else 'negative')

line()

#Task 7

days = 366

print(f'years = {days / 365}')

line()


#Task 8

from math import cos,sin

print(cos(45) * cos(45) + sin(45) * sin(45))


line()


#Task 9

print('Calculator')
line()

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
line()

while True:
    line()
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
        print('Exiting....')
        break

