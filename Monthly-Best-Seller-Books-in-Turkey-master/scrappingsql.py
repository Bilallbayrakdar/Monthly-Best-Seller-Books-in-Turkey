import scrapping1 as sc1
import scrapping2 as sc2
import scrapping3 as sc3
import scrapping4 as sc4
import scrapping5 as sc5
import sqlite3 as sql

db = sql.connect('book.db')
c = db.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS ALL_DATA
          (Satıcı TEXT,Isim TEXT,Fiyat FLOAT,Kategori TEXT,Yayinevi TEXT,Yazar TEXT,Tarih TEXT) """)

def insert():
    listb=[sc1.book1,sc1.book2,sc1.book3,sc1.book4,sc1.book5,sc1.book6,sc1.book7,sc1.book8,
    sc1.book9,sc1.book10,sc1.book11,sc1.book12,sc1.book13,sc1.book14,sc1.book15,sc1.book16,
    sc1.book17,sc1.book18,sc1.book19,sc1.book20,sc1.book21,sc1.book22,sc1.book23,#sc1.book24,
    sc2.book1,sc2.book2,sc2.book3,sc2.book4,sc2.book5,sc2.book6,sc2.book7,sc2.book8,sc2.book9,
    sc2.book10,sc2.book11,sc2.book12,sc2.book13,sc2.book14,sc2.book15,sc2.book16,sc2.book17,
    sc2.book18,sc2.book19,sc2.book20,sc2.book21,sc2.book22,sc2.book23,sc2.book24,sc2.book25,
    sc2.book26,sc2.book27,sc2.book28,sc2.book29,sc2.book30,sc2.book31,sc2.book32,sc2.book33,
    sc2.book34,sc2.book35,sc2.book36,sc2.book37,sc2.book38,sc2.book39,sc2.book40,sc2.book41,
    sc2.book42,sc3.book1,sc3.book2,sc3.book3,sc3.book4,sc3.book5,sc3.book6,sc3.book7,sc3.book8,
    sc3.book9,sc3.book10,sc3.book11,sc3.book12,sc3.book13,sc3.book14,sc3.book15,sc3.book16,
    sc3.book17,sc3.book18,sc3.book19,sc3.book20,sc3.book21,sc3.book22,sc3.book23,sc3.book24,
    sc3.book25,sc3.book26,sc3.book27,sc3.book28,sc3.book29,sc3.book30,sc3.book31,sc3.book32,
    sc3.book33,sc3.book34,sc3.book35,sc3.book36,sc3.book37,sc3.book38,sc3.book39,sc3.book40,
    sc3.book41,sc3.book42,sc4.book1,sc4.book2,sc4.book3,sc4.book4,sc4.book5,sc4.book6,
    sc4.book7,sc4.book8,sc4.book9,sc4.book10,sc4.book11,sc4.book12,sc4.book13,sc4.book14,
    sc4.book15,sc4.book16,sc4.book17,sc4.book18,sc4.book19,sc4.book20,sc5.book1,sc5.book2,
    sc5.book3,sc5.book4,sc5.book5,sc5.book6,sc5.book7,sc5.book8,sc5.book9,sc5.book10,
    sc5.book11,sc5.book12,sc5.book13,sc5.book14,sc5.book15]
    
    for element in listb:
        c.execute(""" INSERT INTO ALL_DATA VALUES(?,?,?,?,?,?,?) """, element)

    db.commit()
def show_t():
    c.execute('''SELECT * FROM ALL_DATA''')
    show=c.fetchall()
    print(show)      

insert()
# show_t()