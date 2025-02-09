select max(salary) AS SecondHighestSalary from Employee
where salary < (select max(salary) from Employee)