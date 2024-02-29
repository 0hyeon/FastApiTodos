from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def health_check_handler():
    return {"kim":"younghyeon"}

todo_data = {
    1: {
        "id" :1,
        "contents" : "실전! FastAPI 섹션 0수강",
        "is_done" : True
    },
    2: {
        "id" :2,
        "contents" : "실전! FastAPI 섹션 1수강",
        "is_done" : True
    },
    3: {
        "id" :3,
        "contents" : "실전! FastAPI 섹션 2수강",
        "is_done" : True
    }
}
# uvicorn main:app --reload

@app.get("/todos")
def get_todos_handler(order:str | None = None):
    ret = list(todo_data.values())

    if order == "DESC":
        return ret[::-1] #역정렬s
    return ret


@app.get("/todos/{todo_id}")
def get_todo_hanlder(todo_id :int):
    return todo_data.get(todo_id,{}) #없으면 {} 반환

class CreateToDoRequest(BaseModel):
    id:int
    contents: str
    is_done:bool

@app.post("/todos")
def create_todo_handler(request:CreateToDoRequest):
    todo_data[request.id] = request.dict()
    return todo_data[request.id]


@app.patch("/todos/{todo_id}")
def update_todo_handler(todo_id:int)