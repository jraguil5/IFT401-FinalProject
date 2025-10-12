-- Create the database
CREATE DATABASE IF NOT EXISTS investrio;
USE investrio;

-- User table
CREATE TABLE User (
    UserID BIGINT PRIMARY KEY,
    FullName VARCHAR(100),
    UserName VARCHAR(50) UNIQUE,
    Email VARCHAR(100) UNIQUE,
    PasswordHash VARCHAR(255),
    Role VARCHAR(20)
);

-- Stock table
CREATE TABLE Stock (
    StockID BIGINT PRIMARY KEY,
    Ticker VARCHAR(10) UNIQUE,
    CompanyName VARCHAR(100),
    InitialPrice DECIMAL(12,2),
    CurrentPrice DECIMAL(12,2),
    OpeningPrice DECIMAL(12,2),
    DayHigh DECIMAL(12,2),
    DayLow DECIMAL(12,2),
    FloatShares BIGINT
);

-- BrokerageAccount table
CREATE TABLE BrokerageAccount (
    AccountID BIGINT PRIMARY KEY,
    UserID BIGINT,
    Balance DECIMAL(12,2),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);

-- Position table
CREATE TABLE Position (
    PositionID BIGINT PRIMARY KEY,
    AccountID BIGINT,
    StockID BIGINT,
    Quantity BIGINT,
    FOREIGN KEY (AccountID) REFERENCES BrokerageAccount(AccountID),
    FOREIGN KEY (StockID) REFERENCES Stock(StockID),
    UNIQUE (AccountID, StockID)
);

-- Order table
CREATE TABLE `Order` (
    OrderID BIGINT PRIMARY KEY,
    AccountID BIGINT,
    StockID BIGINT,
    Action VARCHAR(10), -- Values: Buy, Sell
    Quantity BIGINT,
    Status VARCHAR(20), -- Values: Queued, Executed, Canceled
    CreatedAt TIMESTAMP,
    ExecutedAt TIMESTAMP,
    FOREIGN KEY (AccountID) REFERENCES BrokerageAccount(AccountID),
    FOREIGN KEY (StockID) REFERENCES Stock(StockID)
);

-- Trade table
CREATE TABLE Trade (
    TradeID BIGINT PRIMARY KEY,
    OrderID BIGINT,
    ExecutedPrice DECIMAL(12,2),
    ExecutedQty BIGINT,
    ExecutedTime TIMESTAMP,
    FOREIGN KEY (OrderID) REFERENCES `Order`(OrderID)
);

-- Transaction table
CREATE TABLE Transaction (
    TransactionID BIGINT PRIMARY KEY,
    AccountID BIGINT,
    TransType VARCHAR(20), -- Values: Withdraw, Deposit
    Amount DECIMAL(12,2),
    FOREIGN KEY (AccountID) REFERENCES BrokerageAccount(AccountID)
);

-- PriceTick table
CREATE TABLE PriceTick (
    TickID BIGINT PRIMARY KEY,
    StockID BIGINT,
    Timestamp TIMESTAMP,
    Price DECIMAL(12,2),
    FOREIGN KEY (StockID) REFERENCES Stock(StockID)
);

-- MarketSchedule table
CREATE TABLE MarketSchedule (
    Status VARCHAR(20), -- Values: Open, Closed
    OpenHour INT,
    OpenMinute INT,
    CloseHour INT,
    CloseMinute INT,
    Holiday BOOLEAN
);