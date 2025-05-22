def user_turn(current_number):
    while True:
        try:
            nums = input(f"Your turn! Enter 1 to 3 numbers after {current_number}: ").strip().split()
            nums = [int(n) for n in nums]
            if not 1 <= len(nums) <= 3:
                print("You must enter between 1 and 3 numbers.")
                continue
            if nums[0] != current_number + 1 or any(nums[i] != nums[i-1] + 1 for i in range(1, len(nums))):
                print("Numbers must be consecutive and start from the next number.")
                continue
            return nums[-1]
        except ValueError:
            print("Please enter valid integers.")

def computer_turn(current_number):
    # Strategy: always end on a multiple of 4
    next_number = current_number
    count = 0
    while (next_number - current_number) < 3 and (next_number + 1) % 4 != 0:
        next_number += 1
        count += 1
    if count == 0:
        count = 1
        next_number = current_number + 1
    nums = list(range(current_number + 1, current_number + count + 1))
    print(f"Computer's turn: {' '.join(map(str, nums))}")
    return nums[-1]

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
