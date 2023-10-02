from Modules import ClrTrm
import re
def begin():
    Begining = input("Do you want to Encrypt or Decrypt?\n\n")
    ClrTrm.clear()
    if Begining == ("Encrypt"):
        message = input("Enter the text you want to encrypt:\n\n")
        dictionary = {'a': '11', 'b': '21', 'c': '31', 'd': '12', 'e': '22', 'f': '32', 'g': '13', 'h': '23', 'i': '33', 'j': '14', 'k': '24', 'l': '34', 'm': '15', 'n': '25', 'o': '35', 'p': '16', 'q': '26', 'r': '36', 's': '17', 't': '27', 'u': '37', 'v': '18', 'w': '28', 'x': '38', 'y': '19', 'z': '29', '1': '01', '2': '02', '3': '03', '4': '04', '5': '05', '6': '06', '7': '07', '8': '08', '9': '09', '0': '00', ' ': '**'}
        transtable = message.maketrans(dictionary)
        print("\n"+message.lower().translate(transtable))
        input()
        ClrTrm.clear()

    if Begining == ("Decrypt"):
        message = input('Enter the text you want to decrypt:\n\n')
        dictionary = {'11': 'a', '21': 'b', '31': 'c', '12': 'd', '22': 'e', '32': 'f', '13': 'g', '23': 'h', '33': 'i', '14': 'j', '24': 'k', '34': 'l', '15': 'm', '25': 'n', '35': 'o', '16': 'p', '26': 'q', '36': 'r', '17': 's', '27': 't', '37': 'u', '18': 'v', '28': 'w', '38': 'x', '19': 'y', '29': 'z', '01': '1', '02': '2', '03': '3', '04': '4', '05': '5', '06': '6', '07': '7', '08': '8', '09': '9', '00': '0', '**': ' '}
        message = re.findall('..', message)
        for char in message:
            message.append(dictionary.get(message[0]))
            message.remove(message[0])
        print("\n"+''.join(message))
        input()
        ClrTrm.clear()
        
