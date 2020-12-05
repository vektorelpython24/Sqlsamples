/*INSERT INTO customers (FirstName,LastName,Email) 
VALUES ('Ömer Faruk','AYDOĞDU','eposta@eposta.com')*/

/* UPDATE tablo ismi SET sutunadi = 'değer' WHERE şartlar */

--SELECT * FROM customers where FirstName LIKE 'Ö%'

--UPDATE customers
--   SET Email = 'omeraydogduu.5@gmail.com'
-- WHERE CustomerId = 67;

-- DELETE FROM tabloismi WHERE şartlar

SELECT * FROM customers ORDER BY CustomerId desc;

--DELETE FROM customers WHERE CustomerId IN (65,66);

SELECT * FROM customers ORDER BY CustomerId desc;