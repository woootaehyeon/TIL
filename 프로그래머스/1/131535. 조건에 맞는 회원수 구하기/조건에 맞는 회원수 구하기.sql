SELECT COUNT(*)
FROM user_info
WHERE (joined >= TO_DATE('2021-01-01', 'YYYY-MM-DD') AND joined <= TO_DATE('2021-12-31', 'YYYY-MM-DD'))
and (age >= 20 and age <= 29);
