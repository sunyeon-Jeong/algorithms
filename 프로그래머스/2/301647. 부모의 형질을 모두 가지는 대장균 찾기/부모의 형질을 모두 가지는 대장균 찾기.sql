-- 코드를 작성해주세요
SELECT 
    e.ID 
    , e.GENOTYPE
    , p.GENOTYPE AS PARENT_GENOTYPE
FROM
    ECOLI_DATA e
JOIN
    ECOLI_DATA p
ON
    e.PARENT_ID = p.ID
WHERE
    (e.GENOTYPE & p.GENOTYPE) = p.GENOTYPE
ORDER BY
    e.ID;
    
-- [자식의 개체 형질] & [부모의 개체 형질] = [부모의 개체 형질]