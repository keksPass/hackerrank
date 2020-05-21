select name from STUDENTS 
where marks > 75
order by lower(substr(name, -3)), id asc;
