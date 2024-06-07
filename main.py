from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from todo import todo_router
import uvicorn

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def welcome() -> dict:
    return {
        "msg": "hello world?"
    }

@app.get("/todo", response_class=HTMLResponse)
async def get_todo_html():
    with open("todo_fe/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

app.mount("/static", StaticFiles(directory="todo_fe"), name="static")
app.include_router(todo_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
