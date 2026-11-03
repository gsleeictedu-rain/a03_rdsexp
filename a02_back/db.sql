/*
host주소 : mariadb01.cl0mmgmumaz8.ap-southeast-2.rds.amazonaws.com
port : 3306
mariadb01 
admin/whsskTlqkf
*/

-- 1. 데이터베이스(스키마) 선택 (생성되어 있지 않다면 미리 생성)
CREATE DATABASE IF NOT EXISTS hrms_db 
DEFAULT CHARACTER SET utf8mb4 
COLLATE utf8mb4_general_ci;

USE hrms_db;

-- 2. 기존 테이블이 있다면 삭제 후 재생성 (초기화 목적)
DROP TABLE IF EXISTS emp_test;

-- 3. 사원 정보 테이블 생성
CREATE TABLE emp_test (
    empno INT PRIMARY KEY COMMENT '사원번호',
    ename VARCHAR(50) NOT NULL COMMENT '사원이름',
    job VARCHAR(50) COMMENT '직책',
    sal INT COMMENT '급여'
) COMMENT '사원 테스트 테이블';



INSERT INTO emp_test (empno, ename, job, sal) VALUES
(7369, 'SMITH', 'CLERK', 800),
(7499, 'ALLEN', 'SALESMAN', 1600),
(7521, 'WARD', 'SALESMAN', 1250),
(7566, 'JONES', 'MANAGER', 2975),
(7654, 'MARTIN', 'SALESMAN', 1250),
(7698, 'BLAKE', 'MANAGER', 2850),
(7782, 'CLARK', 'MANAGER', 2450),
(7788, 'SCOTT', 'ANALYST', 3000),
(7839, 'KING', 'PRESIDENT', 5000),
(7844, 'TURNER', 'SALESMAN', 1500),
(7876, 'ADAMS', 'CLERK', 1100),
(7900, 'JAMES', 'CLERK', 950),
(7902, 'FORD', 'ANALYST', 3000),
(7934, 'MILLER', 'CLERK', 1300);