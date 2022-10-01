import random

def riddle():
    """Get number from user and check the value.
    Try until the value would be correct.

    rtype: int
    return: value as int
    """
    while True:
        try:
            given_number = input("GUESS THE NUMBER: ")
            given_number_int = int(given_number)
            break
        except ValueError:
            print("THAT IS NOT A NUMBER. TRY AGAIN!")

    return given_number_int

def game():
    """Main function"""
    drawn_number = random.randint(1, 100)
    game_number = riddle()
    while game_number != drawn_number:
        if game_number > drawn_number:
            print("TOO MUCH! TRY AGAIN")
        else:
            print("NOT ENOUGH! TRY AGAIN")
        given_number = riddle()
    print(f"CONGRATS, YOU WON!")


if __name__ == '__main__':
    game()
