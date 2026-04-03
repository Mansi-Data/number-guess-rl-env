import random

class NumberGuessGame:

    def __init__(self):
        self.secret_number = None
        self.attempts = 0
        self.max_attempts = 10
        self.done = False

    def reset(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.done = False
        return "Game started! Guess a number between 1 and 100."

    def step(self, guess):
        self.attempts += 1

        if guess == self.secret_number:
            self.done = True
            return f"Correct! Number was {self.secret_number}! 🎉"

        elif self.attempts >= self.max_attempts:
            self.done = True
            return f"Game over! Number was {self.secret_number} ❌"

        elif guess < self.secret_number:
            return "Higher! Try bigger number 📈"

        else:
            return "Lower! Try smaller number 📉"