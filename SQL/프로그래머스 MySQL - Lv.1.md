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

```mysql
# NVL(값, 지정값) - ORACLE O / MYSQL X
값이 NULL 이면 지정값
값이 NULL 아니면 값

# IFNULL(A, B) - MYSQL
A 가 NULL 이 아니면 A
A 가 NULL 이면 B
중첩가능
SELECT IFNULL(column_name, IFNULl(column_name, '대체할 값')) FROM [table_name]; 

# NULLIF(A, B) - ORACLE
A 와 B 가 같으면 NULL,
다르면 A

# COALESCE(값1, 값2, 값3 …)
처음으로 NULL 이 아닌 값

# NULL 속성
COUNT 시 집계되지 않음
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
```



## 나이 정보가 없는 회원수 구하기

```MYSQL
-- 코드를 입력하세요
SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE AGE IS NULL;

# WHERE AGE = NULL 불가능	
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
만일 count 가 양수 (positive)라면, 마지막 구분자의 왼쪽에 있는 모든 것들이 리턴된다.
(왼쪽부터 계산이 됨). 만일 count 가 음수일 경우에는, 마지막 구분자의 오른쪽에 있는 모든 것들이 리턴된다 (오른쪽부터 계산됨).
SUBSTRING_INDEX()는 delim에 대한 검색을 할 때 문자의 크기를 구분한다.
 
사용예 : SELECT SUBSTRING_INDEX('www.chongmoa.com', '.', 2);
결과 : www.chongmoa
사용예 : SELECT SUBSTRING_INDEX('www.chongmoa.com', '.', -2);
결과 : chongmoa.com
사용예 : SELECT SUBSTRING_INDEX('admin@chongmoa.com', '@', 1)
결과 : admin
사용예 : SELECT SUBSTRING_INDEX('admin@chongmoa.com', '@', -1)
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



## **최댓값 구하기**

```MYSQL
-- 코드를 입력하세요
SELECT MAX(DATETIME) AS 시간
FROM ANIMAL_INS;

# 시간도 MIN, MAX 적용가능
```













































