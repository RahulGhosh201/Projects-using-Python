name = input("Type your name: ")
print("Welcome ",name," to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go to left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You came to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross:  ").lower()

    if answer == 'swim':
        print('You swam across th river and were eaten by an alligator and you lost the game.')
    elif answer == 'walk':
        print('You walked for many miles, ran out of water and you lost the game.')
    else:
        print("Not a valid option, You lose.")

elif answer == "right":
    answer=input('You come to a bridge, it looks woobly, do you want to cross it or head back (cross/back)? ').lower()

    if answer == 'cross':
        answer = input('You cross the bridge and meet a stranger. Do you talk to them (yes/No)? ').lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold and you WIN!!")
        elif answer == "no":
            print("You ignored the stranger and they are offended and you lose.")
        else:
            print("Not a valid option, You lose.")

    elif answer == 'back':
        print('You go back and lose.')
    else:
        print("Not a valid option, You lose.")

else:
    print('Not a valid option, You lose.')