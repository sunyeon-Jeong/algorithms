-- 코드를 입력하세요
SELECT
    (CASE
        WHEN PRICE < 10000 THEN 0
        ELSE TRUNCATE(PRICE, -4)        # 10,000원 미만 -> 0 / 10,000원 이상 -> 정수 네자리 버림
    END) AS PRICE_GROUP
    , COUNT(PRODUCT_ID) AS PRODUCTS
FROM
    PRODUCT
GROUP BY
    PRICE_GROUP
ORDER BY
    PRICE_GROUP ASC;