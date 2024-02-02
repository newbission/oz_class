USE classicmodels;

### 기본 조회 및 필터링 ###
# 고객 목록 조회
-- SELECT * FROM customers;

# 특정 제품 라인의 제품 조회: 'Classic Cars' 제품 라인에 속하는 모든 제품의 이름과 가격을 조회하세요.
-- SELECT productName, buyPrice FROM products WHERE productLine = 'Classic Cars';

# 최근 주문: 가장 최근에 ㅈ주문된 10개의 주문을 주문 날짜(orderDate)와 함께 조회하세요
-- SELECT * FROM orders 
-- ORDER BY orderDate DESC
-- LIMIT 10;

# 최소 금액 이상의 결제: 100달러 이상 결제된 거래(amount)만 조회하세요.
-- SELECT * FROM payments WHERE amount >= 100;

### 조인 쿼리 ###
# 주문과 고객 정보 조합: 
# 각 주문에 대한 주문 번호(orders-orderNumber)와 주문한 고객(customers-customerName)의 이름을 조회하세요.
-- SELECT o.orderNumber, c.customerName FROM orders o
-- JOIN customers c ON o.customerNumber = c.customerNumber

# 제품과 제품 라인 결합: 
# 각 제품의 이름(products-productName)과 속한 제품 라인의 설명(productlines-textDescription)을 조회하세요.
-- SELECT p.productName, pl.textDescription FROM products p
-- JOIN productlines pl ON p.productLine = pl.productLine;

# 직원과 상사 정보: 각 직원의 이름과 직속 상사의 이름을 조회하세요.
-- SELECT e.lastName, e.firstName, m.lastName AS 'ManagerLastName', m.firstName AS 'ManagerFirstName'
-- FROM employees e JOIN employees m ON e.reportsTo = m.employeeNumber;

# 특정 사무실의 직원 목록: 'San Francisco' 사무실에서 근무하는 모든 직원의 이름을 조회하세요.
# employees.officeCode, offices.officeCode, offices.city
-- SELECT e.firstName, e.lastName FROM employees e
-- JOIN offices o ON e.officeCode = o.officeCode WHERE o.city = 'San Francisco';

### 그룹 쿼리 ###
# 제품 라인별 제품 수: 각 제품 라인에 속한 제품의 수를 조회하세요.
-- SELECT productLine, COUNT(*) FROM products
-- GROUP BY productLine;

# 고객별 총 주문 금액: 각 고객별로 총 주문 금액을 계산하세요.
-- SELECT customerNumber, SUM(amount) FROM payments
-- GROUP BY customerNumber;

# 가장 많이 팔린 제품: 가장 많이 판매된 제품의 이름과 판매 수량을 조회하세요.
-- SELECT p.productName, SUM(od.quantityOrdered) as OrderAmount FROM products p
-- JOIN orderdetails od ON p.productCode = od.productCode
-- GROUP BY productName ORDER BY OrderAmount DESC LIMIT 1;

# 매출이 가장 높은 사무실: 가장 많은 매출을 기록한 사무실의 위치와 매출액을 조회하세요.
-- SELECT o.city, SUM(p.amount) as totalSales FROM customers c
-- JOIN payments p ON c.customerNumber = p.customerNumber
-- JOIN employees e ON e.employeeNumber = c.salesRepEmployeeNumber
-- JOIN offices o ON o.officeCode = e.officeCode
-- GROUP BY o.city ORDER BY totalSales DESC LIMIT 1;

### 서브 쿼리 ###
# 특정 금액 이상의 주문: 50000달러 이상의 총 주문 금액을 기록한 주문들을 조회하세요.
-- SELECT orderNumber, sum(quantityOrdered * priceEach) AS total
-- FROM orderdetails
-- GROUP BY orderNumber
-- HAVING total >= 50000;

# 평균 이상 결제 고객: 평균 결제 금액보다 많은 금액을 결제한 고객들의 목록을 조회하세요.
-- SELECT customerNumber, SUM(amount) as total FROM payments
-- GROUP BY customerNumber
-- HAVING total > (SELECT AVG(amount) FROM payments);

# 주문 없는 고객: 아직 주문을 하지 않은 고객의 목록을 조회하세요.
-- SELECT customerName FROM customers
-- WHERE customerNumber NOT IN (SELECT customerNumber FROM orders);

# 최대 매출 고객: 가장 많은 금액을 지불한 고객의 이름과 총 결제 금액을 조회하세요.
-- SELECT c.customerName, SUM(od.quantityOrdered * od.priceEach) AS total FROM customers c
-- JOIN orders o ON c.customerNumber = o.customerNumber
-- JOIN orderdetails od ON o.orderNumber = od.orderNumber
-- GROUP BY c.customerName ORDER BY total DESC LIMIT 1;

### 데이터 수정 및 관리 ###
#신규 고객 추가: 'customers' 테이블에 새로운 고객을 추가하는 쿼리를 작성하세요.
-- 'customers'테이블의 costomerNumber가 AI가 아님
-- INSERT INTO customers 
-- VALUES(498, 'New Customer', 'New Last Name', 'New First Name',
-- '+81 10 1123-3094',  'New Address1', 'New Address2',
-- 'New City', 'New State', '11023', 'Korea', 1188, 123456.00);
		
# 제품 가격 변경: 'Classic Cars' 제품 라인의 모든 제품 가격을 10% 인상하는 쿼리를 작성하세요.
-- UPDATE products SET buyPrice = buyPrice * 1.1 WHERE productLine = 'Classic Cars';

# 고객 데이터 업데이트: 특정 고객의 이메일 주소를 변경하는 쿼리를 작성하세요.
-- UPDATE customers SET email = 'newemail@gmail.com' WHERE customerNumber = 101;

# 직원 전보: 특정 직원을 다른 사무실로 이동시키는 쿼리를 작성하세요.
UPDATE employees SET officeCode = 3 WHERE employeeNumber = 1002;