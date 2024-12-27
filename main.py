from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from googletrans import Translator
translator = Translator()
from pydantic import BaseModel
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
    text: str
    dest: str = 'hi'

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post('/translate')
def translate(data: Data):
    obj = translator.translate(text=data.text, dest=data.dest)
    return obj.text