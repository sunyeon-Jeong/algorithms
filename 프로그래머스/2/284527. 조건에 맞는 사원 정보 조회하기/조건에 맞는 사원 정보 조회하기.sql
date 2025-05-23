-- 코드를 작성해주세요
SELECT
    SUM(GRADE.SCORE) AS SCORE
    , EMPLOYEES.EMP_NO
    , EMPLOYEES.EMP_NAME
    , EMPLOYEES.POSITION
    , EMPLOYEES.EMAIL
FROM
    HR_EMPLOYEES EMPLOYEES
JOIN
    HR_GRADE GRADE
ON
    EMPLOYEES.EMP_NO = GRADE.EMP_NO
GROUP BY
    GRADE.EMP_NO
ORDER BY
    SCORE DESC
LIMIT 1;