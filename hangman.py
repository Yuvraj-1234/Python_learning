import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6

chosen_word = random.choices(word_list)
print(f"Psst!! The solution is {chosen_word}")
letter = []
for char in chosen_word:
  char = '_'
  letter += char
print(letter)  

end_of_game = False
while not end_of_game:
    guess = input("Ask the user to guess a word: ")
    
    for k in range(0, len(chosen_word)):
        if guess == chosen_word[k]:
          letter[k] = guess

    if guess not in chosen_word:
      lives -= 1
      print(stages[lives+1])
      if lives == -1:
        print("You lose")
        break
          #join all the letters into a string    
    print(f"{' '.join(letter)}")

    if "_" not in letter:
      end_of_game = True
      print("You win")  
