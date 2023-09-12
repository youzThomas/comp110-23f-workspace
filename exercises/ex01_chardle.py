"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730679279"

word: str = input("Enter a 5-character word:")
character: str = input("Enter a single character:")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

count: int = 0
print("Searching for "+character+" in "+word)

if character == word[0]:
    print(character+" found at index 0")
    count+=1

if character == word[1]:
    print(character+" found at index 1")
    count+=1

if character == word[2]:
    print(character+" found at index 2")
    count+=1

if character == word[3]:
    print(character+" found at index 3")
    count+=1

if character == word[4]:
    print(character+" found at index 4")
    count+=1

print(count+" instance of "+character+" found in "+word)