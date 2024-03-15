CREATE DATABASE IF NOT EXISTS WaterTreatment;

USE WaterTreatment;

SELECT user FROM mysql.user WHERE user = 'ignition' AND host = '%';
CREATE USER IF NOT EXISTS 'ignition'@'%' IDENTIFIED BY 'ignition';
GRANT ALL PRIVILEGES ON WaterTreatment.* TO 'ignition'@'%';

FLUSH PRIVILEGES;

