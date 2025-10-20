USE `investrio-dev-db`;

-- Users

INSERT INTO User (UserID, FullName, UserName, Email, PasswordHash, Role)
VALUES
(1, 'Richard Lahaie', 'rlahaie', 'richard.lahaie@example.com', 'hashed_pw1', 'Admin'),
(2, 'Summer Olson', 'solson', 'summer.olson@example.com', 'hashed_pw2', 'Trader'),
(3, 'Jorge Aguilar', 'jaguilar', 'jorge.aguilar@example.com', 'hashed_pw3', 'Trader');


-- Stocks

INSERT INTO Stock (StockID, Ticker, CompanyName, InitialPrice, CurrentPrice, OpeningPrice, DayHigh, DayLow, FloatShares)
VALUES
(100, 'AAPL', 'Apple Inc.', 170.00, 172.50, 171.00, 173.00, 169.50, 16000000000),
(101, 'TSLA', 'Tesla Inc.', 250.00, 255.00, 252.00, 260.00, 248.00, 3000000000),
(102, 'AMZN', 'Amazon.com Inc.', 130.00, 132.00, 131.00, 134.00, 129.00, 900000000);


-- Brokerage Accounts

INSERT INTO BrokerageAccount (AccountID, UserID, Balance)
VALUES
(500, 1, 15000.00),  -- Richard
(501, 2, 20000.00),  -- Summer
(502, 3, 25000.00);  -- Jorge


-- Positions

INSERT INTO Position (PositionID, AccountID, StockID, Quantity)
VALUES
(1000, 500, 100, 40),  -- Richard owns 40 AAPL
(1001, 501, 101, 25),  -- Summer owns 25 TSLA
(1002, 502, 102, 60);  -- Jorge owns 60 AMZN


-- Orders

INSERT INTO `Order` (OrderID, AccountID, StockID, Action, Quantity, Status, CreatedAt, ExecutedAt)
VALUES
(2000, 500, 101, 'Buy', 10, 'Executed', NOW(), NOW()),  -- Richard bought TSLA
(2001, 501, 100, 'Sell', 5, 'Queued', NOW(), NULL),     -- Summer queued sell of AAPL
(2002, 502, 101, 'Buy', 15, 'Executed', NOW(), NOW());  -- Jorge bought TSLA


-- Trades

INSERT INTO Trade (TradeID, OrderID, ExecutedPrice, ExecutedQty, ExecutedTime)
VALUES
(3000, 2000, 255.00, 10, NOW()),
(3001, 2002, 254.00, 15, NOW());


-- Transactions

INSERT INTO Transaction (TransactionID, AccountID, TransType, Amount)
VALUES
(4000, 500, 'Deposit', 5000.00),   -- Richard deposit
(4001, 501, 'Withdraw', 3000.00),  -- Summer withdrawal
(4002, 502, 'Deposit', 7000.00);   -- Jorge deposit


-- Price Ticks

INSERT INTO PriceTick (TickID, StockID, Timestamp, Price)
VALUES
(6000, 100, NOW(), 172.00),
(6001, 101, NOW(), 256.50),
(6002, 102, NOW(), 133.00);


-- Market Schedule

INSERT INTO MarketSchedule (ScheduleId, Status, OpenHour, OpenMinute, CloseHour, CloseMinute, Holiday)
VALUES
('Open', 9, 30, 16, 0, FALSE);