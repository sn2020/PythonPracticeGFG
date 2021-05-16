print("Learning Python")
x = 1
y = " Kiaan "
print(x)
print(y)

print(type(x))
print(type(y))

x = str(x)
print(type(x))

fruits = ["apples", "bananas", "orange"]
a = b = c = fruits
print(a)
print(type(b))

x = "awesome"
print("Life is " + x)

a = 1
b = 2

y = a + b
print(y)

x = str(5)
y = "John"
print(x+y)


v = "what u r global"

def testFun():
    global v
    v = "lets play with global"
    print("Lets see what global has", v)

testFun()

v = "dont be global"
print("Global from outside function", v)


a = -123333
b = 222222222222222222222
print(type(a))
print(type(b))


x = float("4.2")
print(x)

s = "Hello World!"
print(s[1:6])
print(s[-5:-1])


b = "Good Lord"
print(type (b.split(" ")))

age = 5
date = 29
month = 8
message = "My age is {} born on {} in month {}"

print(message.format(age, date, month))

print("we r \"Vikings\" from the North\n")

#a = "12345!"
a = "\u0030"
print(a.isdigit())

txt = "apple, banana, orange"
x = txt.rsplit(", ")
print(x)

myTuple = ("apple", "banana", "orange")
x = "#".join(myTuple)
print(x)

str1 = ""
myList = {"Neon ", "is ", "catchy"}
x = str1.join(myList)
print(type(x))
print(x)

ListFruits = ["apple", "cherry", "banana", "apple", "orange"]
print(type(ListFruits))

for x in set(ListFruits):
    print(x, ListFruits.count(x))

funnyArray = [1, 2, 3]
print(funnyArray[-3]) #1
print(funnyArray[-2]) #2
print(funnyArray[-1]) #3

names = ['Chris', 'Jack', 'Rabc']
print(names[-1][-1])

names1 = ['Amir', 'bear', 'charlton', 'daman']
names2 = names1
names3 = names1[:]

print(names1)
print(names2)
print(names3)

names2[0] = 'Alice'
names3[1] = 'bob'

list1 = [1, 3, 2]
print(list1 * 1)

print(list("hello"))

n = 0
elementsList = []
n = int(input("Enter the number of element for taking their average"))

for i in range(0, n):
    elem = (int)(input("Enter next element"))
    elementsList.append(elem)


avg = sum(elementsList)/n
print("Average:", avg)
print(round(avg, 2))







