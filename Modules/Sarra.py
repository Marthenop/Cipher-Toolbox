from Modules import ClrTrm

def begin():

    Begining2 = input("Would you like to Encrypt or Decrypt?\n\n")
    ClrTrm.clear()

    if Begining2 == ("Encrypt"):
        message = input("Enter message to be encrypted.\n\n")
        dictionary = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', '1': 'A', '3': 'C', '4': 'D', '5': 'E','6': 'F', '7': 'G', '8': 'H', '9': 'I'}
        transtable = message.maketrans(dictionary)
        message = message.encode('utf-8').hex().translate(transtable).replace('20', 'T ').replace('0', 'nil').replace('2', 'B')
        message2 = ' '.join(message[i:i+2] for i in range(0, len(message), 2)).replace('  ', ' ').replace('n ', 'n')
        print("\n"+message2)
        input("")
        ClrTrm.clear()

    if Begining2 == ("Decrypt"):
        message = input("Enter message to be decrypted.\n\n")
        dictionary = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'I': '9', 'T': '20', '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e','6': 'f', '7': 'g', '8': 'h', '9': 'i'}
        transtable = message.maketrans(dictionary)
        message = message.translate(transtable).replace('nil', '0').replace(' ', '')
        message2 = bytes.fromhex(message).decode('utf-8')
        print("\n"+message2)
        input("")
        ClrTrm.clear()
