from random import choice
from Modules import ClrTrm

def begin():

    Begining2 = input("Would you like to Encrypt or Decrypt?\n\n")
    ClrTrm.clear()
    
    if Begining2 == ("Encrypt"):
        message = input("Input message to be Encrypted:\n\n")
        def is_even(number):
            return number % 2 == 0

        def get_even_letters(message):
            even_letters = []
            for counter in range(0, len(message)):
                if is_even(counter):
                    even_letters.append(message[counter])
            return even_letters
            
        def get_odd_letters(message):
            odd_letters = []
            for counter in range(0, len(message)):
                if not is_even(counter):
                    odd_letters.append(message[counter])
            return odd_letters

        def swap_letters(message):
            letter_list = []
            extra_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '`', '1', '2', '3', '4', '5,' '6', '7', '8', '9', '0', '-', '=', '[', ']', '.', '/', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', ' ']
            if not is_even(len(message)):
                message = message + (choice(extra_letters))
            even_letters = get_even_letters(message)
            odd_letters = get_odd_letters(message)
            for counter in range(0, int(len(message)/2)):
                letter_list.append(odd_letters[counter])
                letter_list.append(even_letters[counter])
            new_message = ''.join(letter_list)
            return new_message

        def encrypt(message):
            swapped_message = encrypt_2(message)
            encrypted_message = ''.join(reversed(swapped_message))
            return encrypted_message

        def encrypt_2(message):
            encrypted_list = []
            fake_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '`', '1', '2', '3', '4', '5,' '6', '7', '8', '9', '0', '-', '=', '[', ']', ',', '.', '/', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', ' ']
            for counter in range(0, len(message)):
                encrypted_list.append(message[counter])
                encrypted_list.append(choice(fake_letters))
            new_message = ''.join(encrypted_list)
            return new_message

        encrypted = encrypt(message)
        print("\n"+encrypted)
        input("")
        ClrTrm.clear()

    if Begining2 == ("Decrypt"):
        message = input("Input message to be Decrypted:\n\n")
            
        def is_even(number):
            return number % 2 == 0

        def get_even_letters(message):
            even_letters = []
            for counter in range(0, len(message)):
                if is_even(counter):
                    even_letters.append(message[counter])
            return even_letters

        def get_odd_letters(message):
            odd_letters = []
            for counter in range(0, len(message)):
                if not is_even(counter):
                    odd_letters.append(message[counter])
            return odd_letters

        def swap_letters(message):
            letter_list = []
            extra_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '`', '1', '2', '3', '4', '5,' '6', '7', '8', '9', '0', '-', '=', '[', ']', ',', '.', '/', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', ' ']
            if not is_even(len(message)):
                message = message + (choice(extra_letters))
            even_letters = get_even_letters(message)
            odd_letters = get_odd_letters(message)
            for counter in range(0, int(len(message)/2)):
                letter_list.append(odd_letters[counter])
                letter_list.append(even_letters[counter])
            new_message = ''.join(letter_list)
            return new_message

        def decrypt(message):
            unreversed_message = ''.join(reversed(message))
            decrypted_message = decrypt_2(unreversed_message)
            return decrypted_message

        def decrypt_2(message):
            even_letters = get_even_letters(message)
            new_message = ''.join(even_letters)
            return new_message

        decrypted = decrypt(message)
        print("\n"+decrypted)
        input("")
        ClrTrm.clear()
