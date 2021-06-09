import random
import string

answers = "python", "java", "kotlin", "javascript"
correct_letters = set()
incorrect_letters = set()

print("H A N G M A N")
answer = random.choice(answers)


def show_question():
    global answer
    global correct_letters
    for x in answer:
        if x in correct_letters:
            print(x, end="")
        else:
            print("-", end="")
    else:
        print()


def is_win():
    global answer
    global correct_letters
    return correct_letters == set(answer)

def setup_game():
    global answer
    global correct_letters
    global incorrect_letters
    answer = random.choice(answers)
    correct_letters.clear()
    incorrect_letters.clear()


while True:
    print('Type "play" to play the game, "exit" to quit: ', end="")
    choice = input()
    if choice == "play":
        setup_game()
        i = 0
        while True:
            print()
            show_question()
            print("Input a letter: ", end="")
            letter = input()
            if len(letter) != 1:
                print("You should input a single letter")
            elif letter not in string.ascii_lowercase:
                print("Please enter a lowercase English letter")
            elif letter in correct_letters or letter in incorrect_letters:
                print("You've already guessed this letter")
            elif letter in answer:
                correct_letters.add(letter)
            else:
                print("That letter doesn't appear in the word")
                incorrect_letters.add(letter)
                i = i + 1
            if is_win():
                show_question()
                print("You guessed the word!")
                print("You survived!")
                break
            if i == 8:
                break

        if not is_win():
            print("You lost!")
    elif choice == "exit":
        break
