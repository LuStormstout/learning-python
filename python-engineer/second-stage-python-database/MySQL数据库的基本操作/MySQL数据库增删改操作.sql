-- INSERT 语句
-- INSERT INTO 表名(字段1, 字段2, ...) VALUES(值1, 值2, ...);
-- INSERT INTO 表名(字段1, 字段2, ...) VALUES(值1, 值2, ...), (值1, 值2, ...), ...;
-- INSERT INTO tbl_name VALUES(expr, expr)
-- 不写对应的字段执行效率会受到影响

INSERT INTO t_dept(deptno, dname, loc) VALUES(50, "技术部", "北京");
INSERT INTO t_dept(deptno, dname, loc) VALUES(60, "后勤部", "北京"), (70, "保安部", "北京");

-- 向技术部添加一条员工信息
INSERT INTO t_emp(empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES(8001, "刘娜", "SALESMAN", 8000, "1988-12-20", 2000, NULL, (SELECT deptno FROM t_dept WHERE dname = "技术部"));

-- MySQL INSERT 语句方言
-- INSERT INTO 表名 SET 字段1=值1, 字段2=值2, ...;
-- INTO 省略了也是可以运行的
INSERT INTO t_emp SET empno=8002, ename="JACK", job="SALESMAN", mgr=8000, hiredate="1985-03-14", sal=2500, comm=NULL, deptno=50;
DELETE FROM t_emp WHERE empno = 8002;
INSERT t_emp SET empno=8002, ename="JACK", job="SALESMAN", mgr=8000, hiredate="1985-03-14", sal=2500, comm=NULL, deptno=50;

-- IGNORE 关键字会让 INSERT 只插入数据库不存在的记录
-- INSERT [IGNORE] INTO 表名 ...;
INSERT IGNORE INTO t_dept(deptno, dname, loc) VALUES(70, "A", "北京"), (80, "B", "上海");

-- UPDATE 语句用于修改表的记录
-- UPDATE [IGNORE] 表名 SET 字段1=值1, 字段2=值2, ...
-- [WHERE 条件1 ...]
-- [ORDER BY ...]
-- [LIMIT ...];
-- 执行顺序 UPDATE > WHERE > ORDER BY > LIMIT > SET
-- UPDATE table_reference SET col_name1=expr1 WHERE where_condition

-- 把每个员工和上司的编号都 +1, 用 ORDER BY 子句完成
UPDATE t_emp SET empno=empno+1, mgr=mgr+1 ORDER BY empno DESC;

-- 把月收入前三名的员工底薪减 100 元，用 LIMIT 子句完成
UPDATE t_emp SET sal=sal-100 ORDER BY sal+IFNULL(comm,0) LIMIT 3;

-- 把 10 部门中，工龄超过 20 年的员工，底薪增加 200 元
UPDATE t_emp SET sal=sal+200 WHERE FLOOR(DATEDIFF(NOW(),hiredate)/365) > 20;

-- 把 ALLEN 掉往 RESEARCH 部门，职务调整为 ANALYST
-- UPDATE 表1 JOIN 表2 ON 条件 SET 字段1 = 值1, 字段2 = 值2, ...;
-- 表连接的 UPDATE 语句可以修改多张表的记录
-- UPDATE 语句的表连接可以演变成下面的样子
-- UPDATE 表1, 表2 SET 字段1 = 值1, 字段2 = 值2, ... WHERE 连接条件;
UPDATE t_emp e JOIN t_dept d SET e.deptno = d.deptno, e.job = "ANALYST", d.loc = "北京" WHERE e.ename = "ALLEN" AND d.dname = "RESEARCH";

-- 把底薪低于公司平均底薪的员工，底薪增加 150 元
UPDATE t_emp e JOIN (SELECT AVG(sal) AS sal_avg FROM t_emp) t ON e.sal < t.sal_avg SET e.sal = e.sal + 150;

-- UPDATE 语句的表连接即可以是内连接，又可以是外连接
-- UPDATE 表1 [LEFT | RIGHT] JOIN 表2 ON 条件 SET 字段1 = 值1, 字段2 = 值2, ...;
-- 把没有部门的员工，或者 SALES 部门低于 2000 元底薪的员工，都调往 20 部门
UPDATE t_emp e LEFT JOIN t_dept d ON e.deptno = d.deptno SET e.deptno = 20 WHERE e.deptno IS NULL OR (d.dname = "SALES" AND e.sal < 2000);


-- DELETE 语句用于删除记录，语法如下
-- DELETE [IGNORE] FROM 表名 [WHERE 条件1, 条件2, ...] [ORDER BY ...] [LIMIT ...];
-- 执行顺序 FROM > WHERE > ORDER BY > LIMIT > DELETE
-- 删除 10 部门中，工龄超过 20 年的员工记录
DELETE FROM t_emp WHERE deptno = 10 AND DATEDIFF(NOW(),hiredate)/365 >=20;

-- 删除 20 部门中工资最高的员工记录
DELETE FROM t_emp WHERE deptno = 20 ORDER BY sal + IFNULL(comm,0) DESC LIMIT 1;

-- 删除 SALES 部门和该部门的全部员工记录
-- 因为相关子查询效率非常低，所以我们可以用表连接的方式改造 DELETE 语句
-- DELETE 表1, ... FROM 表1 JOIN 表2 ON 条件 [WHERE 条件1, 条件2, ...] [ORDER BY ...] [LIMIT ...];
DELETE e,d FROM t_emp e JOIN t_dept d ON e.deptno = d.deptno WHERE d.dname = "SALES";

-- 删除每个低于部门平均底薪的员工记录
DELETE e FROM t_emp e JOIN (SELECT deptno, AVG(sal) AS sal_avg FROM t_emp GROUP BY deptno) t ON e.deptno = t.deptno AND e.sal < t.sal_avg;

-- 删除员工 KING 和他的直接下属的员工记录，用表连接实现
DELETE e FROM t_emp e JOIN (SELECT empno FROM t_emp WHERE ename = "KING") t ON e.mgr = t.empno OR e.empno = t.empno;

-- DELETE 语句的表连接即可以是内连接，又可以是外连接
-- DELETE 表1, ... FROM 表1 [LEFT | RIGHT] JOIN 表2 ON 条件 ...;
-- 删除 SALES 部门的员工，以及没有部门的员工
DELETE e FROM t_emp e LEFT JOIN t_dept d ON e.deptno = d.deptno WHERE d.dname = "SALES" OR e.deptno IS NULL;

-- 快速删除数据表的全部记录
-- DELETE 语句是在事物机制下删除记录，删除记录之前，先把将要删除的记录保存到日志文件里，然后再删除记录。
-- TRUNCATE 语句在事物机制之外删除记录，速度远超过 DELETE 语句
-- TRUNCATE TABLE 表名;
TRUNCATE TABLE t_emp;