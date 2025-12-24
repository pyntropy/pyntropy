from fastapi import FastAPI


app = FastAPI(
    title="Pyntropy"
)


@app.get("/")
def home():
    return {"message": "Hello World"}