import time
import requests as req 
import htmlget as get
from bs4 import BeautifulSoup 

myheaders={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
sysdate=time.strftime("%Y-%m")
kyPage = req.get('https://www.kitapyurdu.com/cok-satan-kitaplar/haftalik/1.html', headers=myheaders)
kyParsed = BeautifulSoup(kyPage.content, 'html.parser')

def tolxml(oldAtt):
    lxmlList=[] #Burada fonksyonda oluturacağım temiz veriyi kaydetmek için bir liste oluşturdum
    for element in list(oldAtt):
        soup = BeautifulSoup(str(element),'lxml') #Burada ise veriyi html taglerinden temizledim
        text_1 = "".join(soup.text.split("\r\n")) #Verinin içinde bulunan satır atlama taglerini temizledim
        text_2 = " ".join(text_1.split("    ")) #Verinin çindekki fazla boş karateleri temizledim
        text_3 = "".join(text_2.split("\n"))
        lxmlList.append(text_3) # temiz verileri listeye ekledim
    return lxmlList

kyBooks = kyParsed.find_all('div', itemtype="http://schema.org/Book" )
kyNames = kyParsed.find_all('span', itemprop='name')
kyNames = tolxml(kyNames)
kyprice = kyParsed.find_all('span', class_='value')

for a in range(0,20):
    del kyprice[a]

kypricet,kyprice = tolxml(kyprice),[]

for element in kypricet:
    b = str(element).replace(",",".")
    kyprice.append(float(b))

del kyNames[15]
kyname,kybrand,kyauthor = [],[],[]
for a in range (0,60,3):
    kyname.append(kyNames[a])
    kybrand.append(kyNames[a+1])
    kyauthor.append(kyNames[a+2])

book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,book11,book12,book13,book14,book15,book16,book17,book18,book19,book20 =[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
kydate,ky,kycat=[],[],[]
for a in range (20):
    kydate.append(sysdate)
    ky.append("Kitapyurdu")
    kycat.append('İlgili veri yok')
attlist=[ky,kyname,kyprice,kycat,kybrand,kyauthor,kydate]

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

# print(book1)

listb=[book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,book11,book12,book13,book14,book15,book16,book17,book18,book19,book20]
def writetxt():
    log = open('logs/ky'+sysdate+'.txt', 'w') 
    log.write("Kitapyurdu ayın en çok satan kitapları\n")
    for element in listb:
        a = "".join(str(element))
        log.write(a+"\n")    
        print(a)
    log.close
writetxt()