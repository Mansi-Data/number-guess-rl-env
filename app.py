from fastapi import FastAPI
from pydantic import BaseModel
from environment import NumberGuessGame

app = FastAPI()
game = NumberGuessGame()

class GuessInput(BaseModel):
    guess: int

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/reset")
def reset():
    message = game.reset()
    return {"message": message}

@app.post("/step")
def step(action: GuessInput):
    result = game.step(action.guess)
    return {
        "message": result,
        "done": game.done,
        "attempts": game.attempts
    }

@app.get("/state")
def state():
    return {
        "attempts": game.attempts,
        "max_attempts": game.max_attempts,
        "done": game.done
    }