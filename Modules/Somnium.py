from Modules import ClrTrm

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
        ClrTrm.clear()
        message = input("Enter the text you want to decrypt:\n\n")
        dictionary = {'26': 'a', '2b': 'b', '36': 'c', '3b': 'd', '17': 'e', '4a': 'f', '27': 'g', '3a': 'h', '37': 'i', '2a': 'j', '47': 'k', '1a': 'l', '57': 'm', '0a': 'n', '08': 'o', '59': 'p', '18': 'q', '49': 'r', '28': 's', '39': 't', '38': 'u', '29': 'v', '48': 'w', '19': 'x', '58': 'y', '09': 'z', '06': '1', '56': '2', '0b': '3', '5b': '4', '4b': '5', '46': '7', '16': '8', '07': '9', '5a': '0', '+': ' '}
        message = [message[i:i+2] for i in range(0, len(message), 2)]
        for char in message:
            message.append(dictionary.get(message[0]))
            message.remove(message[0])
        print("\n"+str(message).replace("[","").replace("\'","").replace(",","").replace("]","").replace(" ",""))
        input()
        ClrTrm.clear()
