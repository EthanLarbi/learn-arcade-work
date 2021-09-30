import random



def main(the_natives_traveled=None):
    print("welcome the Cheetah Race")
    print("You have stolen a cheetah to make your way across the great Sahara Desert")
    print("The natives want their Cheetah back and are chasing you down! Survive your desert trek and outrun the natives.")

    done = False
    miles_traveled = 0
    thirst = 0
    cheetah_tiredness = 0
    native_distance = -20
    drinks = 3
    player_pos = 0
    loser = True
    enemies = 0


    while not done:
        print("A. Drink from your Canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status Check")
        print("Q. Quit")

        user_choice = input("enter your choice: ")
        if user_choice.upper() == "Q":
            print("catch you later")
            done = True

        elif user_choice.upper() == "A":
            # take a drink
            if drinks > 0:
                thirst = 0
                print("this water was indeed helpful")
                drinks = drinks - 1
            else:
                print(" you are out of water!")


        elif user_choice.upper() == "B":
            # move at moderate speed
            miles_traveled = miles_traveled + random.randrange(5, 10)
            thirst = thirst + 1
            cheetah_tiredness = cheetah_tiredness + 1
            native_distance = native_distance + random.randrange(7, 15)
            print("\nyou are now", miles_traveled - native_distance, "miles ahead of the natives")
            print("your thirst is now at ", thirst)

        elif user_choice.upper() == "E":
            # Drink from Canteen
            print("\nmiles traveled: ", "miles_traveled")
            print("Drink in canteen: 3")
            print("the natives are ", miles_traveled - native_distance, "miles behind you. ")
            print("your cheetah tiredness is ", cheetah_tiredness)


        elif user_choice.upper() == "C":
            miles_traveled = miles_traveled + random.randrange(10,18)
            thirst = thirst + 1
            cheetah_tiredness = cheetah_tiredness + random.randrange(1,4)
            native_distance = native_distance + random.randrange(7, 15)
            print("you are now", miles_traveled - native_distance, "miles ahead of the natives")
            #print("your thirst is now at ", thirst)


        elif user_choice.upper() == "D":
            print("you stop for the night")
            print("your cheetah is happy")
            print("The natives don't stop, and are off your trail. ")
            print()
            cheetah_tiredness = 0
            native_distance = native_distance + random.randrange(7, 15)
            print("Drink in Canteen: ", drinks)
            print("the natives are", miles_traveled - native_distance, "miles behind you")

        if cheetah_tiredness >= 8:
            print("\n your cheetah is dead!")
            done = True

        if cheetah_tiredness >= 5 and done == False:
            print("\nYour cheetah is getting tired.")


        if thirst > 6:
            print("\nyou have died of thirst")
            done = True

        if thirst > 3 and done == False:
            print("\nYou are Thirsty!")

        if miles_traveled >= 200:
            print("\nyou have outrun the natives, your and your cheetah are free!")
            done = True

        enemies = miles_traveled - native_distance

        if enemies <= 0:
            print("the enemies captured you! you lose!")
            done = True

        if enemies <= 15:
            print("The enemies are getting closer!")


main()





