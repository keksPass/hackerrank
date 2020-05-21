SELECT  distinct city FROM STATION 
WHERE lower(CITY) LIKE '%a' or lower(CITY) like '%e' or lower(CITY) like '%i' or lower(CITY) like '%o' or lower(CITY) like '%u';
