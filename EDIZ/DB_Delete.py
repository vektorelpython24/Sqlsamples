import sqlite3 as sql
try:
    db = sql.connect(r"chinook\chinook.db") 
    cur = db.cursor() 
    kayitIdS = input("Silmek istediğiniz kayıt(lar)a ait id leri ',' koyarak yazınız:")
    sorgu = f"""
        DELETE FROM customers
      WHERE CustomerId IN ({kayitIdS});
    """
    cur.execute(sorgu)
    db.commit()
    print("İşlem Başarılı")
    db.rollback()
except Exception as hata:
    print("Hata Mesajı :",hata)
finally:
    cur.close()
    db.close() 


# Commit işlemi verilerde  DML için yani (INSERT,DELETE,UPDATE) için kullanılır. 