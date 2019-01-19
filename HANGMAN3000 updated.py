import random

class Hangman:
        words_dic = {"a fruit":['apple','orange','mango','banana','pear','kiwi'],"an animal":['donkey','monkey','baboon','dolphin','tiger'],"a super hero":['hulk','ironman','superman','batman']}
        picture = (
              """
               ------
               |    |
               |
               |
               |
               |
               |
               |
              ----------
              """,
              """
               ------
               |    |
               |    O
               |
               |
               |
               |
               |
              ----------
              """,
              """
               ------
               |    |
               |    O
               |    |
               |
               |
               |
               |
              ----------
              """,
              """
               ------
               |    |
               |    O
               |   \|
               |
               |
               |
               |
              ----------
              """,
              """
               ------
               |    |
               |    O
               |   \|/
               |
               |
               |
               |
              ----------
              """,
              """
               ------
               |    |
               |    O
               |   \|/
               |   /
               |
               |
               |
               |
              ----------
              """,
              """
               ------
               |    |
               |    O
               |   \|/
               |   / \
               |
               |
               |
               |
              ----------
              """)

        def __init__(self):
            #constructor of the class Hangman
            self.word = self.random_word()
            self.status = "-" * len(self.word)
            self.guessed_letters = []
            self.fails = 0

        def random_word(self):
            #function that generates random word from the dictionary's values
            self.category = random.choice(list(self.words_dic))
            self.words_list = self.words_dic[self.category]
            self.word = random.choice(self.words_list)
            return self.word


        def game(self):
            #main game set up. connected with progress, players_guess and check funcions. it runs those functions until incorrect guesses number is less than number of pictures items(6) and while word is not yet guessed
                print('Welcome to the picture 3000 !')
                print('In this game you will be able to achieve great results in guessing most complicated words in English language')
                while self.fails < len(self.picture) and self.status != self.word:
                        self.progress()
                        guess = self.players_guess()
                        self.check(guess)

                self.result()

        def progress(self):
            #calls out the picture accordingly to how many time user failed to guess. shows the status of word, which if letter is correct is update in check function
                print(self.picture[self.fails])
                print("Word : ", self.status)
                print("Letters used: ",self.guessed_letters)
                if self.fails == 5:
                    print("Hey, something to help you out. This word is",self.category)
                else:
                    pass


        def players_guess(self):
            #gets players guess and appends it to the guessed letters list
                guess = input("Guess a letter: ")

                if guess in self.guessed_letters:
                     print("Try again... You've already used this letter")
                     guess = input("Guess a letter: ")
                else:
                     self.guessed_letters.append(guess)

                return guess

        def check(self, guess):
            #checks if guess is in the word and updates stutus of word. if guess is not in the word adds 1 to fails
                    if guess in self.word:
                          print('That is correct')

                          for i in range(len(self.word)):
                              if guess == self.word[i]:
                                  self.status = self.status[:i] + guess + self.status[i+1:]

                    else:
                          print("Incorrect! Try again!")
                          self.fails += 1

        def result(self):
            #final check is used when game while function doesnt meet requirements this function checks whether player won or lost
                    if self.fails == len(self.picture):
                          print("Game over")
                          print("The word was",self.word)
                          user_input = input("Thanks for playing. Press ENTER to exit the game")

                    else:
                          print("You won! Congratulations! The word was",self.word)
                          user_input = input("Thanks for playing. Press ENTER to exit the game")

if __name__ == '__main__':
    play = Hangman()

play.game()
