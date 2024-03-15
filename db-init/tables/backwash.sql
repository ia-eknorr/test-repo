-- liquibase formatted sql
-- changeset cahrens:report-backwash-table
USE WaterTreatment;

DROP TABLE IF EXISTS `backwash`;

CREATE TABLE `backwash` (
  `index` int(11) NOT NULL AUTO_INCREMENT,
  `filter` int(8) DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `duration` float DEFAULT NULL,
  `backwash_type` char(1) DEFAULT NULL,
  `turb_before` float DEFAULT NULL,
  `loh_before` float DEFAULT NULL,
  `flow_before` float DEFAULT NULL,
  `level_before` float DEFAULT NULL,
  `turb_after` float DEFAULT NULL,
  `loh_after` float DEFAULT NULL,
  `flow_after` float DEFAULT NULL,
  `level_after` float DEFAULT NULL,
  PRIMARY KEY (`index`)
  );