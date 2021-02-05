import random
import string

def numpass():
    random_num = random.sample(range(0,9), 6)
    return random_num

def letterpass():
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for i in range(7))
    return random_string

def symbol():
    symbols = ['!','@','#','%','&','*','(',')']
    random_symbol = random.choice(symbols)
    return random_symbol

def final_password():
    li = (numpass())
    li.extend(symbol())
    li.extend(letterpass())
    random.shuffle(li)
    final_string = ''.join(str(i) for i in li)
    return final_string

print(final_password())
