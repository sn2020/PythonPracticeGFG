from sys import stdin, stdout

def main():
#    arr = [int(x) for x in input("Enter list of numbers").split()]
#    print(arr)
    sum = 0
    readVar = [int(x) for x in stdin.readline().split()]

    print("List is of type {}",type(readVar))
    print(readVar)

    for x in readVar:
        sum = sum + x

    print (sum)

if __name__ == "__main__":
    main()




