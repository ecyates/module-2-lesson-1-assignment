# Task 1: Code Correction
# Below is a piece of Python code with incorrect indentation. Your task is to correct it.

weather = "sunny"

# If statements require the lines included in the statement to be indented
if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")


# Task 2: Your Mood Today 
# Ask the user how they feel today. If they say "happy", print "That's great to hear!", 
# and if they say "sad", print "I hope your day gets better!". 

# Ask the user how they feel today. 
mood = input("How do you feel today? ")

# If user is happy, say that's great to hear. 
if mood.lower() == "happy": 
    print("That's great to hear!")
# If user is sad, say that I hope the day gets better.
elif mood.lower() == "sad": 
    print("I hope your day gets better!")
# If user says a different mood, say that's interesting.
else: print("That's interesting!") 
#EOF