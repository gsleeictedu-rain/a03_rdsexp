from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from datetime import datetime
from pydantic import BaseModel
import os
import uvicorn
import database1

app = FastAPI()

# 절대 경로를 사용하여 템플릿 경로 오류(TemplateNotFound) 방지
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "../a01_front"))


# http://127.0.0.1:8000/
@app.get("/")
async def empList(request:Request):
    return templates.TemplateResponse(request=request, name="a02_hero.html")

# http://127.0.0.1:8000/api/emps
# @app.get("/api/emps")
# def get_emps(ename:str = "", job:str=""):
#     return database.select_emps(ename, job)

# 웹 브라우저 CORS 허용 설정
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# 신규 용사 추가 API
@app.get("/api/addhero")
def addHero(
    nickname: str = "", 
    jobclass: str = "", 
    level: int = 1, 
    mainskill: str = "", 
    tacticalpos: str = "", 
    joindate: datetime | None = None
):
    try:
        if not nickname or not jobclass:
            raise HTTPException(status_code=400, detail="닉네임과 직업군은 필수입니다.")
            
        new_id = database1.addHero(nickname, jobclass, level, mainskill, tacticalpos, joindate)
        return {
            "status": "success", 
            "message": f"용사 [{nickname}] 님이 길드에 합류했습니다!", 
            "hero_id": new_id
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


# 길드원 목록 조회 API
@app.get("/api/heroes")
def getHeroes(keyword: str = ""):
    try:
        heroes = database1.searchHeroes(keyword)
        return {"status": "success", "data": heroes}
    except Exception as e:
        return {"status": "error", "message": str(e)}
# hero_id INT AUTO_INCREMENT PRIMARY KEY COMMENT '용사 고유 번호',
# nickname VARCHAR(50) NOT NULL COMMENT '용사 닉네임',
# job_class VARCHAR(30) NOT NULL COMMENT '직업군',
# level INT DEFAULT 1 COMMENT '현재 레벨',
# main_skill VARCHAR(100) COMMENT '주력 스킬',
# tactical_position VARCHAR(50) COMMENT '전술 배치 포지션',
# join_date DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '길드 가입일'

# 4. main() 실행시, 메모리에 로딩할 코드 처리..
if __name__ == "__main__":
    # 서버 실행 
    uvicorn.run("main01:app", host="127.0.0.1", port=8000, reload=True)    