-- MySQL 的函数

-- 数字函数：
# ABS(X) # 绝对值
# ROUND(X) # 四舍五入
# FLOOR(X) # 强制舍位到最近的整数
# CEIL(X) # 强制进位到最近的整数
# POWER(X,Y) # 幂函数
# LOG(B,X) # 对数函数
# LN(X) # 对数函数

SELECT ABS(-100);
SELECT ROUND(3.1415926 * 100) / 100; # 四舍五入，通过 * 100 结果 / 100 来保留两位小数。
SELECT FLOOR(9.9);
SELECT CEIL(3.2);
SELECT POW(2,3);
SELECT LOG(7,3);
SELECT LN(10);

# SQRT(X) # 开平方
# PI() # 圆周率
# SIN(X) # 三角函数 正弦
# COS(X) # 三角函数 余弦
# TAN(X) # 三角函数 正切
# COT(X) # 三角函数 余切
# RADIANS(X) # 角度转换弧度
# DEGREES(X) # 弧度转换角度

SELECT SQRT(9);
SELECT PI();
SELECT SIN(RADIANS(30));
SELECT COS(RADIANS(45));
SELECT TAN(RADIANS(30));
SELECT COT(RADIANS(45));
SELECT DEGREES(1);

-- 日期函数：
# NOW() # 函数能获得系统日期与时间，格式 yyyy-MM-dd hh:mm:ss 24 小时制，数据库最小的时间单位为秒。
# CURDATE() # 函数能获得当前系统日期，格式 yyyy-MM-dd
# CURTIME() # 函数能获得当前系统时间，格式 hh:mm:ss
# DATE_FORMAT(date,format) # 函数用于格式化日期，返回用户想要的日期格式。
# -- format 格式化表达式：
# -- %Y 年份， %d 日期， %W 星期（名称）， %U 本年第几周， %h 小时（12）， %s 秒， %T 时间（24）， %m 月份， %w 星期（数字）， %j 本年第几天， %H 小时（24）， %i 分钟， %r 时间（12）
# DATE_ADD(date,INTERVAL expr unit) # 函数可以实现日期的偏移计算，而且时间单位很灵活 DATE_ADD(日期,INTERVAL 偏移量 时间单位)
# DATEDIFF(expr1,expr2) # 函数用来计算两个日期之间相差的天数 DATEDIFF(日期,日期)

SELECT NOW(), CURDATE(), CURTIME();
SELECT DATE_FORMAT(NOW(),"%Y");
SELECT DATE_FORMAT(NOW(),"%w");
-- 获取所有员工以及入职年份
SELECT ename, DATE_FORMAT(hiredate,"%Y") FROM t_emp;
-- 利用日期函数，查询明年你的生日是星期几
SELECT DATE_FORMAT("2021-05-05","%W");
-- 利用日期函数，查询 1981 年上半年入职的员工有多少人
SELECT COUNT(*) FROM t_emp WHERE DATE_FORMAT(hiredate,"%Y") = 1981 AND DATE_FORMAT(hiredate,"%m") <= 6;
-- MySQl 数据库里面，两个日期不能直接加减，日期也不能与数字加减
SELECT DATE_ADD(NOW(),INTERVAL 15 DAY); # 15 天之后
SELECT DATE_FORMAT(DATE_ADD(DATE_ADD(NOW(),INTERVAL -6 MONTH),INTERVAL -3 DAY),"%Y/%m/%d"); # 6 个月零 3 天之前

-- 字符串函数：
# LOWER(str) # 转换小写字符
# UPPER(str) # 转换大写字符
# LENGTH(str) # 字符数量
# CONCAT(str1,str2,...) # 连接字符串
# INSTR(str,substr) # 字符出现的位置
# INSERT(str,pos,len,newstr) # 插入/替换字符
# REPLACE(str,from_str,to_str) # 替换字符
# SUBSTR(str,pos,len) # 截取字符串
# SUBSTRING(str FROM pos FOR len) # 截取字符串
# LPAD(str,len,padstr) # 左侧填充字符
# RPAD(str,len,padstr) # 右侧填充字符
# TRIM([remstr FROM] str) # 去除首尾空格

SELECT LOWER(ename), UPPER(ename), LENGTH(ename), CONCAT("$",sal), INSTR(ename,"A") FROM t_emp;
SELECT INSERT("你好",1,0,"先生");
SELECT REPLACE("你好先生","先生","女士");
SELECT SUBSTR("你好世界",3,4);
SELECT SUBSTRING("你好世界",3,2);
SELECT LPAD(SUBSTRING("13312345678",8,4),11,"*");
SELECT RPAD(SUBSTRING("李晓娜",1,1),LENGTH("李晓娜")/3,"*");
SELECT TRIM("   Hello World  ");

-- 条件函数：
# IFNULL(expr1,expr2) # IFNULL(表达式,值)
# IF(expr1,expr2,expr3) # IF(表达式,值1,值2) 表达式为真返回第一个值，否则返回第二个值
-- 复杂的条件判断可以用条件语句来实现，比 IF 语句功能更强大
-- CASE
-- 	WHEN 表达式 THEN 值1
-- 	WHEN 表达式 THEN 值2
-- 	ELSE 值N
-- END;

-- 中秋节公司发放礼品，SALES 部门发放礼品 A，其余部门发放礼品 B，打印每名员工获得的礼品
SELECT e.empno, e.ename, d.dname, IF(d.dname = "SALES","礼品A","礼品B") FROM t_emp e JOIN t_dept d ON e.deptno = d.deptno;
-- 公司年庆决定组织员工集体旅游，每个部门旅游目的地是不同的。SALES 部门去 P1 地点，ACCOUNTING 部门去 P2 地点，RESEARCH 部门去 P3 地点，查询每名员工的旅游地点。
SELECT e.empno, e.ename, d.dname,
CASE
	WHEN d.dname = "SALES" THEN "P1"
	WHEN d.dname = "ACCOUNTING" THEN "P2"
	WHEN d.dname = "RESEARCH" THEN "P3"
END AS place
FROM t_emp e JOIN t_dept d ON e.deptno = d.deptno;

-- 公司决定为员工调整基本工资，具体调整方案如下
-- SALES 部门中工龄超过 20 年的涨 10%
-- SALES 部门中工龄不满 20 年的涨 5%
-- ACCOUNTING 部门的涨 300 元
-- RESEARCH 部门里低于部门平均底薪的涨 200 元
-- 没有部门的员工涨 100 元
UPDATE t_emp e
LEFT JOIN t_dept d ON e.deptno = d.deptno
LEFT JOIN (SELECT deptno, AVG(sal) AS sal_avg FROM t_emp GROUP BY deptno) t ON e.deptno = t.deptno
SET e.sal = (
	CASE
		WHEN d.dname = "SALES" AND DATEDIFF(NOW(),e.hiredate)/365 >= 20 THEN e.sal * 1.1
		WHEN d.dname = "SALES" AND DATEDIFF(NOW(),e.hiredate)/365 < 20 THEN e.sal * 1.05
		WHEN d.dname = "ACCOUNTING" THEN e.sal + 300
		WHEN d.dname = "RESEARCH" AND e.sal < t.sal_avg THEN e.sal + 200
		WHEN d.deptno IS NULL THEN e.sal + 100
		ELSE e.sal
	END
);
