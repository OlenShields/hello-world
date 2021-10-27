userText = input("Enter plaintext: ")
distanceValue = int(input("Enter the distance value: "))
plainText = ""
for ch in userText:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distanceValue
    plainText += chr(cipherValue)
print(plainText)
