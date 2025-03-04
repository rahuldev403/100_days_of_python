import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

Scissors = '''
    _______
---'   ____)____
          ______) ✂  
       __________)
      (____)
---.__(___)

'''

compute_choice = random.randint(1,3)
print("print \"1\" for rock \"2\" for paper \"3\" for scissors:")
user_choice = int(input())


if(user_choice == compute_choice):
  print("draw")
elif(user_choice==1):
  if(compute_choice == 2):
      print("Compute choice:")
      print(paper)
      print("Your choice:")
      print(rock)
      print("You loose")
  elif(compute_choice == 3):
      print("Compute choice:")
      print(Scissors)
      print("Your choice:")      
      print(rock)
      print("You Won")
elif(user_choice==2):
  if(compute_choice == 1):
      print("Compute choice:")
      print(rock)
      print("Your choice:")
      print(paper)
      print("You Won")
  elif(compute_choice == 3):
      print("Compute choice:")
      print(Scissors)
      print("Your choice:")
      print(paper)
      print("You loose")      
elif(user_choice==3):
  if(compute_choice == 1):
      print("Compute choice:")
      print(rock)
      print("Your choice:")
      print(Scissors)
      print("You losse")
  elif(compute_choice == 2):
      print("Compute choice:")
      print(paper)
      print("Your choice:")
      print(Scissors)
      print("You Won")           
else:
   print("Invalid input")