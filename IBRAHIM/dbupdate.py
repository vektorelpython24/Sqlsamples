import sqlite3 as sql
try:
    db = sql.connect(r"chinook\chinook.db") 
    cur = db.cursor() 
    eposta = input("E Posta Adresinizi Giriniz:")
    Cid = int(input("Müşteri Numaranızı Giriniz:"))
    sorgu = f"""
        UPDATE customers
        SET Email = '{eposta}'
        WHERE CustomerId = {Cid};
    """
    cur.execute(sorgu)
    db.commit()
    print("İşlem Başarılı")
    sorgu = f""" SELECT * FROM CUSTOMERS WHERE CustomerId = {Cid} """
    print(cur.execute(sorgu).fetchall()[0])
except Exception as hata:
    db.rollback()
    print("Hata Mesajı :",hata)
finally:
    cur.close()
    db.close() 
    
# Commit işlemi verilerde  DML için yani (INSERT,DELETE,UPDATE) için kullanılır. 
