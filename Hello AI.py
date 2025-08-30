# Greet the user
print("Hello! I am AI Bot. Whats our name? : ")

# Get user Input    
name = input()

#Respond to the user' name
print(f"Nice to meet you, {name}!")

# Ask a question 
print("How are you feeling today? (good/bad) : ")
mood = input().lower()

# Use conditional statements to respond based on input
if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. i hope u get well soon")
else:
    print("I see. Sometimes its hard to put feelings into words")

# End the conversation
print(f"It was nice chatting with you {name}. Goodbye!")
