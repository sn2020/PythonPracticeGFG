charX = input('Enter a character')

print(type(charX))

#if charX == 'a' or charX == 'e' or charX == 'i' or charX == 'o' or charX == 'u':
 #   print("It's a vowel", charX)
#else:
 #   print("It's not a vowel")

if charX.lower() in "aieou":
    print("charX.lower()")
    print("its a vowel")
else:
    print(charX.lower())
    print("Not a vowel")

