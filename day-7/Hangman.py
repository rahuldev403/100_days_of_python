import random

hangmanStages = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========

""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========

""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========

""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========

""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

""",
]

logo = '''
  _                                             
 | |                                            
 | |__   __ _ _ __ ___   __ _ _ __ _   _ ___    
 | '_ \ / _` | '_ ` _ \ / _` | '__| | | / __|   
 | | | | (_| | | | | | | (_| | |  | |_| \__ \   
 |_| |_|\__,_|_| |_| |_|\__,_|_|   \__,_|___/   
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

'''

print(logo)
arr = ["camel", "tiger", "jackal"]  
animal = random.choice(arr)
hidden_word = "_" * len(animal)  
print("You have to guess this animal name:")
print(hidden_word)

correct_letters = []
num = 6
i = 0
space = hidden_word  

while space != animal:
    if num == 0 or i > 5:
        print("****** You lose :( ******")
        break

    guess = input("Guess a letter: ").lower()

    if guess in animal:
        space1 = ""
        for letter in animal:
            if letter == guess:
                space1 += letter
                correct_letters.append(letter)
            elif letter in correct_letters:
                space1 += letter
            else:
                space1 += "_"
        print(space1)
        space = space1
    else:
        num -= 1
        print(f"*******-: Wrong {num}/6 lives left :-*******")
        print(hangmanStages[i])
        i += 1

    if space == animal:
        print("*******-: You won! :-*******")
