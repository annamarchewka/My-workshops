import random

def get_number():
    """Get number from user and check the value.
    Try until the value would be correct.

    :rtype: int
    :return: value as int
    """
    while True:
        try:
            given_number = input("CHOOSE NUMBER: ")
            given_number_int = int(given_number)
            break
        except ValueError:
            print("INCORRECT VALUE")

    return given_number_int

def six_numbers():
    """Get six numbers from user.

    :rtype: list
    :return: list with 6 numbers
    """
    given_six = []
    while len(given_six) < 6:
        number = get_number()
        if number not in given_six and number > 0 and number <= 49:
            given_six.append(number)
    return given_six

def luckyLOTTO_numbers():
    """Select and print lotto table.

    :rtype: list
    :return: list with 6 random numbers
    """
    our_range = list(range(1, 49))
    random.shuffle(our_range)
    lucky_numbers = our_range[:6]
    return lucky_numbers

def lotto_games():
    """Print given and lotto tables.
    Main function of LOTTO game.
    """
    sorted_table = sorted(six_numbers())
    lotto_table = luckyLOTTO_numbers()
    print(f"YOURS NUMBERS: {sorted_table}"), print(f"LOTTO NUMBERS: {lotto_table}")

    guessed = 0
    for number in sorted_table:
        if number in lotto_table:
            guessed +=1
    print(f"You have guessed: {guessed} numbers!")

    if guessed > 2:
        print(f"You won!")
    else:
        print(f"You failed!")

if __name__ == '__main__':
    lotto_games()
