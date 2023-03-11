num1, operator, num2 = input("enter calculation: ").split()
#convert to interger
num1 =int(num1)
num2 =int(num2)

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
if operator == "*":
    print("{} * {} = {}".format(num1, num2,num1 * num2))
if operator == "/":
    print("{} / {} = {}".format(num1, num2,num1 / num2))
if operator == "%":
    print("{} % {} = {}".format(num1, num2,num1 % num2))