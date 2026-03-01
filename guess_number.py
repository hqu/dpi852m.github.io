#!/usr/bin/env python3

import random


def main() -> None:
    secret = random.randint(1, 1_000_000)
    attempts = 0

    print("Guess the number between 1 and 1,000,000.")

    while True:
        raw = input("Enter your guess: ").strip()

        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if guess < 1 or guess > 1_000_000:
            print("Your guess must be between 1 and 1,000,000.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct! You guessed it in {attempts} tries.")
            break


if __name__ == "__main__":
    main()
