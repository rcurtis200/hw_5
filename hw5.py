#!/usr/var/env python3

import sys

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
