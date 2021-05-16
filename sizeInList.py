print("Finding highest in a list")
n = int(input("enter number of elements in list"))
mylist = []

for i in range(1, n+1):
    b = int(input("List elements"))
    mylist.append(b)
    mylist.sort()

print("Second largets number ", mylist[-2])

