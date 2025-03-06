'''
letter = ['T','R','U','E']
letter1 = ['L','O','V','E']
def calculate_love_score(name1,name2):
    count1 = 0
    count2 = 0
    name1 = name1.upper()
    name2 = name2.upper()
    combined_names = name1 + name2
    for word in combined_names:
        if word in letter:
            count1 += 1
        if word in letter1:
            count2 += 1           
    count1 = str(count1)
    count2 = str(count2)
    total_score = count1 + count2
    return total_score 
'''

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
        