import sqlite3 as sql
#veritabanına bağlandıktan sonra sorgu göndermek icin bir nesneye ve buna bağlı bir cursor ihtiyacımız var
db = sql.connect(r"chinook\chinook.db")
#connect methodu veritabanına bağlamamızı sağlar. veritabanı belirtilen adreste yoksa sıfırdan oluşturur
#adres kısmına dikkat etmekte fayda var
cur = db.cursor()#cursor sayesinde sorguları veritabanına gönderir sonuçları alabiliriz
sorgu = "SELECT * FROM albums"
sanatci = input("Sorgulamak istediğiniz sanatçının ismini giriniz: ")
if sanatci:
    sorgu += fr" WHERE artistId IN (SELECT artistId FROM artists WHERE NAME LIKE '{sanatci}')"
cur.execute(sorgu)
print(*cur.fetchall())


#print(cur.fetchmany())
#print(cur.fetchone())
#print(cur.fetchall())

