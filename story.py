place = input ("You wake up. Where will you go today? Paris or school?: ")
if place == "Paris":
    print("Yay, Paris has the best food!")
    french = input ("Do you speak French?: ")
    if french == "yes":
        frenchie = input("That's so cool, are you French?: ")
        if frenchie == "yes":
            print("Nice!")
        else:
            print("ok, cool!")
    else: 
        print("Well, you can get around Paris pretty easily with just English.")
if place == "school":
    print("At least you get to see all your friends.")
    firstclass = input 