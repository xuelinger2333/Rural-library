from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

ROOT_PASSWORD = "rural-library"

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/library")
async def get_libraries():
    with open("libraries.json", "r") as f:
        libraries = json.load(f)
    return libraries

@app.post("/library")
async def update_libraries(libraries: str):
    libraries = json.load(libraries)
    with open("libraries.json", "w") as f:
        json.dump(libraries, f)
    return {"message": "Library updated successfully"}

class User(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(user: User):
    if user.name == 'root' and user.password == ROOT_PASSWORD:
        return {"message": "Login successful"}
    else:
        return {"message": "Login failed"}

