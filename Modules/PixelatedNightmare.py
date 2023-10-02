from Modules import ClrTrm
import re
def begin():
    Begining = input("Do you want to Encrypt or Decrypt?\n\n")
    ClrTrm.clear()
    if Begining == ("Encrypt"):
        message = input("Enter the text you want to encrypt:\n\n")
        dictionary = {'a': 'r', 'b': 'd', 'c': 'i', 'd': 'k', 'e': 'n', 'f': 's', 'g': 'a', 'h': 'q', 'i': 'e', 'j': 'v', 'k': 'l', 'l': 'f', 'm': 'o', 'n': 'c', 'o': 'm', 'p': 'y', 'q': 't', 'r': 'p', 's': 'w', 't': 'h', 'u': 'g', 'v': 'u', 'w': 'x', 'x': 'z', 'y': 'b', 'z': 'j'}
        transtable = message.maketrans(dictionary)
        print("\n"+message.lower().translate(transtable))
        input()
        ClrTrm.clear()

    if Begining == ("Decrypt"):
        message = input('Enter the text you want to decrypt:\n\n')
        dictionary = {'r': 'a', 'd': 'b', 'i': 'c', 'k': 'd', 'n': 'e', 's': 'f', 'a': 'g', 'q': 'h', 'e': 'i', 'v': 'j', 'l': 'k', 'f': 'l', 'o': 'm', 'c': 'n', 'm': 'o', 'y': 'p', 't': 'q', 'p': 'r', 'w': 's', 'h': 't', 'g': 'u', 'u': 'v', 'x': 'w', 'z': 'x', 'b': 'y', 'j': 'z'}
        message = re.findall('.', message)
        for char in message:
            message.append(dictionary.get(message[0]))
            message.remove(message[0])
        print("\n"+str(message).replace("[","").replace("\'","").replace(",","").replace("]","").replace(" ",""))
        input()
        ClrTrm.clear()
        
