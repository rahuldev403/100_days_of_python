import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [1,2,3,4,5,6,7,8,9,0]

charactes = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
print("number of laters you want:")
n = int(input())
print("number of charactes you want:")  
o = int(input())
print("number of digits you want:")  
m = int(input())
password = ""
for i in range(0,n):
  password += random.choice(letters)
for j in range(0,m):
  password += str(random.choice(numbers))
for j in range(0,o):
  password += random.choice(charactes)
  passwordArr = list(password)  
for i in range(0,len(passwordArr)):
  print(random.choice(passwordArr),end="") #i can use suffle here (random.suffle(passwordArr))