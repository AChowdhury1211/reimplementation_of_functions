import pandas as pd
import pyperclip

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-', "" : " "
}
class morse:
    def encryption(self, msg):
        encrypt = ""
        for i in msg:
            if i != " ":            
                encrypt += MORSE_CODE_DICT[i] + " "
            else:
                encrypt += "  "
            
        return encrypt        
    
    def decryption(self, encrypt): ## T
        encrypt = encrypt.split(" ")
        msg = ""
        for i in encrypt:
            for key , j in MORSE_CODE_DICT.items():
                if i == j:
                    msg += key
            if i == "":
                msg += " "
        return msg
    
    
obj = morse()
choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
if choice == 'E':
    a = obj.encryption(str(input("Enter sentence to encrypt: ")).upper())
    print(a)
choice2 = input("Do you want to Decrypt the above Encrypted text, Choose: 'C' :").upper()
if choice2 == "C":
    b = obj.decryption(a)
    print(b)

else:
    print("Invalid choice. Please enter 'E' or 'D'.")
    
    





