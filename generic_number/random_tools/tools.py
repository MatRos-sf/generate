from random import choice, randint, choices, sample, shuffle
from textwrap import wrap
import string
def random_number(a,b,amount=1):
    #if number b> a. A must be always lower
    a,b = sorted([a,b])

    rand_arr = []
    for i in range(amount):
        rand_arr.append(randint(a,b))
    return rand_arr


def heads_or_tails():
    return choice(['Heads', 'Tails'])

def throw_a_dice():
    return randint(1,6)

def draw_list(arr, amount=1,repeat=False):
    if repeat:
        return choices(arr, k=amount)
    else:
        if amount < len(arr):

            return sample(arr, k=amount)
        else:
            print('here')
            shuffle(arr)
            return arr

def generic_password(name,year, prefix):
    name = name.lower()
    if name:
        if 'a' in name:     name = name.replace('a', '@')
        if 'b' in name:     name = name.replace('b', '&')
        if 'e' in name:     name = name.replace('e', '3')
        if 's' in name:     name = name.replace('s','$')
    else:
        name = ''.join(chr(randint(33,126)) for i in range(4))

    if year:
        year = str(year)
        year = wrap(year,2)
        year = str(choice(year))
    else:
        year = ''.join(chr(randint(48,57)) for i in range(2))

    if prefix:
        prefix = prefix.upper()
    else:
        prefix = ''.join(chr(randint(33,47)) for i in range(2))
    add_letter = chr(randint(33,126))
    new_password = [name,year,prefix,add_letter]
    #mieszanie
    shuffle(new_password)

    return ''.join(new_password)


