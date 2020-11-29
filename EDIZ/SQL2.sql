--WHERE kullanımı
-- SELECT sutun adları FROM tablo ismi WHERE sartlar
/* 
kullanılabilecek operatör ve anahtar kelimeler
=
!= ya da <>
>=,<=,>,< 
IN
BETWEEN AND
LIKE 'pattern'
AND OR NOT

% tüm karakterler için
? ya da _ tek karakter için kullanılır
*/

-- SELECT * FROM employees WHERE EmployeeId > 5;
-- SELECT * FROM employees WHERE Title LIKE '_ale%'

SELECt * FROM albums WHERE AlbumId = 2
-- '3 harfi a 5. harfi r olan album isimlerine göre kayıtları listeleyen SQL sorgusu'