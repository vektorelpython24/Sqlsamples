-- WHERE kullanımı
-- SELECT sutun adları FROM tablo ismi WHERE sartlar
/* 
kullanılabilecek operatör ve anahtar kelimeler
=
!= ya da <>
>=,<=,>
IN
BETWEEN AND
LİKE "pattern"
AND OR NOT

% tüm karakterler için
? ya da _tek karakterler için kullanılıt
*/

--SELECT * FROM employees WHERE EmployeedId > 5;
SELECT * FROM employees WHERE Title LIKE '_ale%'



