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

# ORDER BY '5월예약건수' ASC, '진료과코드' ASC; 불가능
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



