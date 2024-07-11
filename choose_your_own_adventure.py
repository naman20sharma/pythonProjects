name = input("Type your name: ")
print("Welcome", name.capitalize(), "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You can come to a river, you can walk around it or swim across? Type walk to walk around it or swim to swim across: ").lower()
    if answer == 'swim':
        print("You swam across and were eaten by an alligator.")
    elif answer == 'walk':
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You have arrived at a bridge, but it looks wobbly, do you still wish to cross it or head back (cross/back)?").lower()
    if answer == 'back':
        print("You go back and lose. Sorry.")
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them? (Yes/No) ").lower()
        if answer == 'yes':
            print("You talk to the stranger and you receive gold from them. Hurray you WIN!! ")
        elif answer == 'no':
            print("You ignored the stranger and they are offended and you lose. Sorry, but you sometimes you need to trust people.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print("Thank you for trying", name)