def encrypt():
    cipherText = ""
    alp = []
    plainText = input("Enter the plain Text to encrypt: ")
    for n in range(len(plainText)):
        if plainText[n] == 'Z':
            alp.append('A')

        else:
            alp.append(chr(ord(plainText[n])+1))

    print("The cipher Text is: "+cipherText.join(alp))


def decrypt():
    plainText = ""
    alp = []
    cipherText = input("Enter the cipher Text: ")
    for n in range(len(cipherText)):
        if cipherText[n] == 'A':
            alp.append('Z')
        else:
            alp.append(chr(ord(cipherText[n])-1))

    print("The plain Text is: "+plainText.join(alp))


userInput = int(
    input("Enter the choices: 1 to encrypt data 2 to decrypt data: "))

if userInput == 1:
    encrypt()

else:
    decrypt()
