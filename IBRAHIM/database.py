import sqlite3 as sql
# veritabanına bağlandıktan sonra sorgu gondermek için bir nesneye ve buna bağlı bir cursor ihtiyacımız var
db = sql.connect(r"chinook\chinook.db") 
# connect metodu veritabanına bağlanmamızı sağlar. Veritabanı belirtilen adreste yoksa sıfırdan oluşturur bu yüzden 
# adres kısmına dikkat etmekte fayda var. 
cur = db.cursor() # cursor sayesinde sorguları veritabanına gönderir sonuçları alabiliriz
sorgu = "SELECT * FROM albums"
sanatci = input("Sorgulamak İstediğiniz Sanatçının İsmini Giriniz:")
if sanatci:
    sorgu += fr" WHERE artistId IN (SELECT artistId FROM artists WHERE NAme LIKE '{sanatci}')"
cur.execute(sorgu)
print(*cur.fetchall())
