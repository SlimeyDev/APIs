from fastapi import FastAPI
from random import choice

app = FastAPI()

@app.get("/random")
async def get_weather(city: str):
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_+-=[]\;',./{}|:\"<>"
    random_letter = choice(alphabet)
    return {"letter": random_letter}