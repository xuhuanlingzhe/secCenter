/*
SQLyog Ultimate v13.1.1 (64 bit)
MySQL - 5.1.73 : Database - sec_db
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`sec_db` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `sec_db`;

/*Table structure for table `asset_domains` */

DROP TABLE IF EXISTS `asset_domains`;

CREATE TABLE `asset_domains` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `reg_email` varchar(64) DEFAULT NULL,
  `etime` date DEFAULT NULL,
  `tmp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_domains_person` */

DROP TABLE IF EXISTS `asset_domains_person`;

CREATE TABLE `asset_domains_person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(64) NOT NULL,
  `name` varchar(64) DEFAULT NULL,
  `usage` varchar(256) DEFAULT NULL,
  `yf_person` varchar(32) DEFAULT NULL,
  `cp_person` varchar(32) DEFAULT NULL,
  `sy_person` varchar(32) DEFAULT NULL,
  `other` text,
  `last_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_hosts` */

DROP TABLE IF EXISTS `asset_hosts`;

CREATE TABLE `asset_hosts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) CHARACTER SET latin1 NOT NULL,
  `hostname` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `os` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `dev_type` int(11) DEFAULT '0' COMMENT '0-server,1-netdev,2-secdev,3-other',
  `asset_value` int(11) DEFAULT '0' COMMENT '资产价值',
  `vul_sum` int(11) DEFAULT '0' COMMENT '漏洞总数',
  `alert_sum` int(11) DEFAULT '0' COMMENT '报警总数',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=469 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_hosts1` */

DROP TABLE IF EXISTS `asset_hosts1`;

CREATE TABLE `asset_hosts1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) CHARACTER SET latin1 NOT NULL,
  `hostname` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `os` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `dev_type` int(11) DEFAULT '0' COMMENT '0-server,1-netdev,2-secdev,3-other',
  `asset_value` int(11) DEFAULT '0' COMMENT '资产价值',
  `vul_sum` int(11) DEFAULT '0' COMMENT '漏洞总数',
  `alert_sum` int(11) DEFAULT '0' COMMENT '报警总数',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=466 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_hosts2` */

DROP TABLE IF EXISTS `asset_hosts2`;

CREATE TABLE `asset_hosts2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) CHARACTER SET latin1 NOT NULL,
  `hostname` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `os` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `dev_type` int(11) DEFAULT '0' COMMENT '0-server,1-netdev,2-secdev,3-other',
  `asset_value` int(11) DEFAULT '0' COMMENT '资产价值',
  `vul_sum` int(11) DEFAULT '0' COMMENT '漏洞总数',
  `alert_sum` int(11) DEFAULT '0' COMMENT '报警总数',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=466 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_hosts3` */

DROP TABLE IF EXISTS `asset_hosts3`;

CREATE TABLE `asset_hosts3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) CHARACTER SET latin1 NOT NULL,
  `hostname` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `os` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `dev_type` int(11) DEFAULT '0' COMMENT '0-server,1-netdev,2-secdev,3-other',
  `asset_value` int(11) DEFAULT '0' COMMENT '资产价值',
  `vul_sum` int(11) DEFAULT '0' COMMENT '漏洞总数',
  `alert_sum` int(11) DEFAULT '0' COMMENT '报警总数',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=466 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_hosts4` */

DROP TABLE IF EXISTS `asset_hosts4`;

CREATE TABLE `asset_hosts4` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) CHARACTER SET latin1 NOT NULL,
  `hostname` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `os` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `dev_type` int(11) DEFAULT '0' COMMENT '0-server,1-netdev,2-secdev,3-other',
  `asset_value` int(11) DEFAULT '0' COMMENT '资产价值',
  `vul_sum` int(11) DEFAULT '0' COMMENT '漏洞总数',
  `alert_sum` int(11) DEFAULT '0' COMMENT '报警总数',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=466 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_hosts5` */

DROP TABLE IF EXISTS `asset_hosts5`;

CREATE TABLE `asset_hosts5` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) CHARACTER SET latin1 NOT NULL,
  `hostname` varchar(50) CHARACTER SET latin1 DEFAULT NULL,
  `os` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `dev_type` int(11) DEFAULT '0' COMMENT '0-server,1-netdev,2-secdev,3-other',
  `asset_value` int(11) DEFAULT '0' COMMENT '资产价值',
  `vul_sum` int(11) DEFAULT '0' COMMENT '漏洞总数',
  `alert_sum` int(11) DEFAULT '0' COMMENT '报警总数',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_iplist` */

DROP TABLE IF EXISTS `asset_iplist`;

CREATE TABLE `asset_iplist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ips` varchar(50) CHARACTER SET latin1 NOT NULL,
  `area` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_ports` */

DROP TABLE IF EXISTS `asset_ports`;

