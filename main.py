# add fastapi import

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def test_api():
        return {"message": "Hello, FastAPI!"}