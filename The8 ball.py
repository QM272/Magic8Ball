#8 ball or something like that
#200802

import random
import time
options = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definately.", "You may rely on it", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Dont count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]


print ("Behold. THE 8 Ball. (THE8 hee hee)")
print ("")
print ("")

def themainstuff():
     print ("Ask away, amigo.")
     input()
     print ("")
     print ("Processing...")
     time.sleep (3)
     print ("")
     print (random.choice(options))
     print ("")
     print ("There you go.")
     askagain()
     
def askagain():
     print ("")
     print ("Do you have another question? If so... then")
     themainstuff()



themainstuff()
askagain()
