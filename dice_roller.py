import random
dice_faces = [
    """
    ---------
    |       |
    |   O   |
    |       |
    ---------
    """,
    """
    ---------
    | O     |
    |       |
    |     O |
    ---------
    """,
    """
    ---------
    | O     |
    |   O   |
    |     O |
    ---------
    """,
    """
    ---------
    | O   O |
    |       |
    | O   O |
    ---------
    """,
    """
    ---------
    | O   O |
    |   O   |
    | O   O |
    ---------
    """,
    """
    ---------
    | O   O |
    | O   O |
    | O   O |
    ---------
    """
]

stars = [
"*","**","***","****","*****","******"
]

def roll_dice():
    min_number = 1
    max_number = 6
    return random.randint(min_number, max_number)

def main():
    print("Welcome to the Dice Rolling Simulator")

    while True:
        input("Press enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled: {result}")
        print(dice_faces[result - 1])
        print(f"You got: {stars[result - 1]} stars")

        roll_again = input("Roll Again? (yes/no): ").strip().lower()
        if roll_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()