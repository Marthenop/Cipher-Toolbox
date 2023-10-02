from Modules import ClrTrm

def begin():
    Begining2 = input("Elder, Younger, or Both? (The last two currently don't exist.)\n\n")
    ClrTrm.clear()

    if Begining2 == ("Elder"):
        message = input("Please enter the runes you want translated.\n\n")
        dictionary = {'ᚠ': 'f', 'ᚢ': 'uh', 'ᚦ': 'th', 'ᚨ': 'ay', 'ᚱ': 'r', 'ᚲ': 'k', 'ᚷ': 'g', 'ᚹ': 'w', 'ᚺ': 'h', 'ᚾ': 'n', 'ᛁ': 'ih', 'ᛃ': 'j', 'ᛇ': 'ï', 'ᛈ': 'p', 'ᛉ': 'z', 'ᛊ': 's', 'ᛏ': 't', 'ᛒ': 'b', 'ᛖ': 'e', 'ᛗ': 'm', 'ᛚ': 'l', 'ᛜ': 'ng', 'ᛟ': 'oh', 'ᛞ': 'd'}
        transtable = message.maketrans(dictionary)
        message = message.translate(transtable).replace('ïk', 'ïke')
        print("\n"+message)
        input("")
        ClrTrm.clear()
