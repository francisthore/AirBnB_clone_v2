-- script that prepares dbs, create a user and grant users permission
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE DATABASE IF NOT EXISTS performance_schema;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED WITH authentication_plugin BY 'hbnb_dev_pwd';

GRANT  ALL PRIVILEGES on hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT on performance_schema TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
