-- 内连接的几种写法
-- SELECT ... FROM 表1 JOIN 表2 ON 连接条件;
-- SELECT ... FROM 表1 JOIN 表2 WHERE 连接条件;
-- SELECT ... 表1, 表2 WHERE 连接条件;

-- 查询每名员工的部门信息
SELECT e.empno, e.ename, d.dname FROM t_emp e JOIN t_dept d ON e.deptno = d.deptno;
SELECT e.empno, e.ename, d.dname FROM t_emp e JOIN t_dept d WHERE e.deptno = d.deptno;
SELECT e.empno, e.ename, d.dname FROM t_emp e, t_dept d WHERE e.deptno = d.deptno;

--  查询每个员工的工号、姓名、部门名称、底薪、职位、工资等级。
 SELECT e.empno, e.ename, d.dname, e.sal, e.job, s.grade
 FROM t_emp AS e
 JOIN t_dept AS d ON e.deptno = d.deptno
 JOIN t_salgrade AS s ON e.sal BETWEEN s.losal AND s.hisal;

-- 查询与 SCOTT 相同部门的员工都有谁
-- 子查询比较慢效率慢，用表连接代替子查询
-- 相同的数据表也是可以做表连接的
SELECT ename, deptno FROM t_emp
WHERE deptno = (SELECT deptno FROM t_emp WHERE ename = "SCOTT") AND ename != "SCOTT";

SELECT e2.ename, e2.deptno FROM t_emp AS e1 JOIN t_emp AS e2
ON e1.deptno = e2.deptno
WHERE e1.ename = "SCOTT" AND e2.ename != "SCOTT";

-- 查询底薪超过公司平均底薪的员工信息
-- 表查询的结果集也可以作为“一张表”来和其他表来做表连接
SELECT e.empno, e.ename, e.sal FROM t_emp AS e JOIN (SELECT AVG(sal) AS sal_avg FROM t_emp) AS t ON e.sal >= t.sal_avg;

-- 查询 RESEARCH 部门的人数、最高底薪、最低底薪、平均底薪、平均工龄
-- FLOOR(X)舍去小数点后的36.9=36
-- CEIL(X)强制进位 36.1=37
SELECT COUNT(*), MAX(e.sal), MIN(e.sal), AVG(e.sal), FLOOR(AVG(DATEDIFF(NOW(),e.hiredate)/365))
FROM t_emp AS e JOIN t_dept AS d ON e.deptno = d.deptno WHERE d.dname = "RESEARCH";

-- 查询每种职业的最高工资、最低工资、平均工资、最高工资等级和最低工资等级
SELECT e.job, MAX(e.sal + IFNULL(e.comm,0)), MIN(e.sal + IFNULL(e.comm,0)), AVG(e.sal + IFNULL(e.comm,0)), MAX(s.grade), MIN(s.grade)
FROM t_emp AS e JOIN t_salgrade AS s ON e.sal + IFNULL(e.comm,0) BETWEEN s.losal AND s.hisal GROUP BY e.job;

-- 查询每个底薪超过部门平均底薪的员工信息
-- 把查询的结果集当作一张表来做表连接以代替效率比较低的子查询
SELECT e.empno, e.ename, e.sal
FROM t_emp AS e JOIN (SELECT deptno, AVG(sal) AS sal_avg FROM t_emp GROUP BY deptno) AS t
ON e.deptno = t.deptno AND e.sal >= t.sal_avg;

-- 数据表的外连接
-- 左外连接就是保留左表所有的记录，与右表做连接。如果右表有符合条件的记录就与左表连接，如果右表没有符合条件的记录，就用 NULL 与左表连接。右外连接也是如此。
SELECT e.empno, e.ename, d.dname FROM t_emp AS e LEFT JOIN t_dept AS d ON e.deptno = d.deptno;
SELECT e.empno, e.ename, d.dname FROM t_dept AS d RIGHT JOIN t_emp AS e ON e.deptno = d.deptno;

-- 查询每个部门的名称和部门的人数
SELECT d.dname, COUNT(e.deptno) FROM t_dept AS d LEFT JOIN t_emp AS e ON d.deptno = e.deptno GROUP BY d.deptno;

-- 查询每个部门的名称和部门的人数，如果没有部门的员工，部门名称用 NULL 代替。
-- （查询语句） UNION （查询语句） UNION （查询语句） ......
(SELECT d.dname, COUNT(e.deptno) FROM t_dept AS d LEFT JOIN t_emp AS e ON d.deptno = e.deptno GROUP BY d.deptno)
UNION
(SELECT d.dname, COUNT(*) FROM t_dept AS d RIGHT JOIN t_emp AS e ON d.deptno = e.deptno GROUP BY d.deptno);

-- 查询每名员工的编号、姓名、部门、月薪、工资等级、工龄、上司编号、上司姓名、上司部门
SELECT e.empno, e.ename, d.dname, e.sal + IFNULL(e.comm,0), s.grade, FLOOR(DATEDIFF(NOW(),e.hiredate)/365), t.empno AS mgr_no, t.ename AS mgr_name, t.dname AS mgr_dname
FROM t_emp AS e
LEFT JOIN t_dept AS d ON e.deptno = d.deptno
LEFT JOIN t_salgrade AS s ON e.sal BETWEEN s.losal AND s.hisal
LEFT JOIN (SELECT e1.empno, e1.ename, d1.dname FROM t_emp AS e1 JOIN t_dept AS d1 ON e1.deptno = d1.deptno) AS t ON e.mgr = t.empno;

-- 内连接只保留符合条件的记录，所以查询条件写在 ON 子句和 WHERE 子句中的效果是相同的。但是外连接里，条件写在 WHERE 子句里，不符合条件的记录是会被过滤掉的，而不是保留下来。
SELECT e.deptno, e.ename, d.dname FROM t_emp e LEFT JOIN t_dept d ON e.deptno = d.deptno WHERE e.deptno = 10;
SELECT e.deptno, e.ename, d.dname FROM t_emp e LEFT JOIN t_dept d ON e.deptno = d.deptno AND e.deptno = 10;