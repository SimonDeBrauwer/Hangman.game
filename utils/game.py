import random, re
from typing import List, Union
import collections

class Hangman: 
    """
    Class defining the Hangman game containing ALL attributes and functions
    """
    def __init__(self, possible_word_list):
        def Convert(string)->List: 
            mylist=[]
            mylist[:0]=string
            return mylist 

        self.possible_words: List[str]=["becode", "learning", "mathematics", "sessions"]
        self.word_to_find: List[str]=Convert(self.possible_words[possible_word_list])
        self.possible_words=len(self.word_to_find)
        self.well_guessed_letters: List[str]=["_"]*(len(self.word_to_find))
        self.bad_guessed_letters: List[str]=[]
        self.turn_count: int=0
        self.error_count: int=0
        self.lives: int=5

    def play(self):
        guess=input("Guess a letter")
        if not re.match("[a-z]{1}$", guess):
            print("only 1 letter a - z!")
        while lives > 0:
            if len(guess)==1 and guess.isalpha():
                if guess in self.well_guessed_letters:
                    print("Already guessed", guess)
                elif guess in self.word_to_find:
                    self.turn_count+=1
                    indexes=[x.start() for x in re.finditer(guess, self.word_to_find)]
                    for i in indexes:
                        self.well_guessed_letters[i]=guess
                    print("good guess")
                elif guess not in self.word_to_find:
                    self.bad_guessed_letters.append(guess)
                    self.error_count+=1
                    self.lives-=1
                    print("wrong guess")

    def game_over(self):
        """
        The game is ended when lives reach 0
        """
        print("Game Over! ")
        quit()

    
    def well_played(self):
        """
        When you have guessed all letters correctly
        """
        print(f"You guessed the word:{self.word_to_find}in{self.turn_count}turns with{self.error_count}errors!")

    def start_game(self):
        """
        This will start a new game
        """       
        while self.lives>0 and self.turn_count <self.possible_words:
            self.play()           

        if len(self.well_guessed_letters)==len(self.word_to_find):
            self.well_played()
        
        print(f"well_guessed_letters:{self.well_guessed_letters}, Bad guessed letters:{self.bad_guessed_letters}, \n lif:{self.lives}, Error count:{self.error_count}, Turn:{self.turn_count}")

        self.game_over()
        