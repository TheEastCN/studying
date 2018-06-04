1、程序使用第三方模块PrettyTable进行表格输出

2、 本程序支持以下查询语句，条件可进行更换
find name,age from staff_table where age > 22
find * from staff_table where dept = IT
find * from staff_table where enroll_date like 2013

add staff_table Alex Li,25,134435344,IT,2015-10-29

del from staff where id = 3

UPDATE staff_table SET dept = Market WHERE dept = IT 
UPDATE staff_table SET age = 25 WHERE name = Alex Li

