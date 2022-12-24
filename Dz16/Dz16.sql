# Завдання 1
use pds;
select * from employees order by FIRST_NAME
# Завдання 2
select FIRST_NAME as Name, LAST_NAME as Surname, SALARY as Salary, SALARY*0.15 as Taxes  from employees
# Завдання 3
select sum(SALARY) as Total_salaries from employees
# Завдання 4
select max(SALARY) as Maximum_salarys, min(SALARY) as Minimum_salary from employees
# Завдання 5
select avg(SALARY) as Average_salary, count(EMPLOYEE_ID) as Average_amount from employees
