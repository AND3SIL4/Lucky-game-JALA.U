class Game:
    def __init__(self):
      self.scores = {
          "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10
      }

    def calculate_score(self,word):
        score = 0
        for letter in word:
            letter = letter.lower()
            if letter in self.scores:
                score += self.scores[letter]
        return score
game = Game() # Instance
while True:
  print("...Welcome to the game...")
  print("If you want exit, enter 000")
  word = input("For play enter only words: ").lower()
  if word == "000":
    break 
  elif not word.isalpha(): #[!@#$%^&*()]
    print("Invalid, please try again")
  game.calculate_score(word) # Calculate word score 
  score = game.calculate_score(word)
  print(f"The word score '{word}' is: {score}")
  print()
print("Thank you for play, see you")