USE demo;

SELECT * FROM t_emp;

SELECT AVG(sal+IFNULL(comm,0)) FROM t_emp;

SELECT SUM(sal) FROM t_emp WHERE deptno IN(10,20);

SELECT MAX(comm) FROM t_emp;

SELECT MAX(sal+IFNULL(comm,0)) FROM t_emp WHERE deptno IN(10,20);

SELECT MAX(LENGTH(ename)) FROM t_emp;

SELECT MIN(empno), MIN(hiredate) FROM t_emp;

SELECT COUNT(*), COUNT(comm) FROM t_emp;

SELECT COUNT(*) FROM t_emp WHERE deptno IN(10,20) AND sal >= 2000 AND DATEDIFF(NOW(),hiredate)/365 >=15;

-- ROUND() 四舍五入取整数
SELECT deptno, ROUND(AVG(sal)) AS deptno_avg FROM t_emp GROUP BY deptno ORDER BY deptno;

SELECT deptno, job, COUNT(*) AS job_count, AVG(sal) AS sal_avg FROM t_emp GROUP BY deptno, job ORDER BY deptno ASC;

-- WITH ROLLUP 对聚合函数的执行结果再次执行同样聚合函数的统计
SELECT deptno, COUNT(*), AVG(sal), MAX(sal), MIN(sal) FROM t_emp GROUP BY deptno WITH ROLLUP;

-- GROUP_CONCAT 函数可以把分组查询中的某个字段拼成一个以逗号分隔开的字符串
SELECT deptno, GROUP_CONCAT(ename), COUNT(*) FROM t_emp WHERE sal >= 2000 GROUP BY deptno;