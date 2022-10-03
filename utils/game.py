import random


class Hangman:
    def __init__(self,possible_words, word_to_find, well_guessed_letters, bad_guessed_letters, turn_count, error_count, lives):
        self.possible_words=["becode", "learning", "mathematics", "sessions"]
        self.word_to_find=random.choice(list(self.possible_words)) #split each letter into string
        self.well_guessed_letters= #starts with "_" and gets replaced by correct guessed letter
        self.bad_guessed_letters= #regex all letters that are NOT in the selected word
        self.turn_count=0
        self.error_count=0
        self.lives=5

    def play()
    