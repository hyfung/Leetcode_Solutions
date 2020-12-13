# Write your MySQL query statement below
SELECT a.Name AS 'Employee' FROM Employee AS a, Employee AS B WHERE a.ManagerId = b.Id AND a.Salary > b.Salary;
