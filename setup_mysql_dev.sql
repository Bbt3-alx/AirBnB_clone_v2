-- Create the DB hbnb_dv_db if it does not exit
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user hbnb_dev with the password hbnb_dev_pwd if it doen't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileg on the db hbnb_dev_db to the user hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Apply the change
FLUSH PRIVILEGES;
