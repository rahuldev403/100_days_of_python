'''
def seconds_to_minute_seconds(seconds: int) -> tuple:
    minutes = seconds // 60
    
    second = seconds % 60
    '
    Given an integer representing seconds, return a tuple of (minutes, seconds).

    Arguments:
    seconds: int - an integer representing the number of seconds.

    Return: tuple - a tuple of (minutes, remaining_seconds).
    '
    return (minutes, second)

n = int(input())
print(seconds_to_minute_seconds(n))
'''



'''

def create_indexed_dict(items: list) -> dict:
    '
    Given a list of items, create a dictionary with the indices as keys and the items as items.

    Args:
        items (list): A list of items.

    Returns:
        dict: A dictionary with indices as keys and items as items.
    '
    return {index: item for index, item in enumerate(items)}
    

'''
'''
    def is_even(n):
    if(n%2 == 0):
        return True
    else:
        return False    

    def is_right_triangle_with_even_sides(a:int,b:int,c:int) -> bool:
    if(c**2 == a**2 + b**2  and is_even(a) and is_even(b)):
        return True
    else:
        return False
    Given three side lengths in the increasing 
    order of length as a, b, and c, where a<=b<=c,
    check if the given sides are the sides of a right 
    triangle whose perpendicular sides are of even length.

    Hint: in a right triangle the square of hypotenuse is the sum of square of other two sides.

    Arguments:
    a: int - the first side length
    b: int - the second side length
    c: int - the hypotenuse length

    Return:
    bool - True if the sides form a right triangle and the perpendicular sides are even, else False
    '''
    
    

