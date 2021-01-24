SELECT empno,ename,sal FROM t_emp;

SELECT empno, sal*12 AS income FROM t_emp;

SELECT empno, ename FROM t_emp LIMIT 10,5;

SELECT empno, ename, sal FROM t_emp ORDER BY sal DESC;

SELECT empno, ename, sal, hiredate FROM t_emp ORDER BY ename;

SELECT empno, ename, sal, hiredate FROM t_emp ORDER BY sal DESC, hiredate;

SELECT empno, ename, deptno, sal, hiredate FROM t_emp ORDER BY deptno, sal DESC;

SELECT empno, ename, deptno, sal, hiredate FROM t_emp ORDER BY sal DESC LIMIT 5;

SELECT job FROM t_emp;
SELECT DISTINCT job FROM t_emp;
SELECT DISTINCT job, ename FROM t_emp;


SELECT empno, deptno, ename, sal FROM t_emp WHERE (deptno = 10 OR deptno = 20) AND sal >= 2000;

SELECT empno, ename, sal, hiredate FROM t_emp WHERE deptno=10 AND (sal + IFNULL(comm,0))*12 >= 15000 AND DATEDIFF(NOW(),hiredate)/365 >= 20;

SELECT empno, ename, sal, hiredate FROM t_emp WHERE deptno IN(10,20,30) AND job != 'SALESMAN' AND hiredate < '1985-01-01';

SELECT empno, ename, sal, hiredate, comm FROM t_emp WHERE comm IS NOT NULL;
SELECT empno, ename, sal, hiredate, comm FROM t_emp WHERE comm IS NULL AND sal BETWEEN 2000 AND 3000 AND ename LIKE '%A%';
SELECT empno, ename, sal, hiredate, comm FROM t_emp WHERE comm IS NULL AND sal BETWEEN 2000 AND 3000 AND ename LIKE '_LAKE';
SELECT empno, ename, sal, hiredate, comm FROM t_emp WHERE comm IS NOT NULL AND sal BETWEEN 1000 AND 3000 AND ename REGEXP '^[\\u4e00-\\u9fa5]{2,4}$';

SELECT empno, ename, sal, hiredate, comm, deptno FROM t_emp WHERE deptno NOT IN (10,20);
SELECT empno, ename, sal, hiredate, comm, deptno FROM t_emp WHERE deptno NOT IN (10,20) XOR sal >= 2000;
SELECT 3 & 7;