
def reverse_first_half(t: tuple) -> tuple:
    '''
    Given an even-length tuple, return a new tuple where the first half 
    is reversed, and the second half remains unchanged.

    Arguments:
    t: tuple - an even-length tuple.

    Return: tuple - a new tuple with the first half reversed.
    '''
    half_length = len(t) // 2
    first_half = t[:half_length]
    second_half = t[half_length:]
    reversed_first_half = first_half[::-1]  # Reverse the first half
    return reversed_first_half + second_half