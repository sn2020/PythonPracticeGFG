#strIn = input("Enter str1")

def palindrome(strIn):
    strOut = strIn[::-1]
    print(strOut)
    if (strIn == strOut):
        print("true")
        return True
    else:
        print("false")
        return False

palindrome("abba")
palindrome("rotator")
palindrome("Code")
palindrome("rotatro")






