#8 ball program
#200802

import random
import time

#All possible 8-Ball answers alongside the decision to play agian
options = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definately.", "You may rely on it", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Dont count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
yesorno = ["Y","N"]

print("")
print ("Behold. The 8 Ball.")
print ("")

def question():
     print("")
     print ("Ask a question to reveal your future.")
     input()
     print ("")
     print ("Processing...")
     time.sleep (3)
     print ("")
     print (random.choice(options))
     askagain()
     
def askagain():
     print ("")
     playagain = ""
     playagain = input ("Do you have another question? If yes, press Y. If no , press N.")
     if playagain == "Y" or playagain == "y":
          question()
     elif playagain == "N" or playagain == "n":
          print ("")
          print ("Thank you for playing")
          exit()
     else: 
          print ("")
          print ("I did not understand. Please repeat.")


question()
askagain()
