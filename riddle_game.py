def info():
    """Define user inputs.

    :rtype: str
    :return: correct inputs as sting
    """
    our_info = ["too small", "too big", "you won"]
    while True:
        answear = input().lower()
        if answear in our_info:
            break
        print("Incorrect information")
    return answear

def game():
    """Main function"""
    number = input("Choose number between 1 and 1000: ")
    answear = ""
    minnum = 0
    maxnum = 1000
    while answear != "you won":
        computer = (maxnum - minnum) //2 + minnum
        print(f"I guess that is: {computer}")
        answear = info()
        if answear == "too big":
            maxnum = computer
        elif answear == "too small":
            minnum = computer
    print("Hurra, i guessed!")

if __name__ == '__main__':
    game()
