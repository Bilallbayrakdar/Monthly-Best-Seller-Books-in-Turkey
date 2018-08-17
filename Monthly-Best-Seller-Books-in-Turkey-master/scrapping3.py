import time
import requests as req 
import htmlget as get
from bs4 import BeautifulSoup 

myheaders={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
sysdate=time.strftime("%Y-%m")
id_raw=req.get("https://www.idefix.com/CokSatanlar/Kitap", headers=myheaders)
id_parsed= BeautifulSoup(id_raw.content,'html.parser')

def tolxml(oldAtt):
    lxmlList=[] #Burada fonksyonda oluturacağım temiz veriyi kaydetmek için bir liste oluşturdum
    for element in list(oldAtt):
        soup = BeautifulSoup(str(element),'lxml') #Burada ise veriyi html taglerinden temizledim
        text_1 = "".join(soup.text.split("\r\n")) #Verinin içinde bulunan satır atlama taglerini temizledim
        text_2 = " ".join(text_1.split("    ")) #Verinin çindekki fazla boş karateleri temizledim
        text_3 = "".join(text_2.split("\n"))
        lxmlList.append(text_3) # temiz verileri listeye ekledim
    return lxmlList

idBooks = id_parsed.find_all('div', class_='cell')
idAuthor1 = id_parsed.find_all('a', class_="who")
idAuthor1 = tolxml(idAuthor1)
idprice = id_parsed.find_all('span', class_='price')
idpricet = tolxml(idprice)
idname = [item['title'] for item in id_parsed.find_all('a', class_='item-name', attrs={"title" : True})]
idcat = [item['data-category'] for item in id_parsed.find_all('div',class_='cell', attrs={"data-category" : True}) ]
idAuthor,idBrand,idf,iddate=[],[],[],[]
idprice=[] 
for a in range (42):
    iddate.append(sysdate)
    idf.append("Idefix")


for element in idpricet:
    a = element[:-4]
    b = a.replace(",",".")
    c = idprice.append(float(b))
    

val = len(idAuthor1)/2
for a in range (0,84,2):
    b = str(idAuthor1[a])
    if b[-3:]=="...":
        idAuthor.append(b[:-3])
    else :
        idAuthor.append(b)
    
    c = str(idAuthor1[a+1])
    if c[-3:]=="...":
        idBrand.append(c[:-3])
    else :      
        idBrand.append(c)

idBooks = tolxml(idBooks)

book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,book11,book12,book13,book14,book15,book16,book17,book18,book19,book20 =[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
book21,book22,book23,book24,book25,book26,book27,book28,book29,book30,book31,book32,book33,book34,book35,book36,book37,book38,book39,book40=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
book41,book42=[],[]

attlist=[idf,idname,idprice,idcat,idBrand,idAuthor,iddate]

for element in attlist:
    book1.append(element[0])
    book2.append(element[1])
    book3.append(element[2])
    book4.append(element[3])
    book5.append(element[4])
    book6.append(element[5])
    book7.append(element[6])
    book8.append(element[7])
    book9.append(element[8])
    book10.append(element[9])
    book11.append(element[10])
    book12.append(element[11])
    book13.append(element[12])
    book14.append(element[13])
    book15.append(element[14])
    book16.append(element[15])
    book17.append(element[16])
    book18.append(element[17])
    book19.append(element[18])
    book20.append(element[19])
    book21.append(element[20])
    book22.append(element[21])
    book23.append(element[22])
    book24.append(element[23])
    book25.append(element[24])
    book26.append(element[25])
    book27.append(element[26])
    book28.append(element[27])
    book29.append(element[28])
    book30.append(element[29])
    book31.append(element[30])
    book32.append(element[31])
    book33.append(element[32])
    book34.append(element[33])
    book35.append(element[34])
    book36.append(element[35])
    book37.append(element[36])
    book38.append(element[37])
    book39.append(element[38])
    book40.append(element[39])
    book41.append(element[40])
    book42.append(element[41])
    
# print(book1)
listb=[book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,book11,book12,book13,book14,book15,book16,book17,book18,book19,book20,book21,book22,book23,book24,book25,book26,book27,book28,book29,book30,book31,book32,book33,book34,book35,book36,book37,book38,book39,book40,book41,book42]
def writetxt():
    log = open('logs/idefix'+sysdate+'.txt', 'w') 
    log.write("Idefix ayın en çok satan kitapları\n")
    for element in listb:
        a = "".join(str(element))
        log.write(a+"\n")    
        print(a)
    log.close
writetxt()