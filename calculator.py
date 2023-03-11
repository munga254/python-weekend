while True:
    try:
        num1, operator, num2 = input("enter calculation: ").split()
        break
    except  ValueError:
        print("Syntax Error")
#convert to interger
num1 =int(num1)
num2 =int(num2)

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2,num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2,num1 / num2))
elif operator == "%":
    print("{} % {} = {}".format(num1, num2,num1 % num2))
else:
    print("error")