from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os
import uvicorn
import database

app = FastAPI()

# 절대 경로를 사용하여 템플릿 경로 오류(TemplateNotFound) 방지
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "../a01_front"))



class Emp(BaseModel):
    empno: int
    ename: str
    job: str
    sal: int

# http://127.0.0.1:8000/
@app.get("/")
async def empList(request:Request):
    return templates.TemplateResponse(request=request, name="a01_emp.html")

# http://127.0.0.1:8000/api/emps
@app.get("/api/emps")
def get_emps(ename:str = "", job:str=""):
    return database.select_emps(ename, job)



# 4. main() 실행시, 메모리에 로딩할 코드 처리..
if __name__ == "__main__":
    # 서버 실행 
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)    