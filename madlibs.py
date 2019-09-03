# Here I used import random, so i can use it when I print my text
import random
# Here I added the color magenta in the output
import sys
sys.stdout.write("\033[0;35m")
print("Mad Libs!")
print("Enter an example of each")
0
#Here I used a for loop to make my code much more organized
adjective = []
i = 0
max_adjectives = 5
while i < max_adjectives:
      reply1 = input("Enter a random adjective: ")
      while len(reply1) < 1:
            print("You got to write something! ")
            reply1= input("Enter a random adjective: ")
      adjective.append(reply1)
      i += 1



verb = []
i = 0
max_verbs = 2
while i < max_verbs:
      reply2 = input("Enter a random verb: ")
      while len(reply2) < 1:
            print("You got to write something! ")
            reply2 = input("Enter a random verb: ")
      verb.append(reply2)
      i += 1

noun = []
i = 0
max_nouns = 4
while i < max_nouns:
      reply3 = input("Enter a random noun: ")
      while len(reply3) < 1:
            print("You got to write something! ")
            reply3 = input("Enter a random noun: ")
      noun.append(reply3)
      i += 1





#  I borrowed this mad lib from https://me.me/i/madolibs-print-our-cafeteria-glamorous-adjective-our-school-cafeteria-has-c4aa33f3592a4a8b910a2e4c89472e01
print("Our school cafeteria has really", random.choice(adjective) , "food. Just thinking about it makes my stomach", random.choice(verb) , ". The spaguetti is", random.choice(adjective) ,"and tastes like", random.choice(noun) ,". One day, I swear one of my meatballs started to", random.choice(verb) , "!The turkey tacos are totally", random.choice(adjective) , "and look kind of like old", random.choice(noun) ,". My friend Dana actually likes the meatloaf, even though it's", random.choice(adjective) , "and", random.choice(adjective) , ".I call it 'mystery meatloaf' and think it's really made out of", random.choice(noun) , ".My dad said he'd make my lunches, but the first day, he made me a sandwich out of", random.choice(noun) , "and peanut butter! I think I'd rather take my chances with the cafeteria!")
