# [프로그래머스 MySQL - Lv.2](https://school.programmers.co.kr/learn/challenges?order=recent&page=1&levels=2&languages=mysql)



## 조건에 맞는 도서와 저자 리스트 출력하기

```MYSQL
-- 코드를 입력하세요
SELECT BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK AS A
JOIN AUTHOR AS B ON A.AUTHOR_ID = B.AUTHOR_ID
WHERE CATEGORY = '경제'
ORDER BY PUBLISHED_DATE;
```



## 성분으로 구분한 아이스크림 총 주문량

```MYSQL
-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, SUM(TOTAL_ORDER)
FROM FIRST_HALF AS A
JOIN ICECREAM_INFO AS B ON A.FLAVOR = B.FLAVOR
GROUP BY INGREDIENT_TYPE
ORDER BY TOTAL_ORDER;
```



## 진료과별 총 예약 횟수 출력하기

```MYSQL
-- 코드를 입력하세요
SELECT MCDP_CD AS '진료과코드', COUNT(PT_NO) AS '5월예약건수'
FROM APPOINTMENT
WHERE YEAR(APNT_YMD) = '2022'
AND MONTH(APNT_YMD) = '05'
GROUP BY MCDP_CD
ORDER BY COUNT(PT_NO) ASC, MCDP_CD ASC;

# ORDER BY 5월예약건수 ASC, 진료과코드 ASC; # 가능
# ORDER BY '5월예약건수' ASC, '진료과코드' ASC; # 불가능
```



## 재구매가 일어난 상품과 회원 리스트 구하기

```mysql
# -- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) > 1
ORDER BY USER_ID ASC, PRODUCT_ID DESC;

# -- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID  FROM (
    SELECT USER_ID, PRODUCT_ID, count(*) as CNT
    From ONLINE_SALE
    group by USER_ID, PRODUCT_ID
) AS T
WHERE T.CNT >= 2
ORDER BY USER_ID ASC, PRODUCT_ID DESC;

# HAVING
HAVING – 34.23
GROUP BY 없이도 사용가능하긴 함
집계함수가 아닌 일반속성에 대한 조건을 줄 수도 있음(이 경우에는 HAVING 조건을 WHERE 절에 붙여도 똑같은 결과가 나옴)

# SELECT 문장 실행 순서
FROM – WHERE – GROUP BY – HAVING – SELECT – ORDER BY


```



## 상품 별 오프라인 매출 구하기

```mysql
# -- 코드를 입력하세요
SELECT PRODUCT_CODE, SUM(SALES_AMOUNT) * PRICE AS SALES
FROM PRODUCT AS A
JOIN OFFLINE_SALE AS B ON A.PRODUCT_ID = B.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY SUM(SALES_AMOUNT) * PRICE DESC, PRODUCT_CODE ASC;

```



## 가격대 별 상품 개수 구하기

```MYSQL
-- 코드를 입력하세요
SELECT TRUNCATE(PRICE, -4) AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP;


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



## 카테고리 별 상품 개수 구하기

```MYSQL
-- 코드를 입력하세요
SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(*) PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY

```



## 3월에 태어난 여성 회원 목록 출력하기

```MYSQL
-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE 
WHERE TLNO IS NOT NULL
AND MONTH(DATE_OF_BIRTH) = 03
AND GENDER = 'W'
ORDER BY MEMBER_ID ASC;
```



## 가격이 제일 비싼 식품의 정보 출력하기

```MYSQL
-- 코드를 입력하세요
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT 
WHERE PRICE = (SELECT MAX(PRICE) 
               FROM FOOD_PRODUCT)
                    
```



## DATETIME에서 DATE로 형 변환

```mysql
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS;
```







































.









