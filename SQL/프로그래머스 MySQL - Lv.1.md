# [프로그래머스 MySQL - Lv.1](https://school.programmers.co.kr/learn/challenges?order=recent&page=1&levels=0%2C1&languages=mysql)



[TOC]

## 조건에 부합하는 중고거래 댓글 조회하기

```mysql
-- 코드를 입력하세요
SELECT A.TITLE, B.BOARD_ID, B.REPLY_ID, B.WRITER_ID, B.CONTENTS, DATE_FORMAT(B.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD AS A 
JOIN USED_GOODS_REPLY AS B
ON A.BOARD_ID = B. BOARD_ID
WHERE YEAR(A.CREATED_DATE) = 2022
AND MONTH(A.CREATED_DATE) = 10
ORDER BY B.CREATED_DATE ASC, A.TITLE ASC

```





## 자동차 대여 기록에서 장기/단기 대여 구분하기

```mysql
-- 코드를 입력하세요
SELECT HISTORY_ID, 
       CAR_ID,
       DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
       DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
       CASE WHEN TIMESTAMPDIFF(DAY, START_DATE, END_DATE) >= 29 THEN '장기 대여'
            ELSE '단기 대여'
       END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE YEAR(START_DATE) = 2022
AND MONTH(START_DATE) = 09
ORDER BY HISTORY_ID DESC

-- 코드를 입력하세요
SELECT HISTORY_ID, 
       CAR_ID,
       DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
       DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
       CASE WHEN DATEDIFF(END_DATE, START_DATE) >= 29 THEN '장기 대여'
            ELSE '단기 대여'
       END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE YEAR(START_DATE) = 2022
AND MONTH(START_DATE) = 09
ORDER BY HISTORY_ID DESC


# DATEDIFF() - 두 기간 사이의 일수 계산
DATEDIFF(종료일, 시작일);
SELECT DATEDIFF('2021-12-31','2021-01-20');
	-> 345
SELECT DATEDIFF('2021-12-31','2022-01-20');
	-> -20
SELECT DATEDIFF('2021-12-31', CURRENT_DATE());
	-> -7
# 날짜 포맷에 시간이 포함되어 있는 경우에는 시간은 계산에 포함하지 않습니다.
SELECT DATEDIFF('2021-12-31 11:11:00','2021-01-20 13:00:00');
	-> 345
	
# TIMEDIFF() - 두 기간 사이의 시간 계산
TIMEDIFF(종료시간, 시작시간)
SELECT TIMEDIFF('2022-02-01 23:00:00','2022-01-30 00:00:00');
	-> 71:00:00
SELECT TIMEDIFF('2021-12-31 23:00:00','2022-01-01 00:00:00.000000');
	-> -01:00:00.000000
SELECT TIMEDIFF('2022-01-02 00:00:00',CURRENT_TIMESTAMP());
	-> -135:51:10
SELECT TIMEDIFF('11:30:00','00:00:00');
	-> 11:30:00
	
# () - 두 기간 사이의 여러가지 형태 계산
TIMESTAMPDIFF(반환값 형식, 시작일, 종료일)
SELECT TIMESTAMPDIFF(HOUR, '2022-02-01','2022-02-03');
	-> 48
SELECT TIMESTAMPDIFF(DAY, '2022-02-01','2022-02-03');
	-> 28
SELECT TIMESTAMPDIFF(MONTH, '2021-02-01','2022-03-01');
	-> 13
SELECT TIMESTAMPDIFF(YEAR, '2021-02-01','2022-03-01');
	-> 1
	
```



## 특정 옵션이 포함된 자동차 리스트 구하기

```mysql
-- 코드를 입력하세요
SELECT CAR_ID, CAR_TYPE, DAILY_FEE,	OPTIONS
FROM CAR_RENTAL_COMPANY_CAR 
WHERE OPTIONS LIKE '%네비게이션%'
ORDER BY CAR_ID DESC


# LIKE 조건
A로 시작하는 문자
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE 'A%'
A를 포함하는 문자
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE '%A%'
A로 시작하는 두글자 문자
SELECT 컬럼명 FROM 테이블 WHERE 컬럼명 LIKE 'A_'

# 대소문자 구분할 때에는 BINARY() 로 FIELD 를 감싸주기
WHERE BINARY(컬럼명) LIKE '%el%'
소문자 'el' 만 탐색

```



## 평균 일일 대여 요금 구하기

```mysql
-- 코드를 입력하세요
SELECT ROUND(AVG(DAILY_FEE), 0)
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'
GROUP BY CAR_TYPE


# 숫자함수
ABS: 절대값
ABS(숫자)
POW: 제곱
POW(3, 4) = 3**4 = 81
MOD: 나머지
MOD(15, 4) = 3

# 어림함수
ROUND: 반올림
ROUND(7.45, 1) = 7.5
ROUND(-4.567, 2) = -4.57
ROUND(4567, -2) = 4600
CEIL: (TO INT)올림 
CEIL(7.1) = 8
CEILING(-4.6) = -4	
FLOOR: (TO INT)내림
FLOOR(7.45) = 7
FLOOR(-4.789) = -5

# TRUNCATE
소수점, 시간, 날짜, 요일 등 절사
TRUNCATE(1234.56, 1) 소수점 뒤 첫째까지 남기고 절사 -> 1234.5
TRUNCATE(1234.56, 2) 소수점 뒤 둘째까지 남기고 절사 -> 1234.56
TRUNCATE(1234.56, 0) -> 1234
TRUNCATE(1234.56, -1) 소수점 앞 첫째부터 절사 -> 1230
TRUNCATE(1234.56, -2) 소수점 앞 둘째부터 절사 -> 1200
TRUNCATE(1234.56, -3) 소수점 앞 셋째부터 절사 -> 1000
TRUNCATE(1234.56, -4) 소수점 앞 넷째부터 절사 -> 0

```



