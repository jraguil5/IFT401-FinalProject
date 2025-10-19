USE `investrio-dev-db`;

-- Script to remove test data.

SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE Trade;
TRUNCATE TABLE `Order`;
TRUNCATE TABLE Position;
TRUNCATE TABLE Transaction;
TRUNCATE TABLE PriceTick;
TRUNCATE TABLE BrokerageAccount;
TRUNCATE TABLE Stock;
TRUNCATE TABLE User;
TRUNCATE TABLE MarketSchedule;

SET FOREIGN_KEY_CHECKS = 1;