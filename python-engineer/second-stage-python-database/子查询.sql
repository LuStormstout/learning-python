-- 子查询可以写在三个地方：WHERE 子句、FROM 子句、SELECT 子句，但是只有 FROM 子句子查询是最可取的
-- 只推荐使用 FROM 子句的子查询，只会执行一次，所以效率很高
-- WHERE 子句的子查询不推荐使用，效率很低的子查询，使用连接查询代替
-- SELECT 子查询每一条记录就要执行一次，查询效率很低，不推荐使用
-- 查询底薪超过公司平均底薪的员工信息
-- WHERE 子查询
SELECT empno, ename, sal FROM t_emp WHERE sal >= (SELECT AVG(sal) FROM t_emp);

-- SELECT 子句子查询
SELECT e.empno, e.ename, (SELECT dname FROM t_dept WHERE deptno = e.deptno) FROM t_emp e;

-- FROM 子句子查询
SELECT e.empno, e.ename, e.sal, t.sal_avg FROM t_emp e
JOIN (SELECT deptno, AVG(sal) as sal_avg FROM t_emp GROUP BY deptno) t
ON e.deptno = t.deptno AND e.sal >= t.sal_avg

-- 单行子查询和多行子查询
-- 单行子查询的结果集只有一条记录，多行子查询的结果集有多行记录。
-- 多行子查询只能出现在 WHERE 子句和 FROM 子句中

-- 如何用子查询查找 FORD 和 MARTIN 两个人的同事
SELECT ename, deptno FROM t_emp
WHERE deptno IN (SELECT deptno FROM t_emp WHERE ename IN("FORD", "MARTIN"))
AND ename NOT IN("FORD", "MARTIN") ORDER BY deptno;

-- WHERE 子句中，可以使用 IN、ALL、ANY、EXISTS 关键字来处理多行表达式结果集的条件判断
-- 查询比 FORD 和 MARTIN 底薪都高的员工信息
SELECT ename, sal FROM t_emp WHERE sal >= ALL (SELECT sal FROM t_emp WHERE ename IN("FORD", "MARTIN"))
AND ename NOT IN("FORD", "MARTIN") ORDER BY deptno;

-- EXISTS 关键字是把原来在子查询之外的条件判断，写到了子查询的里面
-- SELECT ... FROM 表名 WHERE [NOT] EXISTS(子查询);
-- 查询工资等级是 3 或者是 4 的员工信息
SELECT empno, ename, sal FROM t_emp WHERE EXISTS(SELECT grade FROM t_salgrade WHERE sal BETWEEN losal AND hisal AND grade IN(3,4));