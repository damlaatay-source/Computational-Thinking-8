points = 0
lives = 3
streak = 0

print("Welcome to Trivia.")
print("Please answer the following questions with the capital letter in front of the answers. You have 3 lives.")
input()

#question 1:
question1 = input("How many planets are in the solar system? A.10 ; B.9 ; C.8 ; D.7: ")
if question1 == "C":
    points += 1
    streak += 1
    print(f"CORRECT! You have a streak of {streak}!")
    input()
else:
    lives -= 1
    print(f"INCORRECT! The correct answer was C. 8. You have {lives} lives left.")
    input()

#question 2:
question2 = input("What is the average population of Seattle? A. 200,000 ; B. 500,000 ; C. 800,000 ; D. 700,000: ")
if question2 == "D":
    points += 1
    streak += 1
    print(f"CORRECT! You have a streak of {streak}!")
else:
    lives -= 1
    streak = 0
    print(f"INCORRECT! The correct answer was D. 700,000. You have {lives} live left.")
input()

#question 3:
question3 = input("What is the sixteenth element in the periodic table? A. sulfer ; B. helium ; C. sodium ; D. iron: ")
if question3 == "B" or question3 == "C" or question3 == "D":
    lives -= 1
    streak = 0
    print(f"INCORRECT! The correct answer was A. sulfer. You have {lives} live left.")
    print()
    if lives == 0:
           # if you lose all three lives you lose
            print ("YOU LOSE")
            quit()
    points += 1
    streak += 1
elif question3 == "A":
    points += 1
    streak += 1
    print(f"CORRECT! You have a streak of {streak}!")
input()

#question 4:
question4 = input("What two countries border Bhutan? A. India ; B. Myanmar ; C. Pakistan ; D. China: ")
if "A" in question4 and "D" in question4:
    points += 1
    streak += 1
    print(f"CORRECT! You have a streak of {streak}!")
else:
    lives -= 1
    streak = 0
    print(f"INCORRECT! The correct answer was A. India, D. China. You have {lives} live left.")
if lives == 0:
    print ("YOU LOSE")
    quit()
input()

#question 5
question5 = input("What year was the 6th ammendement of the Constitution (the right to a fair trial) ratified ? A. 1783 ; B. 1791 ; C. 1812 ; D. 1832: ")
if question5 == "B":
    points += 1
    streak += 1
    print(f"CORRECT! You have a streak of {streak}!")
else:
    lives -= 1
    streak = 0
    print(f"INCORRECT! The correct answer was B. 1791. You have {lives} live left.")
input()
if lives == 0:
    print ("YOU LOSE")
    quit()
   
   # if you still have any lives at this point you survived
print(f"You survived! You have {points} points, and a streak of {streak}")
print()
if streak == 5:
    # if you get every single question right you win
    print("YOU WIN! You got every question correct!")