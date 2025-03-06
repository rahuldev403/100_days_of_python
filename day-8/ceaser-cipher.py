letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

logo = '''
   ____                       _       _           
  / ___|__ _  ___  ___  __ _| |_ ___| |__   ___ 
 | |   / _` |/ _ \/ __|/ _` | __/ __| '_ \ / _ \\
 | |__| (_| |  __/\__ \ (_| | || (__| | | |  __/
  \____\__,_|\___||___/\__,_|\__\___|_| |_|\___|
                                                
     C A E S A R   C I P H E R
'''

print(logo)

def encrypt(message, shift):
    final_output = ""
    for letter in message:
        if letter in letters:
            index = (letters.index(letter) + shift) % 26
            final_output += letters[index]
        else:
            final_output += letter
    return final_output

def decrypt(message, shift):
    final_output = ""
    for letter in message:
        if letter in letters:
            index = (letters.index(letter) - shift) % 26
            final_output += letters[index]
        else:
            final_output += letter
    return final_output

def cipher():
    while True:
        direction = input("Type 'encrypt' to encrypt, 'decrypt' to decrypt the code:\n").lower()
        if direction not in ["encrypt", "decrypt"]:
            print("Invalid option! Please choose 'encrypt' or 'decrypt'.")
            continue
        
        text = input("Type your message:\n").lower()
        
        try:
            shift = int(input("Type the shift number (1 to 26):\n"))
            if shift < 1 or shift > 26:
                print("Shift must be between 1 and 26.")
                continue
        except ValueError:
            print("Please enter a valid number for shift.")
            continue

        if direction == "encrypt":
            result = encrypt(text, shift)
        else:
            result = decrypt(text, shift)

        print(f"Result: {result}")

        user = input("Do you want to continue? (Y/N): ").lower()
        if user != "y":
            print("Goodbye!")
            break

cipher()
