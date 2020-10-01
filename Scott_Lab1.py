# ------------------------------------------
# CECS 378 Lab 1
# Name: Lennox Scott
# I.D. #: 017071819
# Start Date: 09-02-2020
# End Date: 10-12-2020
# Symmetric Cryptography
# ------------------------------------------

# Shift Cipher


# This is the cipher that takes in the plaintext and shifts its letters backward by the amount given in the key
def encrypt(plaintext, key):
    encrypted = ""  # empty string to add the encrypted letters
    for i in plaintext:  # iterates through the plaintext string
        if i.isupper():  # checks if uppercase
            encrypted += chr((ord(i)+key-ord('A')) % 26+ord('A'))  # using modulus operator to encrypt the lowercase letter
        elif i.islower():  # checks if lowercase
            encrypted += chr((ord(i)+key-ord('a')) % 26+ord('a'))  # using modulus operator to encrypt the lowercase letter
    return encrypted  # returns the encrypted string


# This is the cipher that takes in the cipher and shifts its letters forward by the amount given in the key
def decrypt(cipher, key):
    decrypted = ""  # empty string to add the decrypted letters
    for i in cipher:  # iterates through the plaintext string
        if i == ' ':
            decrypted += " "
        if i.islower():
            decrypted += chr((ord(i)-key-ord('a')) % 26+ord('a'))
        if i.isupper():
            decrypted += chr((ord(i)-key-ord('A')) % 26+ord('A'))
    return decrypted  # returns the decrypted string


# Transposition Cipher

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

key2 = "fciebagdkrnhjoltqmupywxvsz"
key3 = "cywsvxefibuzlakdjnqmhogrtp"
key4 = "hogrdjqmxsvuzlfetpcywaknib"

def encryptTrans(plaintext, key):
    encrypted = ""  # empty string to add the encrypted letters
    for i in plaintext:
        if i.isalpha():
            if i.islower():
                encrypted += key[alphabets.index(i)]
            elif i.isupper():
                encrypted += key[alphabets.index(i) % 26].upper()
        else:
            encrypted += i

    return encrypted


def decryptTrans(cipherText, key):
    decrypted = ""  # empty string to add the decrypted letters
    for i in cipherText:
        if i.isalpha():
            if i.islower():
                decrypted += alphabets[(key.index(str(i))) % 26]
            elif i.isupper():
                decrypted += alphabets[(key.index(str(i.lower()))) % 26].upper()
        else:
            decrypted += i
    return decrypted


text = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"
text2 = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy"
text3 = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"
text4 = "iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"
# Part two texts
text5 = "He who fights with monsters should look to it that he himself does not become a monster . And if you gaze long into an abyss , the abyss also gazes into you ."
text6 = "There is a theory which states that if ever anybody discovers exactly what the Universe is for and why it is here , it will"
text7 = "Whenever I find myself growing grim about the mouth ; whenever it is a damp , drizzly November in my soul ; whenever I find myself involuntarily pausing before coffin warehouses , and bringing up the rear of every funeral I meet ; and especially whenever my hypos get such an upper hand of me , that it requires a strong moral principle to prevent me from deliberately stepping into the street , and methodically knocking people ’ s hats off - then , I account it high time to get to sea as soon as I can ."


# answer is test case #9
print("****************** FIRST MESSAGE ******************")
for trial in range(26):
    print("Brute force test case #" + str(trial) + " :" + decrypt(text, trial))

# answer is test case #21
print("\n\n\n****************** SECOND MESSAGE ******************")
for trial in range(26):
    print("Brute force test case #" + str(trial) + " :" + decrypt(text2, trial))

# answer is test case #
print("\n\n\n****************** THIRD MESSAGE ******************")
for trial in range(26):
    print("Brute force test case #" + str(trial) + " :" + decrypt(text3, trial))

print("\n\n\n****************** FOURTH MESSAGE ******************")
for trial in range(26):
    print("Brute force test case #" + str(trial) + " :" + decrypt(text4, trial))


print("****************************** Part Two ******************************\n\n")
print("\n\n\n****************** FIRST MESSAGE ******************")
print("The current string to be encrypted: " + text5)
eText5 = encryptTrans(text5, key2) # key = "fciebagdkrnhjoltqmupywxvsz"
print("The string after encryption: " + eText5)
deText5 = decryptTrans(eText5, key2)
print("The string after decryption: " + deText5)


print("\n\n\n****************** SECOND MESSAGE ******************")
print("The current string to be encrypted: " + text6)
eText6 = encryptTrans(text6, key3) # key = "cywsvxefibuzlakdjnqmhogrtp"
print("The string after encryption: " + eText6)
deText6 = decryptTrans(eText6, key3)
print("The string after decryption: " + deText6)

print("\n\n\n****************** THIRD MESSAGE ******************")
print("The current string to be encrypted: " + text7)
eText7 = encryptTrans(text7, key4) # key = "hogrdjqmxsvuzlfetpcywaknib"
print("The string after encryption: " + eText7)
deText7 = decryptTrans(eText7, key4)
print("The string after decryption: " + deText7)
