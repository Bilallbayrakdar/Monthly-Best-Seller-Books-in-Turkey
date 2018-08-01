import time
import requests as req 
import htmlGet as get
from bs4 import BeautifulSoup 

myheaders={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
sysdate=time.strftime("%Y-%m")

def tolxml(oldAtt):
    lxmlList=[] #Burada fonksyonda oluturacağım temiz veriyi kaydetmek için bir liste oluşturdum
    for element in list(oldAtt):
        soup = BeautifulSoup(str(element),'lxml') #Burada ise veriyi html taglerinden temizledim
        text_1 = "".join(soup.text.split("\r\n")) #Verinin içinde bulunan satır atlama taglerini temizledim
        text_2 = " ".join(text_1.split("    ")) #Verinin çindekki fazla boş karateleri temizledim
        text_3 = "".join(text_2.split("\n"))
        lxmlList.append(text_3) # temiz verileri listeye ekledim
    return lxmlList

pageRaw = req.get('https://www.babil.com/kitap/cok-satanlar', headers=myheaders)
bblParsed = BeautifulSoup(pageRaw.content, 'html.parser')

bblname =bblParsed.find_all('h2' , itemprop="name")
bblname = tolxml(bblname)

bblauthor =bblParsed.find_all('h3' , class_="author")
bblauthor = tolxml(bblauthor)

bblprice = bblParsed.find_all('span', class_='new-price')
bblpricet,bblprice = tolxml(bblprice),[]

for element in bblpricet:
    a = element[:-4]
    b = a.replace(",",".")
    bblprice.append(float(b))


bblbrand = bblParsed.find_all('h4',class_='store')
bblbrand = tolxml(bblbrand)

bblBooks = bblParsed.find_all('div' , class_="plist-item clearfix")

bbldate,bbl,bblcat=[],[],[]
for a in range (15):
    bbldate.append(sysdate)
    bbl.append("Babil")
    bblcat.append('İlgili veri yok')

book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,book11,book12,book13,book14,book15=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

attlist=[bbl,bblname,bblprice,bblcat,bblbrand,bblauthor,bbldate]
# print(type(bblprice[1]))
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

# print(book1)

listb=[book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,book11,book12,book13,book14,book15]
def writetxt():
    log = open('logs/bbl'+sysdate+'.txt', 'w') 
    log.write("Babil ayın en çok satan kitapları\n")
    for element in listb:
        a = "".join(element)
        log.write(a+"\n")    
        print(a)
    log.close