answer1 = input("You wake up. Where will you go today, the mall or the zoo?: ")
if answer1 == "mall" or answer1 == "the mall":
    answer2 = input("Are you going to buy anything?: ")
    if answer2 == "yes":
        answer3 = input("What are you going to buy?: ")
        print(f"You get some cool {answer3} and head home.")
    elif answer2 == "no":
        print("You go home without buying anything.")
    else:
        print("Please restart and answer yes or no.")
if answer1 == "zoo" or answer1 == "the zoo":
    answer4 = input("Which animal do you want to see first?: ")
    if answer4 == "lions":
        print("There are a few lions sitting out today. They're so cool!")
    elif answer4 == "giraffes":
        print("Wow, the giraffes are so big and cool!")
    elif answer4 == "sea lions" or answer4 == "otters" or answer4 == "sea turtles":
        print("You go to the aquarium part of the zoo to see them. They're so cute!")
    else:
        print(f"You go visit the {answer4}, and they're so cool!")
    answer5 = input("Do you want to see anymore animals?: ")
    if answer5 == "yes":
        print("You go see a few more cool animals, then head home.")
    elif answer5 == "no":
        print("You head home without visiting any other animals.")
    else:
        print(f"You go see {answer5}, then head home.")
print("")
print("THE END")