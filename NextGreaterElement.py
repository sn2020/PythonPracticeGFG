alist = [13, 7, 6, 12]
print ("For list", alist)

for i in range(0, len(alist)):
    next = -1
    for j in range(i+1, len(alist)):
        if alist[i] < alist[j]:
            print(alist[i])
            next = alist[j]
            break

    print(str(alist[i]) + " -- " +str(next))


