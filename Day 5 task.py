
#Task 1

def arithmetic():
	number1 = int(input("Please Enter a number:"))
	number2 = int(input("Please Enter a number:"))

	print(f"Addition of two numbers: {number1 + number2}")
	print(f"Subtraction of two numbers: {number1 - number2}")
	print(f"Multiplication of two numbers: {number1 * number2}")
	print(f"Division of two numbers: {number1 / number2}")


arithmetic()


#Task 2

def covid(name, temperature = 98):
	print(name,temperature)

covid('prakash')