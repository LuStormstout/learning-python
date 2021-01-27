CREATE DATABASE vega;
USE vega;

-- 创建新闻类型表
CREATE TABLE t_type(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	type VARCHAR(20) NOT NULL UNIQUE
);
INSERT INTO t_type(type) VALUES("要闻"), ("体育"), ("科技"), ("娱乐"), ("历史");

-- 创建角色表
CREATE TABLE t_role(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	role VARCHAR(20) NOT NULL UNIQUE
);
INSERT INTO t_role(role) VALUES("管理员"), ("新闻编辑");

-- 创建用户表
-- MySQL 数据库提供的 AES 加密和解密函数
-- AES_ENCRYPT(原始数据,密匙字符串) AES 加密
-- AES_DECRYPT(加密结果,密匙字符串) AES 解密
-- HEX(N_or_S) 二进制转换成十六进制
-- UNHEX(str) 十六进制转换成二进制

-- SELECT AES_ENCRYPT("你好世界","ABC123456");
-- SELECT HEX(AES_ENCRYPT("你好世界","ABC123456"));
-- SELECT AES_DECRYPT(UNHEX("E85A104B6142A7375E53C0545CAD48EE"),"ABC123456");

CREATE TABLE t_user(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR(20) NOT NULL UNIQUE,
	password VARCHAR(500) NOT NULL,
	email VARCHAR(100) NOT NULL UNIQUE,
	role_id INT UNSIGNED NOT NULL,
	INDEX(username)
);
INSERT INTO t_user(username, password, email, role_id) VALUES("admin", HEX(AES_ENCRYPT("123456","HelloWorld")), "admin@gmail.com", 1);
INSERT INTO t_user(username, password, email, role_id) VALUES("scott", HEX(AES_ENCRYPT("123456","HelloWorld")), "scott@gmail.com", 2);

-- 创建新闻表
-- 对应的新闻内容将存放在 MongoDB 中，用 content_id 来关联。
CREATE TABLE t_news(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	title VARCHAR(40) NOT NULL,
	editor_id INT UNSIGNED NOT NULL,
	type_id INT UNSIGNED NOT NULL,
	content_id CHAR(12) NOT NULL,
	is_top TINYINT UNSIGNED NOT NULL,
	create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	state ENUM("草稿", "待审批", "已审批", "隐藏") NOT NULL,
	INDEX(editor_id),
	INDEX(type_id),
	INDEX(state),
	INDEX(create_time),
	INDEX(is_top)
);