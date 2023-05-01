def decryption(message,key):
    for i in range(26):
        encryption =""
        KEY =i
        for char in list(message):
            ASCII=ord(char)
            if (ASCII == 32):                   # if ASCII is SPC, make space.
                encryption += " "
                continue
            if (122 >= ASCII and ASCII >= 97):  # if ASCII is lower
                num = ASCII - 97
                num = (num + KEY) % 26
                ASCII = num + 97
                encryption += chr(ASCII)
            elif (90 >= ASCII and ASCII >= 65): # if ASCII is upper
                num = ASCII - 65
                num = (num + KEY) % 26
                ASCII = num + 65
                encryption += chr(ASCII)
            else :                              # if ASCII is symbol
                encryption += chr(ASCII)
        if KEY ==3:
            return encryption
message =input("Enter your code : ")
key=3
code = decryption(message,key)
print("Your message coded is ",code)