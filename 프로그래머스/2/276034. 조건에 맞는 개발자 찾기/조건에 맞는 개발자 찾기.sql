-- 코드를 작성해주세요
SELECT
    ID
    , EMAIL
    , FIRST_NAME
    , LAST_NAME
FROM
    DEVELOPERS
WHERE
    (SKILL_CODE & 256) <> 0  -- Python 스킬 보유
    OR (SKILL_CODE & 1024) <> 0  -- C# 스킬 보유
ORDER BY
    ID ASC;