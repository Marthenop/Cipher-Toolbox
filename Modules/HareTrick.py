from Modules import ClrTrm

def begin():

    Cipher = input("Enter the letters now.\n\n")

    Cipher = [Cipher[i:i+2] for i in range(0, len(Cipher), 2)]

    ClrTrm.clear()

    Key = input("Enter the numbers now.\n\n").split("/")

    ClrTrm.clear()

    if Key[0] == '' and Key[-1] == '':
        Key.pop(0)
        Key.pop(-1) #Can't do both pops at once...

    y = 0
    for x in Key:
        Key[y] = int(Key[y])-1
        y=y+1

    Key, Cipher = (list(s) for s in zip(*sorted(zip(Key, Cipher))))#Had to search for this, sorts Cipher via Key.

    Cipher = ''.join(Cipher)

    print(Cipher)
    input()
    ClrTrm.clear()
