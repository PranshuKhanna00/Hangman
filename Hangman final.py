import os
import random
import images
import words

def main():
  global word 
  global reveal 
  global lives 
  global gameWon 
  word = random.choice(words.hm_words)
  word = word.upper()
  reveal = list(len(word)*'_')
  lives = 7
  gameWon = False

  while gameWon == False and lives > 0:
    status()
    global guess
    guess = input('\nGuess a letter or an entire word:')
    guess = guess.upper()

    if guess == word:
      gameWon = True
      reveal = word
    elif len(guess) == 1 and guess in word:
      gameWon = check_letter(guess,word)
    else:
      lives -= 1
    status()

  if gameWon:
    print('\nWELL DONE YOU WON')
    loop()
  else:
    print('\nYOU FAILED the word was:',word)
    loop()

def check_letter(letter,word):
  global reveal
  for i in range(0,len(word)):
    letter = word[i]
    if guess == letter:
      reveal[i] = guess
  if '_' not in reveal:
    return True
  else:
    return False
    
def status(): 
  os.system('cls')
  print(images.hangman[7-lives])
  print(' '.join([str(e) for e in reveal]))
  print('\nYou have',lives,'lives')


def loop():
  global play_game
  play_game = input("\nDo You want to play again? y = yes, n = no :")
  while play_game not in ["y", "n","Y","N"]:
      play_game = input("\nDo You want to play again? y = yes, n = no :")
  if play_game == "y":
      main()
  elif play_game == "n":
      print("Thanks For Playing! We expect you back again!")
      time.sleep(3)
      exit()
main()
  
