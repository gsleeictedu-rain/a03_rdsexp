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

def select_emps(ename:str, job:str):
    conn = get_db_conn()
    try:
        with conn.cursor() as cursor:
            sql='''
                SELECT *
                FROM emp_test
                WHERE ename LIKE %s AND JOB LIKE %s

            '''
            cursor.execute(sql,(f"%{ename}%", f"%{job}%"))
            return cursor.fetchall()

    finally:
        conn.close()