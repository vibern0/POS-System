BEGIN TRANSACTION;
CREATE TABLE "users" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT,
	`password`	TEXT
);
CREATE TABLE "products" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT,
	`type`	TEXT,
	`stock`	INTEGER,
	`price`	INTEGER
);
CREATE TABLE `logs` (
	`id`	INTEGER,
	`type`	TEXT
);
CREATE TABLE `buylist` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`pay_number`	INTEGER,
	`total_price`	INTEGER,
	`author`	TEXT
);
CREATE TABLE `articles_buylist` (
	`id_list`	INTEGER,
	`id_product`	INTEGER,
	`price`	INTEGER,
	`tax`	INTEGER
);
COMMIT;
