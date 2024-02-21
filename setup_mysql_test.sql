-- script that prepares dbs, create a user and grant users permission1
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE DATABASE IF NOT EXISTS performance_schema;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED WITH authentication_plugin BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES on hbnb_test_db.* TO 'hbnb_test'@'hbnb_test';

GRANT SELECT on performance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
