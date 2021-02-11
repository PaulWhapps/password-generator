import random
import string

def numpass():# Generates random numbers.
    random_num = random.sample(range(0,9), 6)
    return list(map(str, random_num))

def letterpass():# Genrates random uppercase and lowercase letters.
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for i in range(7))
    return list(random_string)

def symbol():# Selects random symbol from symbols list.
    symbols = ['!','@','#','%','&','*','(',')']
    random_symbol = random.choice(symbols)
    return list(random_symbol)

def final_password():# Combines and randomises each function into a single string.
    li = (numpass()+letterpass()+symbol())
    random.shuffle(li)
    final_string = ''.join(str(i) for i in li)
    return final_string

print(final_password())
