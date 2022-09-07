from fastapi import FastAPI

app = FastAPI()


@app.get("/games")
async def games():
    return {"message": "Hello World"}
