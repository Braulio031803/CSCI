
import re

# get answer.__doc__
answer_characters = "Dogs"

answer_characters = answer_characters.upper()

# store known or uknown
answer_guesses = []
  
for current_answer_character in answer_characters
 if re.search("^[A-Z]", current_answer_characters:
   answer_guesses.append(False)
 else:
   answer_guesses.append(True)
  
# logic of playing the game.
num_of_incorrect_guesses = 0

while num_of_incorrect_guessess < 5 or False in answer_guesses:
  print("-----------")
  print("Guessed Letters: ", end = "")


 for current_guessed_letter in guessed_letters:
  print(f"{curent_guessed_letters} ", end = "")

  print()

  print(f"number of incorrect guesses remaining: {5- num_of_incorrect_guesses} ")

print()



 print(answer_characters[answer_index], end = "")
      else:
print()

print()

letter = input("Enter a letter: ")

letter = letter.upper()


if letter not in guessed_letters and len(letter) == 1 and re.search("^[A-Z]$", letter):
  if letter in answer_characters:
    # Letter is in puzzle. 
    for current_answer_character_index in range(len(answer_character))s:
     if letter == current_answer_character[current_answer_index]:
   answer_guesses[current_answer_index] = True
  else:
    num_of_incorrect_guessess += 1

# Game is over. Display whether user won or not.
if num_of_incorrect_guessess < 5:
  print("Congratulations, you solved the puzzle!")
else:
print("sorry, you ran out of guesses.")

print(f"{anser_characters} is the answer to the puzzle.")