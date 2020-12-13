# Write your MySQL query statement below

SELECT Customers.name as 'Customers' FROM Customers where Customers.Id NOT IN (SELECT CustomerId FROM Orders);
