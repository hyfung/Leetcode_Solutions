# Write your MySQL query statement below
SELECT d.class FROM (SELECT DISTINCT * FROM courses) AS d
GROUP BY d.class HAVING count(d.class) > 4;
