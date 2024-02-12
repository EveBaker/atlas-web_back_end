-- create user

Create TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    email VARCHAR(225) NOT NULL UNIQUE,
    name VARCHAR (255),
    PRIMARY KEY (id)
);