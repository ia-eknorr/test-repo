-- liquibase formatted sql
-- changeset cahrens:report-backwash-data
USE WaterTreatment;

LOCK TABLES `backwash` WRITE;
INSERT INTO `backwash` VALUES 
(1,1,'2024-2-20 14:01:48','2024-2-20 15:02:49',61,'A',1.1,65.1,10.1,82.1,0.1,12.1,30.1,51.1),
(2,2,'2024-2-20 14:02:48','2024-2-20 15:03:50',61,'M',1.2,65.2,10.2,82.2,0.2,12.2,30.2,51.2),
(3,3,'2024-2-20 14:03:48','2024-2-20 15:04:51',61,'A',1.3,65.3,10.3,82.3,0.3,12.3,30.3,51.3),
(4,4,'2024-2-20 14:04:48','2024-2-20 15:05:52',61,'A',1.4,65.4,10.4,82.4,0.4,12.4,30.4,51.4),
(5,5,'2024-2-20 14:05:48','2024-2-20 15:06:53',61,'A',1.5,65.5,10.5,82.5,0.5,12.5,30.5,51.5),
(6,6,'2024-2-20 14:06:48','2024-2-20 15:07:54',61,'A',1.6,65.6,10.6,82.6,0.6,12.6,30.6,51.6),
(7,7,'2024-2-20 14:07:48','2024-2-20 15:08:55',61,'M',1.7,65.7,10.7,82.7,0.7,12.7,30.7,51.7),
(8,8,'2024-2-20 14:08:48','2024-2-20 15:09:56',61,'A',1.8,65.8,10.8,82.8,0.8,12.8,30.8,51.8),
(9,9,'2024-2-20 14:09:48','2024-2-20 15:10:57',61,'A',1.9,65.9,10.9,82.9,0.9,12.9,30.9,51.9),
(10,1,'2024-2-21 14:01:48','2024-2-21 15:02:49',61,'M',1.1,65.1,10.1,82.1,0.1,12.1,30.1,51.1),
(11,2,'2024-2-21 14:02:48','2024-2-21 15:03:50',61,'A',1.2,65.2,10.2,82.2,0.2,12.2,30.2,51.2),
(12,3,'2024-2-21 14:03:48','2024-2-21 15:04:51',61,'M',1.3,65.3,10.3,82.3,0.3,12.3,30.3,51.3),
(13,4,'2024-2-21 14:04:48','2024-2-21 15:05:52',61,'A',1.4,65.4,10.4,82.4,0.4,12.4,30.4,51.4),
(14,5,'2024-2-21 14:05:48','2024-2-21 15:06:53',61,'A',1.5,65.5,10.5,82.5,0.5,12.5,30.5,51.5),
(15,6,'2024-2-21 14:06:48','2024-2-21 15:07:54',61,'M',1.6,65.6,10.6,82.6,0.6,12.6,30.6,51.6),
(16,7,'2024-2-21 14:07:48','2024-2-21 15:08:55',61,'A',1.7,65.7,10.7,82.7,0.7,12.7,30.7,51.7),
(17,8,'2024-2-21 14:08:48','2024-2-21 15:09:56',61,'M',1.8,65.8,10.8,82.8,0.8,12.8,30.8,51.8),
(18,9,'2024-2-21 14:09:48','2024-2-21 15:10:57',61,'A',1.9,65.9,10.9,82.9,0.9,12.9,30.9,51.9),
(19,1,'2024-2-22 14:01:48','2024-2-22 15:02:49',61,'M',1.1,65.1,10.1,82.1,0.1,12.1,30.1,51.1),
(20,2,'2024-2-22 14:02:48','2024-2-22 15:03:50',61,'A',1.2,65.2,10.2,82.2,0.2,12.2,30.2,51.2),
(21,3,'2024-2-22 14:03:48','2024-2-22 15:04:51',61,'M',1.3,65.3,10.3,82.3,0.3,12.3,30.3,51.3),
(22,4,'2024-2-22 14:04:48','2024-2-22 15:05:52',61,'A',1.4,65.4,10.4,82.4,0.4,12.4,30.4,51.4),
(23,5,'2024-2-22 14:05:48','2024-2-22 15:06:53',61,'A',1.5,65.5,10.5,82.5,0.5,12.5,30.5,51.5),
(24,6,'2024-2-22 14:06:48','2024-2-22 15:07:54',61,'A',1.6,65.6,10.6,82.6,0.6,12.6,30.6,51.6),
(25,7,'2024-2-22 14:07:48','2024-2-22 15:08:55',61,'M',1.7,65.7,10.7,82.7,0.7,12.7,30.7,51.7),
(26,8,'2024-2-22 14:08:48','2024-2-22 15:09:56',61,'M',1.8,65.8,10.8,82.8,0.8,12.8,30.8,51.8),
(27,9,'2024-2-22 14:09:48','2024-2-22 15:10:57',61,'M',1.9,65.9,10.9,82.9,0.9,12.9,30.9,51.9);
UNLOCK TABLES;