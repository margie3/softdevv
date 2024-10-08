import random

# Moyo Fagbuyi, Margie Cao, Tim Ng
# Systems Level Programming
# SoftDev
# K04 -- Python dictionairies and random selection
# 2024-09-13
# time spent: 0.6

krewes = {
           4: [
        'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
        'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
        'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
        'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
        ],
           5: [ 
        'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
        'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
        'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
        'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }

def pop():
    keys = list(krewes.keys())
    #converts keys into a list
    keysLen = len(keys)
    x = random.randint(0, keysLen - 1)
    #takes a random index for the number of keys
    vals = list(krewes.get(keys[x]))
    #converts values of random key into a list
    valsLen = len(vals)
    y = random.randint(0, valsLen - 1)
    #takes a random index for the number of values
    print(vals[y])
  
pop()
    