from color import Color
from wordle_solver import WordleSolver


if __name__ == '__main__':
    solver = WordleSolver()
    word_length = 5
    num_guess = 0
    while solver.is_solved() is False:
        print(f"Guess #{num_guess}\n")
        guess = []
        print("Enter your guesses as <LETTER>/<COLOR>")
        for i in range(word_length):
            letter_color = input(f"Letter {i}: ").split("/")
            guess_letter = (letter_color[0], Color(letter_color[1]))
            guess.append(guess_letter)
        solver.input_guess(guess)
        print("Possible answers:\n" + str(solver.get_words()))
        print()
        num_guess += 1

    if (len(solver.get_words()) == 0):
        print("There are no words matching the criteria provided")
    else:
        print("Solved!")