## 어린 동물 찾기

```mysql
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION <> 'Aged'
ORDER BY ANIMAL_ID ASC

```



## 역순 정렬하기

```mysql
-- 코드를 입력하세요
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC

```



## 상위 N 개 레코드

```mysql
-- 코드를 입력하세요
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1

```



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

```mysql
# NVL(값, 지정값) - ORACLE O / MYSQL X
값이 NULL 이면 지정값
값이 NULL 아니면 값

# IFNULL(A, B) - MYSQL
A 가 NULL 이 아니면 A
A 가 NULL 이면 B
중첩가능
SELECT IFNULL(column_name, IFNULL(column_name, '대체할 값')) FROM [table_name]; 

# NULLIF(A, B) - ORACLE
A 와 B 가 같으면 NULL,
다르면 A

# COALESCE(값1, 값2, 값3 …)
처음으로 NULL 이 아닌 값

# NULL 속성
COUNT(*) 시 NULL 포함, COUNT(FIELD) 시 NULL 미포함

```



## 가장 비싼 상품 구하기

```mysql
-- 코드를 입력하세요
SELECT MAX(PRICE) AS MAX_PRICE
FROM PRODUCT

```



## 조건에 맞는 회원수 구하기

```mysql
-- 코드를 입력하세요
SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE YEAR(JOINED) = 2021
AND (20 <= AGE AND AGE <= 29);

# (20 <= AGE <= 29) 불가능

# WHERE 절 연산 순서
AND > OR

# SELECT 문장 실행 순서
FROM – WHERE – GROUP BY – HAVING – SELECT – ORDER BY

# COUNT(*)는 NULL 값을 포함하고 COUNT(AGE)와 같이 특정 컬럼을 지정해줄 경우 NULL 값을 포함하지 않는다. 만약 USER_ID 가 NULL 값 허용이라면, COUNT(USER_ID) 가 아닌 COUNT(*) 으로 작성해야 함.

```



## 나이 정보가 없는 회원수 구하기

```MYSQL
-- 코드를 입력하세요
SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE AGE IS NULL;

# WHERE AGE = NULL 불가능	
# COUNT(*)는 NULL 값을 포함하고 COUNT(AGE)와 같이 특정 컬럼을 지정해줄 경우 NULL 값을 포함하지 않는다.

```



## 경기도에 위치한 식품창고 목록 출력하기

```mysql
-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
# WHERE LEFT(ADDRESS, 3) = '경기도'
# WHERE SUBSTRING(ADDRESS, 1, 3) = '경기도'
WHERE SUBSTRING_INDEX(ADDRESS, ' ', 1) = '경기도'
ORDER BY WAREHOUSE_ID;

# 1. 왼쪽에서 문자열 자르기
left(컬럼명 또는 문자열, 왼쪽에서 잘라낼 문자열의 길이)

사용예 : SELECT left("chongmoa.com", 5)
결과 : chong


# 2. 중간에서 문자열 자르기
substring(컬럼 또는 문자열, 시작위치, 길이);

사용예 : SELECT substring("chongmoa.com", 3, 5)
결과 : ongmo
사용예 : SELECT substring("chongmoa.com", 1, 5)
결과 : chong

# 3. 오른쪽에서 문자열 자르기
right(컬럼명 또는 문자열, 길이);

사용예 : SELECT right("chongmoa.com", 3)
결과 : com
사용예 : SELECT right("20140323", 2)
결과 : 23

# 4. 구분자 (delimiter) delim가 count 만큼 나오기 전에 스트링 str 에서 서브 스트링을 리턴.
SUBSTRING_INDEX(str,delim,count)

구분자 (delimiter) delim가 count 만큼 나오기 전에 스트링 str 에서 서브 스트링을 리턴한다.
만일 count 가 양수 (positive)라면, 마지막 구분자의 왼쪽에 있는 모든 것들이 리턴된다. (왼쪽부터 계산이 됨). 
만일 count 가 음수일 경우에는, 마지막 구분자의 오른쪽에 있는 모든 것들이 리턴된다 (오른쪽부터 계산됨).
SUBSTRING_INDEX()는 delim에 대한 검색을 할 때 문자의 크기를 구분한다.
 
사용예 : SELECT SUBSTRING_INDEX('www.chongmoa.com', '.', 2);
결과 : www.chongmoa
사용예 : SELECT SUBSTRING_INDEX('www.chongmoa.com', '.', -2);
결과 : chongmoa.com
사용예 : SELECT SUBSTRING_INDEX('admin@chongmoa.com', '@', 1);
결과 : admin
사용예 : SELECT SUBSTRING_INDEX('admin@chongmoa.com', '@', -1);
결과 : chongmoa.com

```



## 강원도에 위치한 생산공장 목록 출력하기

```mysql
-- 코드를 입력하세요
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
# WHERE SUBSTRING(ADDRESS, 1, 3) = '강원도'
WHERE LEFT(ADDRESS, 3) = '강원도'
ORDER BY FACTORY_ID ASC;

```



## 최댓값 구하기

```MYSQL
-- 코드를 입력하세요
SELECT MAX(DATETIME) AS 시간
FROM ANIMAL_INS;

# 시간도 MIN, MAX 적용가능

```













































