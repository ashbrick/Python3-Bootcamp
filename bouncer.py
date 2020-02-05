# practicing nested conditional, user input & comparison operators

# ask for age
age = input("How old are you: ") # this will be returned as a string
if age: # if there's an age, then do the following code block
    age = int(age) # turn age into an integer
    if age >= 18 and age < 21: 
        # 18-21 wristband
        print("You can enter, but need a wristband!")
    elif age >= 21:
        # 21+ drink, normal entry
        print("You can enter, and you can drink!")
    else:
        # too young, sorry
        print("You can't come in, little one :(!")
else:
    print("Please enter an age!")
