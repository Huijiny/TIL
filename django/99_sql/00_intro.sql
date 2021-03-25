-- 테이블 생성
CREATE TABLE classmates(
name TEXT,
age INT,
address TEXT
);

CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

CREATE TABLE tests (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL
);

-- 데이터 추가
INSERT INTO classmates (name, age)
VALUES('홍길동', 23);

INSERT INTO classmates
VALUES('홍길동', 23, '서울');

INSERT INTO classmates (name, age, address)
VALUES ('김영희', 21, '대전');

INSERT INTO classmates
VALUES (2, '홍길동', 21, '대전');

INSERT INTO classmates
VALUES ('홍길동', 30, '서울'),
('김철수', 23, '대전'),
('박나래', 23, '광주'),
('이요셉', 33, '구미');

INSERT INTO classmates
VALUES('최철순', 45, '서울');

INSERT INTO tests (name)
VALUES('홍길동'), ('김철수');

INSERT INTO tests (name)
VALUES('최철순');

-- 데이터 조회
SELECT * FROM classmates;

SELECT rowid, * FROM classmates;

SELECT rowid, name FROM classmates;

SELECT rowid, name FROM classmates LIMIT 1;

SELECT rowid, name 
FROM classmates
LIMIT 1 
OFFSET 2;

SELECT rowid, name
FROM classmates
WHERE address='서울';

SELECT DISTINCT age
FROM classmates;

SELECT * FROM users
WHERE age >= 30;

SELECT first_name FROM users
WHERE age >= 30;

SELECT last_name, age FROM users
WHERE age >= 30 AND last_name='김';

SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users
WHERE age >= 30;

SELECT first_name, MAX(balance) FROM users
WHERE age >= 30;

SELECT AVG(balance) FROM users
WHERE age >= 30;

SELECT * FROM users
WHERE phone LIke '%-5114-%';

-- LIKE (wild cards)
SELECT first_name FROM users
WHERE age LIKE '2_';

SELECT * FROM users
WHERE phone LIKE '02-%';

SELECT * FROM users
WHERE first_name LIKE '%준';

-- 테이블 삭제
DROP TABLE classmates;


-- 데이터 삭제
DELETE FROM classmates WHERE rowid=4;
DELETE FROM tests WHERE id=2;

-- 데이터 수정
UPDATE classmates
SET name='홍길동', address='제주'
WHERE rowid=4;

-- ORDER BY
SELECT * FROM users
ORDER BY age
LIMIT 10;

SELECT * FROM users
ORDER BY age, last_name
LIMIT 10;

SELECT last_name, first_name
FROM users
ORDER BY balance DESC
LIMIT 10;

-- GROUP BY
SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name;

SELECT last_name, COUNT(*) AS name_count
FROM users
GROUP BY last_name;

-- ALTER : 테이블명 변경
CREATE TABLE articles (
title TEXT NOT NULL,
content TEXT NOT NULL
);

INSERT INTO articles 
VALUES ('1번 제목', '1번 내용');

ALTER TABLE articles
RENAME TO news;

-- ALTER TABLE : 새로운 컬럼 추가
ALTER TABLE news
ADD COLUMN created_at TEXT NOT NULL;

ALTER TABLE news
ADD COLUMN create_at TEXT;

INSERT INTO news
VALUES ('title', 'content', datetime('now'));

ALTER TABLE news
ADD COLUMN subtitle TEXT NOT NULL DEFAULT 1;