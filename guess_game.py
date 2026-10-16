import random

n= random.randint(1,100)
a=0
guesses=0
while a!=n:
  a=(int(input("Guess the number:")))
  guesses+=1
  if a>n:
    print("Enter lower number:")
  else:
    print("Enter greater number:") 

print(f"you Guessed the number {n} in {guesses} guesses")