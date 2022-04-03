# Author - Cat
# Written on Apr 3 2022
# Test your typing speed

import time, datetime, random

messages = [
    "Of all the trees we could've hit, we had to getone that hits back.",
    "If he doesn't stop trying to save your life he's going to kill you.",
    "It is our choices that show what we truly are, far more than our abilities.",
    "I am a wizard, not a baboon brandishing a stick.",
    "Greatness inspires envy, envy engenders spite, spite spawns lies.",
    "In dreams, we enter a word that's entirely our own.",
    "It is my belief that the truth is generally preferable to lies.",
    "Drawn seemed to follow midnight with indecent haste."
    ]
print("Typing speed test. Type the following message. I will time you.")
time.sleep(2)
print("\nReady...")
time.sleep(1)
print("\nSet...")
time.sleep(1)
print ("\nGo:")
message = random.choice(messages)
print ("\n " + message)
start_time = datetime.datetime.now()
typing = input ('>')
end_time = datetime.datetime.now()
diff = end_time - start_time
typing_time = diff.seconds + diff.microseconds / float(1000000)
cps = len (message) / typing_time
wpm = cps * 60 / 5.0
print( "\nYou typed %i characters in %.if seconds." % (len(message),
                              typing_time))
print ("That's %.2f chars per sec, or %.if words per minute" % (cps, wpm))
if typing == message:
    print ("You didn't make any mistake.")
else:
    print ("But, you made at least one mistake.")

    
