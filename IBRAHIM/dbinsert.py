import sqlite3 as sql
try:
    db = sql.connect(r"chinook\chinook.db") 
    cur = db.cursor() 
    # insert sorgusunu yazarak işlemi gerçekleştireceğiz. 
    isim = input("İsmi giriniz:")
    soyisim = input("Soyismi giriniz:")
    email = input("Eposta adresini giriniz:")
    sorgu = f"""INSERT INTO customers (FirstName,LastName,Email) VALUES ('{isim}','{soyisim}','{email}')"""
    cur.execute(sorgu)
    sorgu = """SELECT CustomerId FROM customers order by CustomerId DESC LIMIT 1"""
    db.commit()
    print(f"Kayıt Id {cur.execute(sorgu).fetchone()[0]}")
except Exception as hata:
    db.rollback()
    print("Hata Mesajı :",hata)
finally:
    cur.close()
    db.close()