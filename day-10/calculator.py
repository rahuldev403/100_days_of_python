from logo import logo
print(logo)
def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a/b

operations = {
    "+": sum,
    "-": sub,
    "*":mul,
    "/":div
}
def cal():
  num1 = float(input("enter your first number:"))
  num2 = float(input("enter your second number:"))
  operation = input("which operation you want to perform: +,-,*,/ :")
  if operation not in operations:
      print("you should choose a good one to make a fun of")
  print(f"{num1}+{num2} = {operations[operation](num1,num2)}")
user = input("do you want to continue (y/n):").lower()
if user == "y":
    cal()
elif user == "n":
    print("Bye Bye")
else:
    print("you should give a valid ans")        

'''
  if operation == "+":
      print(f"{num1}+{num2} = {operations['+'](num1,num2)}")
  elif operation == "-":
      print(f"{num1}-{num2} = {operations['-'](num1,num2)}")
  elif operation == "*":
      print(f"{num1}*{num2} = {operations['*'](num1,num2)}")
  elif operation == "/":
      print(f"{num1}/{num2} = {operations['/'](num1,num2)}")
  '''