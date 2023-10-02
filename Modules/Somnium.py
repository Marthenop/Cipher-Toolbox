from Modules import ClrTrm
import re


def begin():
    Begining2 = input("Do you want to Encrypt or Decrypt?\n\n")
    if Begining2 == ("Encrypt"):
        ClrTrm.clear()
        message = input("Enter the text you want to encrypt:\n\n")
        dictionary = {'a': '26', 'b': '2b', 'c': '36', 'd': '3b', 'e': '17', 'f': '4a', 'g': '27', 'h': '3a', 'i': '37', 'j': '2a', 'k': '47', 'l': '1a', 'm': '57', 'n': '0a', 'o': '08', 'p': '59', 'q': '18', 'r': '49', 's': '28', 't': '39', 'u': '38', 'v': '29', 'w': '48', 'x': '19', 'y': '58', 'z': '09', '1': '06', '2': '56', '3': '0b', '4': '5b', '5': '4b', '6': '1b', '7': '46', '8': '16', '9': '07', '0': '5a', ' ': '+'}
        transtable = message.maketrans(dictionary)
        message = message.lower().translate(transtable)
        message2 = ''.join((message, '='))
        print("\n"+message2)
        input("")
        ClrTrm.clear()

    if Begining2 == ("Decrypt"):
        clear()
        message = re.findall('.', message)
        for char in message:
            message.append(dictionary.get(message[0]))
            message.remove(message[0])
        print("\n"+str(message).replace("[","").replace("\'","").replace(",","").replace("]","").replace(" ",""))
        input()
        ClrTrm.clear()
