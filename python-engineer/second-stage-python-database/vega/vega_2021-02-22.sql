# ************************************************************
# Sequel Pro SQL dump
# Version 5446
#
# https://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 8.0.22)
# Database: vega
# Generation Time: 2021-02-21 18:43:16 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table t_news
# ------------------------------------------------------------

DROP TABLE IF EXISTS `t_news`;

CREATE TABLE `t_news` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(40) NOT NULL,
  `editor_id` int unsigned NOT NULL,
  `type_id` int unsigned NOT NULL,
  `content_id` char(12) NOT NULL,
  `is_top` tinyint unsigned NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `state` enum('草稿','待审批','已审批','隐藏') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `editor_id` (`editor_id`),
  KEY `type_id` (`type_id`),
  KEY `state` (`state`),
  KEY `create_time` (`create_time`),
  KEY `is_top` (`is_top`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `t_news` WRITE;
/*!40000 ALTER TABLE `t_news` DISABLE KEYS */;

INSERT INTO `t_news` (`id`, `title`, `editor_id`, `type_id`, `content_id`, `is_top`, `create_time`, `update_time`, `state`)
VALUES
	(1,'美国“毅力号”探测器着陆火星 寻找生命痕迹',2,1,'',0,'2021-02-20 08:20:17','2021-02-20 08:20:17','待审批'),
	(2,'新冠疫情下上升的自杀率：日本在为世界敲响警钟吗？',2,1,'',0,'2021-02-20 08:20:50','2021-02-20 08:20:50','待审批'),
	(3,'美国得州大停电：“我穿上了北极御寒服睡觉”',2,1,'',0,'2021-02-20 08:21:15','2021-02-20 08:21:15','待审批'),
	(4,'世界首富打官司：亚马逊和亚洲首富对簿公堂背后的是非曲直',2,1,'',0,'2021-02-20 09:07:06','2021-02-20 09:07:06','待审批'),
	(5,'脸书禁止澳洲用户分享新闻网站连结 科技巨头分享营利争议升温',2,1,'',0,'2021-02-20 09:07:26','2021-02-20 09:07:26','待审批'),
	(6,'美国起诉三名朝鲜人意图盗窃13亿美元',2,1,'',0,'2021-02-20 09:07:37','2021-02-20 09:07:37','待审批'),
	(7,'中国人工降雨雪：控制天气的雄心和邻国的担忧',2,1,'',0,'2021-02-20 09:07:55','2021-02-20 09:07:55','待审批'),
	(8,'脱北者抵达韩国后会发生什么？',2,1,'',0,'2021-02-20 09:08:04','2021-02-20 09:08:04','待审批'),
	(9,'英国议员就中国投资进入英国国防产业供应链发出警告',2,1,'',0,'2021-02-20 09:08:15','2021-02-20 09:08:15','待审批'),
	(10,'玛丽·安宁：一个女性古生物学家为何被历史遗忘？',2,1,'',0,'2021-02-20 09:08:33','2021-02-20 09:08:33','待审批'),
	(11,'酒店隔离生活是怎样的？香港与悉尼两位旅客的对照',2,1,'',0,'2021-02-20 09:09:17','2021-02-20 09:09:17','待审批'),
	(12,'为什么媒体都在向布兰妮道歉？',2,1,'',0,'2021-02-20 09:09:27','2021-02-20 09:09:27','待审批'),
	(13,'缅甸政变：昂山素季被追加新指控 军方再承诺“不会长期掌权”',2,1,'',0,'2021-02-20 09:09:36','2021-02-20 09:09:36','待审批'),
	(14,'史上首富：盛世王朝的繁荣和衰败',2,1,'',0,'2021-02-20 09:09:48','2021-02-20 09:09:48','待审批'),
	(15,'非洲埃博拉疫情 本次爆发有多严重？',2,1,'',0,'2021-02-20 09:09:58','2021-02-20 09:09:58','待审批'),
	(16,'世贸组织总干事选举产生 应对新冠冲击为当务之急',2,1,'',0,'2021-02-20 09:10:11','2021-02-20 09:10:11','待审批'),
	(17,'弹劾特朗普案被参议院否决 对美国，特朗普和拜登意味着什么？',2,1,'',0,'2021-02-20 09:10:22','2021-02-20 09:10:22','待审批'),
	(18,'肺炎疫情中反思环境与人类命运：专访中国艺术家蔡国强',2,1,'',0,'2021-02-20 09:10:33','2021-02-20 09:10:33','待审批'),
	(19,'英国脱欧：英国现在已有哪些双边贸易协议',2,1,'',0,'2021-02-20 09:10:42','2021-02-20 09:10:42','待审批'),
	(20,'新冠疫情下英国人不一样的情人节',2,1,'',0,'2021-02-20 09:10:51','2021-02-20 09:10:51','待审批'),
	(21,'特朗普弹劾案落幕 美国参议院否决，特朗普：“爱国运动才刚开始”',2,1,'',0,'2021-02-20 09:11:05','2021-02-20 09:11:05','待审批'),
	(22,'China Mac：从谋杀未遂犯蜕变为反歧视领袖的华裔饶舌歌手',2,1,'',0,'2021-02-20 09:11:16','2021-02-20 09:11:16','待审批'),
	(23,'日本苍龙撞香港货船：暗流汹涌的亚太水下角力',2,1,'',0,'2021-02-20 09:11:27','2021-02-20 09:11:27','待审批'),
	(24,'特朗普弹劾案进展：你需要了解的五个关键问题',2,1,'',0,'2021-02-20 09:11:37','2021-02-20 09:11:37','待审批'),
	(25,'缅甸反政变示威者围堵中国使馆 北京否认帮忙建“防火墙”',2,1,'',0,'2021-02-20 09:11:52','2021-02-20 09:11:52','待审批'),
	(27,'朝鲜绑架日本人事件：四十多年的相思苦和漫漫寻亲路',2,1,'',0,'2021-02-20 09:12:18','2021-02-20 09:12:18','待审批'),
	(28,'特朗普弹劾案：首度公开监控画面，重现国会骚乱场景',2,1,'',0,'2021-02-20 09:12:26','2021-02-20 09:12:26','待审批'),
	(29,'泰国蝙蝠携带冠状病毒 科学家推测可能遍及亚洲各地',2,1,'',0,'2021-02-20 09:12:39','2021-02-20 09:12:39','待审批'),
	(30,'俄罗斯疫苗“卫星五号”——从备受质疑到外交推手',2,1,'',0,'2021-02-20 09:12:50','2021-02-20 09:12:50','待审批'),
	(31,'气候变化：英国煤矿史和新开煤矿的争议',2,1,'',0,'2021-02-20 09:13:01','2021-02-20 09:13:01','已审批'),
	(32,'火星探测：三位地球来客同时抵达 各有什么使命',2,1,'',0,'2021-02-20 09:13:26','2021-02-20 09:13:26','已审批');

/*!40000 ALTER TABLE `t_news` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table t_role
# ------------------------------------------------------------

DROP TABLE IF EXISTS `t_role`;

CREATE TABLE `t_role` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `role` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `role` (`role`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `t_role` WRITE;
/*!40000 ALTER TABLE `t_role` DISABLE KEYS */;

INSERT INTO `t_role` (`id`, `role`)
VALUES
	(2,'新闻编辑'),
	(1,'管理员');

/*!40000 ALTER TABLE `t_role` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table t_type
# ------------------------------------------------------------

DROP TABLE IF EXISTS `t_type`;

CREATE TABLE `t_type` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `t_type` WRITE;
/*!40000 ALTER TABLE `t_type` DISABLE KEYS */;

INSERT INTO `t_type` (`id`, `type`)
VALUES
	(2,'体育'),
	(5,'历史'),
	(4,'娱乐'),
	(3,'科技'),
	(1,'要闻');

/*!40000 ALTER TABLE `t_type` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table t_user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `t_user`;

CREATE TABLE `t_user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(500) NOT NULL,
  `email` varchar(100) NOT NULL,
  `role_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  KEY `username_2` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `t_user` WRITE;
/*!40000 ALTER TABLE `t_user` DISABLE KEYS */;

INSERT INTO `t_user` (`id`, `username`, `password`, `email`, `role_id`)
VALUES
	(1,'admin','3E6BC27A781F0AC08BCFD78CC3DCE4CA','admin@gmail.com',1),
	(2,'scott','3E6BC27A781F0AC08BCFD78CC3DCE4CA','scott@gmail.com',2),
	(3,'Frank','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Frank@gmail.com',1),
	(4,'Genevieve','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Genevieve@gmail.com',2),
	(5,'Sapphire','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Sapphire@gmail.com',2),
	(6,'Chief','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Chief@gmail.com',2),
	(7,'Forest','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Forest@gmail.com',2),
	(8,'Eric','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Eric@gmail.com',2),
	(9,'Blooming','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Blooming@gmail.com',2),
	(10,'Stewart','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Stewart@gmail.com',2),
	(11,'Fergus','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Fergus@gmail.com',2),
	(12,'Polly','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Polly@gmail.com',2),
	(13,'Seth','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Seth@gmail.com',2),
	(14,'Idelle','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Idelle@gmail.com',2),
	(15,'Delightful','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Delightful@gmail.com',2),
	(16,'Lorelei','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Lorelei@gmail.com',2),
	(17,'Queenie','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Queenie@gmail.com',2),
	(18,'Jesse','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Jesse@gmail.com',2),
	(19,'Simona','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Simona@gmail.com',2),
	(20,'Britney','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Britney@gmail.com',2),
	(21,'Henry','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Henry@gmail.com',2),
	(22,'Warlike','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Warlike@gmail.com',2),
	(23,'Ernestine','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Ernestine@gmail.com',2),
	(24,'Grover','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Grover@gmail.com',2),
	(25,'Land','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Land@gmail.com',2),
	(26,'Edith','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Edith@gmail.com',2),
	(27,'Ivory','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Ivory@gmail.com',2),
	(28,'Leslie','3E6BC27A781F0AC08BCFD78CC3DCE4CA','Leslie@gmail.com',2);

/*!40000 ALTER TABLE `t_user` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
