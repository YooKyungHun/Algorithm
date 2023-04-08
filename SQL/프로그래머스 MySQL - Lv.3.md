# [프로그래머스 MySQL - Lv.3](https://school.programmers.co.kr/learn/challenges?order=recent&page=1&levels=3&languages=mysql)



## 카테고리별 도서 판매량 집계하기

```MYSQL
-- 코드를 입력하세요
SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK AS A
JOIN BOOK_SALES  AS B ON B.BOOK_ID = A.BOOK_ID
# WHERE YEAR(SALES_DATE) = 2022
# AND MONTH(SALES_DATE) = 01
WHERE SALES_DATE LIKE '2022-01%'
GROUP BY CATEGORY
ORDER BY CATEGORY ASC;

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



## 즐겨찾기가 가장 많은 식당 정보 출력하기

```MYSQL
-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (SELECT FOOD_TYPE, MAX(FAVORITES)
                                 FROM REST_INFO
                                 GROUP BY FOOD_TYPE)
ORDER BY FOOD_TYPE DESC;

```



## 조건에 맞는 사용자와 총 거래금액 조회하기

```mysql
-- 코드를 입력하세요
SELECT B.USER_ID, B.NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS A
JOIN USED_GOODS_USER AS B
ON A.WRITER_ID = B.USER_ID
WHERE STATUS = 'DONE'
GROUP BY A.WRITER_ID
HAVING SUM(PRICE) >= 700000
ORDER BY SUM(PRICE) ASC

```







## **조건별로 분류하여 주문상태 출력하기**

```MYSQL
-- 코드를 입력하세요
SELECT ORDER_ID, 
       PRODUCT_ID, 
       DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS DATE_FORMAT,
       IF(OUT_DATE <= '2022-05-01', '출고완료',
          IF(OUT_DATE IS NULL, '출고미정','출고대기')) AS 출고여부
FROM FOOD_ORDER 
ORDER BY ORDER_ID ASC

-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d'), 
    CASE
        WHEN OUT_DATE <= '2022-05-01'
        	THEN '출고완료'
        WHEN OUT_DATE > '2022-05-01'
        	THEN '출고대기'
        ELSE '출고미정'
    END AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID ASC


# IF 문
IF(조건문, 참일때 값, 거짓일때 값)
SELECT IF(SEQ < 3, 'A', 'B') AS RESULT
FROM A_TABLE

# CASE 문
# 조건1도 참이면 조건2 의 참여부와 상관없이 반환값1 로 됨
CASE
	WHEN 조건1 THEN '반환값1'
	WHEN 조건2 THEN '반환값2'
	ELSE '기타 반환값'
END

```



## 오랜 기간 보호한 동물(2)

```mysql
-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.NAME 
FROM ANIMAL_INS AS A, ANIMAL_OUTS AS B 
WHERE A.ANIMAL_ID = B.ANIMAL_ID 
ORDER BY B.DATETIME - A.DATETIME DESC
LIMIT 2

-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS AS A
INNER JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY DATEDIFF(A.DATETIME, B.DATETIME)
LIMIT 2

```





## 헤비 유저가 소유한 장소

```MYSQL
-- 코드를 입력하세요
SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (SELECT HOST_ID
         FROM PLACES
         GROUP BY HOST_ID
         HAVING COUNT(*) > 1)
ORDER BY ID


SELECT A.ID, A.NAME, A.HOST_ID
FROM PLACES AS A
JOIN (SELECT COUNT(*) AS CNT, HOST_ID
      FROM PLACES
      GROUP BY HOST_ID
      HAVING CNT > 1
     ) AS B ON A.HOST_ID = B.HOST_ID
ORDER BY ID

```



## 있었는데요 없었습니다

```MYSQL
-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS AS A
JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE TIMEDIFF(A.DATETIME, B.DATETIME) > 0
ORDER BY A.DATETIME

```





## 오랜 기간 보호한 동물(1)

```mysql
-- 코드를 입력하세요
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS AS A
WHERE A.ANIMAL_ID NOT IN (SELECT ANIMAL_ID
                      FROM ANIMAL_OUTS)
ORDER BY DATETIME
LIMIT 3

-- 코드를 입력하세요
SELECT A.name, A.datetime 
FROM animal_ins AS A 
LEFT JOIN animal_outs AS B
ON A.animal_id = B.animal_id
WHERE B.animal_id IS NULL
ORDER BY A.datetime ASC
LIMIT 3

```

