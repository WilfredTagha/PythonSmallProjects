word_list = ['elephant', 'giraffe', 'tiger','crocodie','leopard','sheep','goat','pig'] 
stages = [
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''','''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''','''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========   
    ''','''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========   
    ''','''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========   
    ''','''
      +---+
      |   |
      O   |
          |
          |
          |
    =========   
    ''','''
      +---+
      |   |
          |
          |
          |
          |
    =========   
    '''
]
import random
chosen_word = random.choice(word_list)


display = []
for _ in range(len(chosen_word)):
    display += "_"
game_end = False
lives = 6
while not game_end:
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("you loose")
            game_end = True
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if "_" not in display:
        print("You win")
        game_end = True
    
    print(stages[lives])
    print(display)


