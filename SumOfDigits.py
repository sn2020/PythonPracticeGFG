print("Calculate sum of digits")
num: int = 0
num = int(input("Enter any number "))
remainder: int = 0
sum: int = 0
originalNum: int = num
print("Number entered", num)
while (num > 0):
    remainder = num % 10
    sum = sum + remainder
    num = num //10

print("Sum of digit of " "is", +originalNum, +sum)
