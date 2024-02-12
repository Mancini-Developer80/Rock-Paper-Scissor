import random

user_points = 0
computer_points = 0
options = ["rock", "paper", "scissors"]

print("Welcome! Play the game and have fun!")
print("")

while True:
    user_input =input("Type Rock/Paper/Scissors or Q to quit the game ").lower()
    if user_input == "q":
        break
    if user_input not in options :
        print("Write one of the right requeted words ")
        continue

    random_number = random.randint(0, 2)
    computer_choice = options[random_number]
    print(f"Computer picked {computer_choice}!")

    if user_input == "rock" and computer_choice == "scissors":
        print("You won this game!!")
        user_points += 1
        
    elif user_input == "paper" and computer_choice == "rock":
        print("You won this game!!")
        user_points += 1
        

    elif user_input == "scissors" and computer_choice == "paper":
        print("You won this game!!")
        user_points += 1

    elif user_input == computer_choice:
        print(f"You have picked {computer_choice} too")
        print("You choose the same!")
        print("Let's try again!")
        user_points += 0
        computer_points += 0
        
    else:
        print("You lost!!")
        computer_points += 1


    
print(f"You won {user_points} times")
print(f"The computer won {computer_points} times")
print("Goodbye!!")

