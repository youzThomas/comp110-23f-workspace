"""EX03 - Structured Wordle."""
__author__ = "730679279"

def contains_char(wordToCheck: str, letter: str) -> bool:
    assert len(letter) == 1
    index_tracker: int = 0

    while index_tracker < len(wordToCheck):
        if wordToCheck[index_tracker] == letter:
            return True
        else:
            index_tracker = index_tracker + 1
    return False
"""Fucntion that check whether the letter is included in the word."""

def emojified(guess: str, secret_word: str) -> str:
    assert len(guess) == len(secret_word)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    
    index_mark: int = 0
    result: str = ""

    while index_mark < len(secret_word):
        if guess[index_mark] == secret_word[index_mark]:
            result = result + GREEN_BOX
        else:
            if contains_char(secret_word, guess[index_mark]) == True:
                result = result + YELLOW_BOX
            else:
                result = result + WHITE_BOX
    
        index_mark = index_mark + 1

    return result

def input_guess(length: int) -> str:
    received_word: str = input("Enter a "+str(length)+" character word:")

    while len(received_word) != length:
        received_word = input("That wasn't "+str(length)+" chars! Try again:")

    return received_word

def main() -> None:
    Try_times: int = 1
    enter_word: str = ""

    while Try_times < 6:
        print("=== Turn "+str(Try_times)+"/6 ===")
        enter_word = input_guess(len("codes"))
        print(emojified(enter_word, "codes"))
        if enter_word == "codes":
            print("You won in "+str(Try_times)+"/6 turns!")
            return
        else:
            Try_times = Try_times + 1
    
    print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()





 
 

