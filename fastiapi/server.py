from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/profile")
def root():
    return {"nome": "Alcione Pereira"}