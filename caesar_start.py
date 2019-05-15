# Script:  caesar.py
# Desc:    encrypt and decrypt text with a Caesar cipher
#          using defined character set with index
# Author:  Petra Leimich
# Created: 23/9/17
# note that you should add a module doc string!

charset="ABCDEFGHIJKLMNOPQRSTUVWXYZ" # characters to be encrypted
numchars=len(charset) # number of characters, for wrapping round

#####Default Demo Encryption Function #####
def caesar_encrypt(plaintext,key):
    """put an appropriate function doc string here"""
    print (f'[*] ENCRYPTING - key: {key}; plaintext: {plaintext}')
    plaintext=plaintext.replace(" ", "") 
    plaintext=plaintext.upper()     # convert plaintext to upper case
    ciphertext=''    # initialise ciphertext as empty string   
    for ch in plaintext:
        if ch in charset:
            pos=charset.find(ch)
            pos=pos+key
            pos=pos%26             
            new=str((charset[pos])) # replace this with your code, may use extra lines
        else:
            new=ch # do nothing with characters not in charset
        ciphertext=ciphertext+new
    print (f'[*] ciphertext: {ciphertext}')
    print (f'')
    return ciphertext # returns ciphertext so it can be reused

#####Default Demo Decryption Function #####
def caesar_decryptcrack(ciphertext,key):
    """put an appropriate function doc string here"""
    # very similar to caesar_encrypt(), but shift left
    plaintext=''   # replace this with your code 
    #plaintext=plaintext.upper()     # convert plaintext to upper case
    ciphertext=ciphertext.upper()
    for ch in ciphertext:
        if ch in charset:
            pos=charset.find(ch)
            pos=pos-key
            pos=pos%26 
            new=str((charset[pos])) # replace this with your code, may use extra lines
        else:
            new=ch # do nothing with characters not in charset
        cipher=str(ciphertext)
        plaintext=plaintext+new
        str(plaintext)
        ciphertext=ciphertext.replace(ciphertext, "") 
    print (f'[*] DECRYPTING - key: {key}; plaintext: {plaintext}')
    return ciphertext # returns plaintext so it can be reused


#####Default Demo Crack Function #####
import time
start_time = time.time()
def caesar_crack(ciphertext):
    c=len(charset)
    for x in range(c):
        crack=caesar_decryptcrack(ciphertext,x)
        print("--- %s seconds ---" % (time.time() - start_time))
        print(crack)
    """put an appropriate function doc string here"""
    # how could you brute force crack a caesar cipher?
    # your code here


#Validate Input for A-Z
#Direct Implementation of the "https://stackoverflow.com/questions/27591977/python-validate-for-a-z-or-a-z"
#Author=inspectorG4dget
#EasilyUnderstandable
def containsOnly(s, whitelist):
    whitelist = set(whitelist)
    for char in s:
        if char not in whitelist:
            return False
    return True

#Validate Input for A-Z
#Reference to "https://stackoverflow.com/questions/27591977/python-validate-for-a-z-or-a-z"
#Author=inspectorG4dget
#EasilyUnderstandable
def containsKey(s, whitelist):
    whitelist = set(whitelist)
    for char in s:
        if char not in whitelist:
            return False
    return True



### Sample Code Ends Here!
### Own Ideas and Codes Start Here.

