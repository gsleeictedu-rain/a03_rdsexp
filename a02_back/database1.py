from datetime import datetime

import pymysql
import os

from dotenv import load_dotenv

load_dotenv()

def get_db_conn():
    return pymysql.connect(
        host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"), db=os.getenv("DB_NAME"),
        charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
    )


def addHero(nickname: str, jobclass: str, level: int, mainskill: str, tacticalpos: str, joindate: datetime | None = None):
    conn = get_db_conn()
    try:
        with conn.cursor() as cursor:
            if joindate is None:
                joindate = datetime.now()

            sql = """
                INSERT INTO hero_guild (nickname, job_class, level, main_skill, tactical_position, join_date)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (nickname, jobclass, level, mainskill, tacticalpos, joindate))
            conn.commit()
            return cursor.lastrowid
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def searchHeroes(keyword: str = ""):
    conn = get_db_conn()
    try:
        with conn.cursor() as cursor:
            if keyword:
                sql = """
                    SELECT * FROM hero_guild 
                    WHERE nickname LIKE %s OR job_class LIKE %s
                    ORDER BY level DESC
                """
                search_pattern = f"%{keyword}%"
                cursor.execute(sql, (search_pattern, search_pattern))
            else:
                sql = "SELECT * FROM hero_guild ORDER BY level DESC"
                cursor.execute(sql)
            return cursor.fetchall()
    finally:
        conn.close()