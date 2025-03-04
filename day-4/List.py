import random
friends = ["Alice","Bob","Charlie","David","Emanuel"]

num = round(random.randint(0,4))
'print(friends[num]) '

'''
i can use random.choice(list) also
'''

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])