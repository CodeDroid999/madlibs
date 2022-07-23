"""
Madlibs projects by codedroid
"""
#string concatenation aka(how to put strings together in pythons?)
#suppose we want to print a string that says "i love to: "
#few ways to print it:

#programme = "programme"
 
#print("I love to " + programme)
#print("I love to {}".format(programme))
#print(f"I love to {programme}")

from ast import main


adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

welcome = f"welcome to my stupid madlib game.Enter a: "

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
  