import random
import string

#password generator
class PassGenerator():
    def numpass(self): #generates random numbers
        rand = random.sample(range(0,9),6)
        my_str = ''.join(map(str, rand))
        return my_str
     
    def letterpass(self):#generates random letters, upper and lower case
        length_string = 7
        letters = string.ascii_letters
        random_string = "".join(random.choice(letters) for i in range(length_string))
        return random_string
    
    def symbols(self):#selects a random symbol from the list below
        symbols = ['~','`','!','@','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|','<','>','.','?','/']
        random_symbol = random.choice(symbols)
        return random_symbol
            
    def final_password(self): #prints the result of each function
        print(self.numpass()+self.letterpass()+self.symbols())
        
c = PassGenerator()
c.final_password()
