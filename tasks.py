from math import sqrt
from random import choice,choices

class Covid:
    def __init__(self,temperature):
        self.temperature = temperature
        self.temp = int(self.temperature * 3.14) + 1
    def covid_test(self):
        if  120<=self.temp<=128:
            print("You Have coronavirus")
        else:
            print("Everything is ok")

class NameNumber:
    def __init__(self,name:str) -> None:
        self.dct = {
            ('a', 'j', 's'):1,
            ('b', 'k', 't'):2,
            ('c', 'l', 'u'):3,
            ('d', 'm', 'v'):4,
            ('e', 'n', 'w'):5,
            ('f','o', 'x') :6,
            ('g', 'p', 'y'):7,
            ('h', 'q', 'z'):8,
            ('i', 'r'):9
        }
        self.name = name.lower()

    def number_name(self):
        num = 0
        for i in self.name:
            for j in self.dct:
                if i in j:
                    num += self.dct[j]
        return num
    
    def show_number(self):
        num = self.number_name()
        if sqrt(num)<5:
            print("yes")
        else:
            print("no")
    
class War:
    def __init__(self,word1='Avada Kedavra', word2='Crucio', word3='Imperio'):
        self.word1 = word1
        self.word2 = word2
        self.word3 = word3
        self.lst = ['Avada Kedavra', 'Crucio','Imperio']
    def war(self):
        calc = 0
        lst = []
        for i in range(3):
            wand = choice([self.word1,self.word2,self.word3])
            you = choice(self.lst)
            if wand==you:
                calc += 1
                lst += [wand]
            else:
                calc-=1
        if calc==2:
            print(lst)
            print("You win")
        else:
            print("You lose")

obj = War()
obj.war()