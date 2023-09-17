"""EX02 - One Shot Wordle."""
__author__ = "730679279"

secret_word: str = "python"
guess_word: str = input("What is your 6-letter guess?")

while len(guess_word) != 6:
    guess_word = input("That was not 6 letters! Try again:")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index_tracker: int = 0
result: str = ""

while index_tracker < 6:
    if guess_word[index_tracker] == secret_word[index_tracker]:
        result = result + GREEN_BOX
    else:
        exist_tracker: bool = False
        alternate_index: int = 0

        while exist_tracker is False and alternate_index < 6:
            if guess_word[index_tracker] == secret_word[alternate_index]:
                exist_tracker = True
            else:
                alternate_index = alternate_index + 1
        
        if exist_tracker is True:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
    
    index_tracker = index_tracker + 1

if guess_word == secret_word:
    print(f"{result}\n Woo! You got it!")
else:
    print(f"{result}\n Not quite. Play again soon!")