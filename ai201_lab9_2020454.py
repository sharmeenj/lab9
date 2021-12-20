
#Task 1

def Cipher_Encryption(text,shift):
    
    output = " "
    
    for i in range(len(text)):

        char = text[i]
     
        if (char.isupper()):

            output += chr((ord(char) + shift - 65) % 26 + 65)

        else:

            output += chr((ord(char) + shift - 97) % 26 + 97)
         
    return output
        
    
    
text = str(input("Enter Text : "))    

shift = int(input("Enter Shift : "))

print("\n")


print("Plain Text : " + text)

print("Shift pattern : " + str(shift))

print("Cipher: " + Cipher_Encryption(text,shift))


print("\n")

#Task 2

print("change madeeeeeee")

message = 'KLMLUKAOLMVYA' 

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    
    translated = " "
   
    for symbol in message:
       
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
         
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
         
    print('Hacking key #%s: %s' % (key, translated))

