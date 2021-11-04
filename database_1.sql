CREATE TABLE `register` (
  `id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255),
  `email` varchar(255),
  `phone` varchar(255),
  `username` varchar(255),
  `password` varchar(255),
   PRIMARY KEY (id)
);

CREATE TABLE `sell` (
  `id` int NOT NULL AUTO_INCREMENT,
  `apartment_name` varchar(255),
  `owner_name` varchar(255),
  `state` varchar(255),
  `address` varchar(255),
  `price` double,
  `bed` int,
  `bath` int,
  `sq_ft` double,
  `type` varchar(255),
   PRIMARY KEY (`id`)
);

CREATE TABLE `rent` (
  `id` int NOT NULL AUTO_INCREMENT,
  `apartment_name` varchar(255),
  `owner_name` varchar(255),
  `state` varchar(255),
  `address` varchar(255),
  `price` double,
  `bed` int,
  `bath` int,
  `sq_ft` double,
  `type` varchar(255),
   PRIMARY KEY (`id`)
);

CREATE TABLE `buy` (
  `id` int NOT NULL AUTO_INCREMENT,
  `buyer_name` varchar(255),
  `phone` varchar(255),
  `email` varchar(255),
  `address` varchar(255),
  `type` varchar(255),
  `buying_id` int,
   PRIMARY KEY (`id`)
);
