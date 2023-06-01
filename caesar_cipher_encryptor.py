# This is a Caesar Cipher based encryption program written in Python

print("\nCaesar Cipher based Code encryptor\n")

def encrypting(message_input, shift):

    after_encryption = ""

    for each_char in range(len(message_input)):
        character = message_input[each_char]

        # Encrypt based on the shift key for all Upper Case English Alphabet Letter
        # ord() will return each looped characters integer Unicode value
        # The first 2 conditional statements will convert the integer value of the shift formula at that time
        # and convert it into a character value

        if (character.isupper()):
            # Upper Case letters have an ASCII value that starts from 65
            after_encryption += chr((ord(character) + shift - 65) % 26 + 65)

        elif (character.islower()):
            # Lower Case letters have an ASCII value that starts from 97
            after_encryption += chr((ord(character) + shift - 97) % 26 + 97)

        else:
            print("")

    return after_encryption

# Take in user input
message_input = input("Please type your message: ")

# The shift key in this program will be set to 3
shift = 3

print("\nDecryption Alphabet section: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("Encryption Alphabet section: DEFGHIJKLMNOPQRSTUVWXYZABC")

print("\nOriginal Message: " + message_input)
print("\nEncoded Message: " + encrypting(message_input, shift))

