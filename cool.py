def play_game():
    print("Welcome to the 21 Number Game!")
    print("Players take turns counting up from 1. On each turn, you can say 1 to 3 consecutive numbers.")
    print("The player who says '21' loses the game.")
    current_number = 0
    while current_number < 21:
        current_number = user_turn(current_number)
        if current_number >= 21:
            print("You said 21. You lose!")
            break
        current_number = computer_turn(current_number)
        if current_number >= 21:
            print("Computer said 21. You win!")
            break

if __name__ == "__main__":
    play_game()
