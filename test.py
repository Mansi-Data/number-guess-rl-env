from environment import NumberGuessGame

# Create the game
game = NumberGuessGame()

# Start the game
message = game.reset()
print(message)
print("---")

# Make some guesses
guesses = [50, 25, 75, 60, 55]

for guess in guesses:
    print(f"I guess: {guess}")
    result = game.step(guess)
    print(f"Result: {result}")
    print("---")
    
    if game.done:
        print("Game finished!")
        break