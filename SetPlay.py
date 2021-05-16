str1 = input("Enter first string")
str2 = input("Enter second string")

print(set(str1))
print(set(str2))

a = list(set(str1) | set(str2))
print(type(a))

for i in a:
    print(i)
