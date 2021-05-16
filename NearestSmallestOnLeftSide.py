arrInput = [8, 6, 9, 7, 5]

print("_, ", end="")

for i in range(1 , len(arrInput)):

    for j in range(i-1, -2, -1):
        if arrInput[j] < arrInput[i]:
            print(arrInput[j], ",", end="")
        break

    if(j == -1):
        print("_, ", end="")
