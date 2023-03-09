print("Basic Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
choice = int(input("Enter your choice: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if(choice==1):
    print("Result: ", num1 + num2)
elif (choice==2):
    print("Result: ", num1 - num2)
elif(choice==3):
    print("Result: ", num1 * num2)
elif(choice==4):
    print("Result: ", num1 / num2)
else:
    print("Thank you")
