DROP TABLE IF EXISTS Orders;

CREATE TABLE Orders (
    OrderId INT,
    OrderStatus VARCHAR(30),
    LastUpdated DATETIME
);

INSERT INTO Orders
    VALUES(1, 'Backordered', '2020-06-01 12:00:00');
INSERT INTO Orders
    VALUES(1, 'Shipped', '2020-06-09 12:00:25');
INSERT INTO Orders
    VALUES(2, 'Shipped', '2020-07-11 3:05:00');
INSERT INTO Orders
    VALUES(1, 'Shipped', '2020-06-09 11:50:00');
INSERT INTO Orders
    VALUES(3, 'Shipped', '2020-07-12 12:00:00');
