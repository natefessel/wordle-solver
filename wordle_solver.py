from typing import Set
from color import Color


class WordleSolver:
    words: Set

    def __init__(self):
        five_letter_words = open("five_letter_words.txt")
        self.words = {word.strip() for word in five_letter_words}

    def input_guess(self, guess):
        pos_dict = {}

        for i, (letter, color) in enumerate(guess):
            pos_arr = pos_dict.get(letter, [0, 0, 0, 0, 0])

            if (color == Color.GRAY):
                pos_arr = [-1 if pos == 0 else pos for pos in pos_arr]
            elif (color == Color.YELLOW):
                pos_arr[i] = -1
            else:
                pos_arr[i] = 1

            pos_dict[letter] = pos_arr
        self.__filter_words(pos_dict)

    def get_words(self):
        return self.words.copy()

    def is_solved(self):
        return len(self.words) <= 1

    def __filter_words(self, pos_dict):
        for letter, pos_arr in pos_dict.items():
            if (pos_arr == [-1, -1, -1, -1, -1]):
                self.words = {word for word in self.words if letter not in word}
            else:
                for i, pos in enumerate(pos_arr):
                    if (pos == -1):
                        self.words = {word for word in self.words if (letter in word and word[i] != letter)}
                    elif (pos == 1):
                        self.words = {word for word in self.words if word[i] == letter}