CREATE TABLE `asset_ports` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) CHARACTER SET latin1 NOT NULL,
  `port` int(11) NOT NULL,
  `stype` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `service` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `version` varchar(256) CHARACTER SET latin1 DEFAULT NULL,
  `state` varchar(50) CHARACTER SET latin1 NOT NULL,
  `protocol` varchar(50) CHARACTER SET latin1 NOT NULL,
  `tags` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4269 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_ports1` */

DROP TABLE IF EXISTS `asset_ports1`;

CREATE TABLE `asset_ports1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) CHARACTER SET latin1 NOT NULL,
  `port` int(11) NOT NULL,
  `stype` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `service` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `version` varchar(256) CHARACTER SET latin1 DEFAULT NULL,
  `state` varchar(50) CHARACTER SET latin1 NOT NULL,
  `protocol` varchar(50) CHARACTER SET latin1 NOT NULL,
  `tags` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4242 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_ports2` */

DROP TABLE IF EXISTS `asset_ports2`;

CREATE TABLE `asset_ports2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) CHARACTER SET latin1 NOT NULL,
  `port` int(11) NOT NULL,
  `stype` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `service` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `version` varchar(256) CHARACTER SET latin1 DEFAULT NULL,
  `state` varchar(50) CHARACTER SET latin1 NOT NULL,
  `protocol` varchar(50) CHARACTER SET latin1 NOT NULL,
  `tags` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4258 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_ports3` */

DROP TABLE IF EXISTS `asset_ports3`;

CREATE TABLE `asset_ports3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) CHARACTER SET latin1 NOT NULL,
  `port` int(11) NOT NULL,
  `stype` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `service` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `version` varchar(256) CHARACTER SET latin1 DEFAULT NULL,
  `state` varchar(50) CHARACTER SET latin1 NOT NULL,
  `protocol` varchar(50) CHARACTER SET latin1 NOT NULL,
  `tags` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4248 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_ports4` */

DROP TABLE IF EXISTS `asset_ports4`;

CREATE TABLE `asset_ports4` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) CHARACTER SET latin1 NOT NULL,
  `port` int(11) NOT NULL,
  `stype` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `service` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `version` varchar(256) CHARACTER SET latin1 DEFAULT NULL,
  `state` varchar(50) CHARACTER SET latin1 NOT NULL,
  `protocol` varchar(50) CHARACTER SET latin1 NOT NULL,
  `tags` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4202 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_ports5` */

DROP TABLE IF EXISTS `asset_ports5`;

CREATE TABLE `asset_ports5` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(15) CHARACTER SET latin1 NOT NULL,
  `port` int(11) NOT NULL,
  `stype` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `service` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `version` varchar(256) CHARACTER SET latin1 DEFAULT NULL,
  `state` varchar(50) CHARACTER SET latin1 NOT NULL,
  `protocol` varchar(50) CHARACTER SET latin1 NOT NULL,
  `tags` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_sslinfo` */

DROP TABLE IF EXISTS `asset_sslinfo`;

CREATE TABLE `asset_sslinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(64) DEFAULT NULL,
  `ip` varchar(128) DEFAULT NULL,
  `state` tinyint(1) DEFAULT NULL,
  `ctime` datetime DEFAULT NULL,
  `ssl_info` varchar(2046) DEFAULT NULL,
  `ssl_etime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=410 DEFAULT CHARSET=utf8;

/*Table structure for table `asset_tags` */

DROP TABLE IF EXISTS `asset_tags`;

CREATE TABLE `asset_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `tag` varchar(128) DEFAULT NULL,
  `num` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `vul_list` */

DROP TABLE IF EXISTS `vul_list`;

CREATE TABLE `vul_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(128) DEFAULT NULL COMMENT '应用名称',
  `vul_name` varchar(128) NOT NULL COMMENT '漏洞名称',
  `ip_adr` varchar(128) NOT NULL COMMENT '漏洞地址（IP或域名或URL）',
  `vul_level` int(11) DEFAULT '1' COMMENT '1高危2中危3低危',
  `vul_desc` text COMMENT '漏洞描述',
  `vul_state` int(11) DEFAULT '1' COMMENT '1尚未修复2正在修复3已经修复4忽略',
  `vul_solution` text COMMENT '解决方案',
  `vul_result` varchar(64) DEFAULT NULL,
  `vul_time` datetime DEFAULT NULL COMMENT '漏洞发现时间',
  `vul_hash` varchar(32) NOT NULL COMMENT '漏洞唯一hash',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `waf_servers` */

DROP TABLE IF EXISTS `waf_servers`;

CREATE TABLE `waf_servers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `ip` varchar(16) DEFAULT NULL,
  `version` varchar(30) DEFAULT NULL,
  `state` int(5) DEFAULT '1',
  `master` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Table structure for table `waf_servers_copy` */

DROP TABLE IF EXISTS `waf_servers_copy`;

CREATE TABLE `waf_servers_copy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `ip` varchar(16) DEFAULT NULL,
  `version` varchar(30) DEFAULT NULL,
  `state` int(5) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Table structure for table `waf_sites` */

DROP TABLE IF EXISTS `waf_sites`;

CREATE TABLE `waf_sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(256) NOT NULL,
  `ip` varchar(512) NOT NULL,
  `http` tinyint(1) DEFAULT '1',
  `https` tinyint(1) DEFAULT '0',
  `state` tinyint(1) DEFAULT '1',
  `cc` tinyint(1) DEFAULT '0',
  `last_attack_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_attack_type` varchar(128) DEFAULT NULL,
  `attack_sum` int(11) DEFAULT '0',
  `create_time` datetime DEFAULT NULL,
  `last_update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
