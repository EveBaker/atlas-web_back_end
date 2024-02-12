-- adds country column

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    email VARCHAR(225) NOT NULL UNIQUE,
    name VARCHAR(225),
    country EMUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id)
);