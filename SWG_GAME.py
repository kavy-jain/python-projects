# snake=1
# water=2
# gun=3

import random

computer=random.choice([1,2,3])
youstr=input("enter your choise :")
youdict={"s":1,"w":2,"g":3}
you=youdict[youstr]
reversedict={1:"snake",2:"water",3:"gun"}

print(f"your choise is {reversedict[you]}\ncomputer choise is {reversedict[computer]}")
if(computer==you):
  print("match tie!!")
else:
  if(computer==1 and you==2):
    print('"you lost"')
  elif(computer==1 and you==3):
    print("you win") 
    
  elif(computer==2 and you==1):
    print("you win") 
  elif(computer==2 and you==3):
    print("you lost") 
  elif(computer==3 and you==1):
    print("you lost") 
  elif(computer==3 and you==2):
    print("you win") 

print("thank you")        