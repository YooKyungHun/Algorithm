# [프로그래머스 MySQL - Lv.1](https://school.programmers.co.kr/learn/challenges?order=recent&page=1&levels=0%2C1&languages=mysql)



## 조건에 맞는 도서 리스트 출력하기

```mysql
-- 코드를 입력하세요
SELECT BOOK_ID, 
DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY = '인문' AND YEAR(PUBLISHED_DATE) = 2021
ORDER BY PUBLISHED_DATE;
```



## 과일로 만든 아이스크림 고르기

```mysql
-- 코드를 입력하세요
SELECT A.FLAVOR
FROM FIRST_HALF AS A
JOIN ICECREAM_INFO AS B ON A.FLAVOR = B.FLAVOR
WHERE TOTAL_ORDER > 3000
AND INGREDIENT_TYPE = "fruit_based"
ORDER BY TOTAL_ORDER DESC;
```



## 인기있는 아이스크림

```mysql
-- 코드를 입력하세요
SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC;
```



## 흉부외과 또는 일반외과 의사 목록 출력하기

```mysql
-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD IN ('CS', 'GS')
ORDER BY HIRE_YMD DESC, DR_NAME ASC;	
```



## 12세 이하인 여자 환자 목록 출력하기

```mysql
-- 코드를 입력하세요
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE GEND_CD = 'W' AND AGE <= 12
ORDER BY AGE DESC, PT_NAME ASC;

SELECT PT_NAME, PT_NO, GEND_CD, AGE, COALESCE(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE GEND_CD = 'W' AND AGE <= 12
ORDER BY AGE DESC, PT_NAME ASC;

SELECT PT_NAME, PT_NO, GEND_CD, AGE,
	CASE 
		WHEN TLNO IS NULL THEN 'NONE'
		ELSE TLNO
	END AS TLNO
FROM PATIENT
WHERE GEND_CD = 'W' AND AGE <= 12
ORDER BY AGE DESC, PT_NAME ASC;
```

```
NVL(값, 지정값) - ORACLE O / MYSQL X
값이 NULL 이면 지정값
값이 NULL 아니면 값

IFNULL(A, B)
A 가 NULL 이 아니면 A
A 가 NULL 이면 B

COALESCE(값1, 값2, 값3 …)
처음으로 NULL 이 아닌 값

NULL 속성
COUNT 시 집계되지 않음
```



## 가장 비싼 상품 구하기

```mysql
-- 코드를 입력하세요
SELECT MAX(PRICE) AS MAX_PRICE
FROM PRODUCT
```



## 