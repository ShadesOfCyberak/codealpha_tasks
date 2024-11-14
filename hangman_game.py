import random
import time

class Hangman:
    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty
        self.__wordlist = {
            "easy": ["apple", "banana", "cherry", "date", "elderberry"],
            "medium": ["orange", "pear", "quince", "raspberry", "strawberry"],
            "hard": ["apricot", "blueberry", "cranberry", "dragonfruit", "elderberry"]
        }
        self.word = random.choice(self.__wordlist[self.difficulty])
        self.guessed_letters = set()
        self.attempts_remaining = 5
        self.hints = {
            "easy": 2,
            "medium": 1,
            "hard": 0
        }
        self.start_time = time.time()

    def display_word(self,ret = False):
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        if ret:
            return display
        print(display)

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print("You already guessed that letter.")
            return False
        self.guessed_letters.add(letter)
        if letter in self.word:
            print("Correct guess!")
            return True
        else:
            print("Incorrect guess.")
            self.attempts_remaining -= 1
            return False

    def check_win(self):
        if ("_" not in self.display_word(ret=True)):
            return True
        return False

    def check_lose(self):
        if self.attempts_remaining <= 0:
            return True
        return False

    def give_hint(self):
        if self.hints[self.difficulty] > 0:
            hint = random.choice(self.word)
            while hint in self.guessed_letters:
                hint = random.choice(self.word)
            print("Hint:", hint)
            self.hints[self.difficulty] -= 1
        else:
            print("No more hints available.")

    def play(self):
        while True:
            self.display_word()
            print("Attempts remaining:", self.attempts_remaining)
            guess = input("Enter a letter or \"hint\": ").lower()
            if guess == "hint":
                self.give_hint()
            elif len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
            else:
                if self.guess_letter(guess):
                    if self.check_win():
                        print("\nCongratulations! You won!")
                        print("Time taken:", round(time.time() - self.start_time, 2), "seconds")
                        break
                else:
                    if self.check_lose():
                        print("Game over! The word was:", self.word)
                        break

if __name__ == "__main__":
    difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()
    hangman = Hangman(difficulty)
    hangman.play()