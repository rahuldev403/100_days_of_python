from art import auction_logo

print(auction_logo)
dic_1 = {}
def max_bid(dictionary):
    max_b = 0
    winner = ""
    for bidded in dictionary:
        current_cash = dictionary[bidded]
        if current_cash > max_b:
            max_b = current_cash
            winner = bidded
    print(f"max :{max_b} ,Winner : {winner}") 
while True:
    name = input("tell your name:")
    price = int(input("Your bid price:"))
    dic_1[name] = price
    ask = input("If there is other users print(Y/N):").lower()
    if ask == "y":
        print("\n" * 100)
    elif ask == "n":
        max_bid(dic_1)
        break
       
"""
i can also use max(name_of_the_dictionary,dictionary.get)

this will help me get the max integer value
"""