#####Custom Encryption Function #####
def input_encrypt(plaintext,key):
    """put an appropriate function doc string here"""
    plaintext = input("Enter Your PlainText:")
    plaintext=plaintext.replace(" ", "") #Replace Every Space with Nothing. It means deleting using Replace Method of string Object.
    plaintext=plaintext.upper()     # convert plaintext to upper case. Upper Method of String Object.
    ciphertext=''    # initialise ciphertext as empty string   
    key = input("Enter Your Key For Better Cipher Algorithm:")
    key = int(key)
    print (f'[*] ENCRYPTING - key: {key}; plaintext: {plaintext}')
    if containsOnly(plaintext, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '):
        for ch in plaintext:
            if ch in charset:
                pos=charset.find(ch)
                pos=pos+key
                pos=pos%26   
                new=str((charset[pos])) # replace this with your code, may use extra lines
            else:
                new=ch # do nothing with characters not in charset
            ciphertext=ciphertext+new
    else:
        print("Caution! Please Type Characters with A-Z")  #if the input contains characters except from A-Z, it shows up.
        print (f'')
    print (f'[*] ciphertext: {ciphertext}')
    print (f'')
    return ciphertext # returns ciphertext so it can be reused


#####Custom Decryption Function #####
def input_decrypt(ciphertext,key):
    """put an appropriate function doc string here"""
    # very similar to caesar_encrypt(), but shift left
    ciphertext = input("Enter Your Cipher Text:")
    key = input("Enter Your Key For Better Cipher Algorithm:")
    key = int(key)
    print (f'[*] DECRYPTING - key: {key}; ciphertext: {ciphertext}')
    plaintext=''   # replace this with your code 
    ciphertext=ciphertext.upper()
    if containsOnly(ciphertext, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        for ch in ciphertext:
            if ch in charset:
                pos=charset.find(ch)
                pos=pos-key
                pos=pos%26 
                new=str((charset[pos])) # replace this with your code, may use extra lines
            else:
                new=ch # do nothing with characters not in charset
            cipher=str(ciphertext)
            plaintext=plaintext+new
            str(plaintext)
            ciphertext=ciphertext.replace(ciphertext, "") 
    else:
        print("Caution! Please Type Characters with A-Z")
        print (f'')
    print (f'[*] plaintext: {plaintext}')
    print (f'')
    return ciphertext # returns plaintext so it can be reused


#####Crack Function #####
def input_crack(ciphertext):
    import time
    start_time = time.time()
    ciphertext = input("Enter Your Custom Cipher Text To Be Cracked:")
    c=len(charset)
    if containsOnly(ciphertext, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        for x in range(c):
            crack=caesar_decrypt(ciphertext,x)
            print("--- %s seconds ---" % (time.time() - start_time))
            print(crack)
    else:
        print("Caution! Please Type Characters with A-Z")
        print (f'')
    """put an appropriate function doc string here"""
    # how could you brute force crack a caesar cipher?
    # your code here


#####Decryption Function For Input Crack#####
def caesar_decrypt(ciphertext,key):
    """put an appropriate function doc string here"""
    # very similar to caesar_encrypt(), but shift left
    print (f'Cipher Text to be Cracked: {ciphertext}')
    plaintext=''   # replace this with your code 
    #plaintext=plaintext.upper()     # convert plaintext to upper case
    ciphertext=ciphertext.upper()
    for ch in ciphertext:
        if ch in charset:
            pos=charset.find(ch)
            pos=pos-key
            pos=pos%26 
            new=str((charset[pos])) # replace this with your code, may use extra lines
        else:
            new=ch # do nothing with characters not in charset
        cipher=str(ciphertext)
        plaintext=plaintext+new
        str(plaintext)
        ciphertext=ciphertext.replace(ciphertext, "") 
    print (f'[*] DECRYPTING - key: {key}; plaintext: {plaintext}')
    return ciphertext # returns plaintext so it can be reused


def main():
    # test cases
    key=2
    plain1 = 'Hello Suzanne'
    cipher1 = 'IQQfOQtpKpIGXGtaQPG'
    crackme = 'PBATENGHYNGVBAFLBHUNIRPENPXRQGURPBQRNAQGURFUVSGJNFGUVEGRRA' 
    # call functions with text cases
    print("Sample Encrypting Output!")
    caesar_encrypt(plain1, key)
    print("Sample Decrypting Output!")
    caesar_decrypt(cipher1,key)
    print("")
    # remove comment to test cracking
    print("")
    

    while True:
        print("Choose the following:\n1. Enter 'E' to encrypt your own text:\n2. Enter 'D' to decrypt your cipher text:\n3. Enter 'C' to crack ciphertext:\n4. Enter 'S' to see how Cracking Works:\n5. Press any key to Exit:")
        e = input("Enter:")
        if(e=='e' or e=='E' or e=='1'):
            input_encrypt(plain1, key)
        elif(e=='d' or e=='D' or e=='2'):
            input_decrypt(cipher1, key)
        elif(e=='S' or e=='s' or e=='3'):
            print("Sample Cracking Output!")
            print("CipherText To Be Cracked = 'PBATENGHYNGVBAFLBHUNIRPENPXRQGURPBQRNAQGURFUVSGJNFGUVEGRRA'")
            print("")
            caesar_crack(crackme)
        elif(e=='C' or e=='c' or e=='4'):
            input_crack(crackme)
        elif(e=='X' or e=='x' or e=='5'):
            exit()
        else:
            exit()

# boilerplate
if __name__ == '__main__':
    main()
