from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from todo import todo_router # added
import uvicorn

app = FastAPI()

origin = ["http://127.0.0.1:5500", "http://50.19.226.105"]

@app.get("/")
async def welcome() -> dict:
    return {
        "msg" : "hello world?"
    }

app.include_router(todo_router)  # added

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
