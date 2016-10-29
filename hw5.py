#!/usr/bin/env python3
"""
riley_curtis_hw5.py
Asks the user to enter their PIN. If they enter it incorrectly three times the card is blocked.
"""


def main():
    strikes = 0
    while strikes != 3:
        user_input = input("Enter your PIN: ")
        if user_input == "1234":
            print("Your PIN is correct")
            exit(0)
        else:
            if len(user_input) != 4:
                print("Invalid PIN length. Correct format is <9876> ")
                strikes += 1
            elif not user_input.isdigit():
                print("Invalid PIN character(s). Correct format is <9876> ")
                strikes += 1
            else:
                print("Invalid PIN. ")
                strikes += 1
    print("Your card is blocked")
    exit(1)

if __name__ == "__main__":
    main()

exit(0)
