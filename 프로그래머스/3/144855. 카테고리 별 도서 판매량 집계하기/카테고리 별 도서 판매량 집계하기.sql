-- 코드를 입력하세요
SELECT
    BOOK.CATEGORY
    , SUM(SALES.SALES) AS TOTAL_SALES
FROM
    BOOK BOOK
JOIN
    BOOK_SALES SALES
ON
    BOOK.BOOK_ID = SALES.BOOK_ID
WHERE
    SALES.SALES_DATE LIKE '2022-01%'
GROUP BY
    BOOK.CATEGORY
ORDER BY
    BOOK.CATEGORY ASC;