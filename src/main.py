from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check_handler():
    return {"kim":"younghyeon"}

todo_data = {
    1: {
        "id" :1,
        "contents" : "실전! FastAPI 섹션 0수강",
        "is_done" : True
    }
}