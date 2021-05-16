print("Program to check a number is armstrong or not")
num: int = 0
num = int(input("Enter a number"))
originalnum = num
newnum: int =0
sum: int =0
rem: int =0
print(num)
while (num > 0):
    rem = num % 10
    num = num // 10

    newnum = rem + sum
    sum = newnum

if(originalnum == originalnum):
    print("Number " " is a palindrome.", +originalnum)
else:
    print("Number " " not a palindrome.", +originalnum)
