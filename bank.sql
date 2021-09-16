/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.6.24 : Database - bank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bank` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;

USE `bank`;

/*Table structure for table `bank_user` */

DROP TABLE IF EXISTS `bank_user`;

CREATE TABLE `bank_user` (
  `account` varchar(8) COLLATE utf8_bin DEFAULT NULL,
  `username` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `password` int(6) DEFAULT NULL,
  `country` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `province` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `street` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `door` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `money` int(20) DEFAULT NULL,
  `bank_name` varchar(20) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `bank_user` */

insert  into `bank_user`(`account`,`username`,`password`,`country`,`province`,`street`,`door`,`money`,`bank_name`) values ('53719763','sususu',123456,'qwrt','qwer','qwer','qwer',0,'狼腾测试猿银行'),('28109074','sususu',666666,'qwer','qwertyu','qwerty','007',0,'狼腾测试猿银行');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
