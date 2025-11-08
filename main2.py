num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
num3=num2
for x in range(num1-1):
    num2=num3+num2
print(num2)