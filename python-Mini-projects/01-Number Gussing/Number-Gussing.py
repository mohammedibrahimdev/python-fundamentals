import random

print("=========================================")
print("      Welcome to Number Guessing Game    ")
print("=========================================")

choose = input("Wanna play game {Y : N} : ")

games_play = 0
games_win = 0
games_lost = 0
best_score = None

if choose == 'Y' or choose == 'y':

    while True:

        games_play += 1

        print()
        print("Choose difficulty:")
        print()
        print("   1. Easy")
        print("   2. Medium")
        print("   3. Hard")
        print()

        difficulty = int(input("Enter choice : "))

        if difficulty == 1:
            maximum = 20
            attempts_left = 10
        elif difficulty == 2:
            maximum = 50
            attempts_left = 6
        elif difficulty == 3:
            maximum = 100
            attempts_left = 3
        else:
            print("Invalid choice")
            games_play -= 1
            continue

        secret_number = random.randint(1, maximum)

        attempts_used = 0
        win = False

        print()
        print(f"Guess a number between 1 and {maximum}")
        print(f"You have {attempts_left} attempts")

        while attempts_left > 0:

            guess = int(input("Guess the number : "))

            attempts_used += 1
            attempts_left -= 1

            if guess == secret_number:
                win = True
                games_win += 1

                print()
                print("Congratulations!")
                print(f"You guessed the number in {attempts_used} attempts")

                # Best score
                if best_score is None or attempts_used < best_score:
                    best_score = attempts_used

                break

            elif guess < secret_number:
                print("Too low")

            else:
                print("Too high")

            if attempts_left > 0:
                print(f"Attempts left : {attempts_left}")

        if not win:
            games_lost += 1
            print()
            print("You couldn't guess the number.")
            print(f"The number was : {secret_number}")

        print()
        choose = input("Wanna play again {Y : N} : ")

        if choose == 'N' or choose == 'n':
            break

    # Game Summary
    print()
    print("=========================================")
    print("             GAME SUMMARY")
    print("=========================================")

    print(f"Games Played : {games_play}")
    print(f"Games Won    : {games_win}")
    print(f"Games Lost   : {games_lost}")

    if best_score is not None:
        print(f"Best Score   : {best_score} attempts")
    else:
        print("Best Score   : No wins")

    win_rate = (games_win / games_play) * 100
    print(f"Win Rate     : {win_rate:.2f}%")

    print("=========================================")
    print("          Thanks for playing!")
    print("=========================================")

else:
    print("No problem")