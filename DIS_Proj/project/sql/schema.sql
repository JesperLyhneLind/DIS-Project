-- Drop tables if they exist
DROP TABLE IF EXISTS hotels;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS reservations;

CREATE TABLE customer (
	username varchar(20) PRIMARY KEY,
	password varchar(255)
);

CREATE TABLE hotels (
    ID INT PRIMARY KEY,
    Owner VARCHAR(255),
    Name VARCHAR(255),
    Type VARCHAR(50),
    Location VARCHAR(255),
    URL VARCHAR(255),
    Availability VARCHAR(255)
);

CREATE TABLE reservations (
    Username VARCHAR(255),
    HotelID INT PRIMARY KEY
);

--
--
----CREATE TABLE attributes (
--    ID INT PRIMARY KEY,
--    Stars INT,
--    Rooms BOOLEAN,
--    Breakfast BOOLEAN,
--    Pool BOOLEAN,
--    Fitness BOOLEAN
--);
--CREATE TABLE reviewandprice (
--    ID INT PRIMARY KEY,
--    Stars INT,
--    ReviewsScore INT,
--    Price INT
--);
--
--CREATE TABLE accessibility (
--    ID INT PRIMARY KEY,
--    Landmarks VARCHAR(255),
--    Pets BOOLEAN,
--    Handicap BOOLEAN
--);
--
--
--
--
--