import time
import requests as req 
import htmlget as get
from bs4 import BeautifulSoup 

sysdate=time.strftime("%Y-%m")


myheaders={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
hbpage = req.get("https://www.hepsiburada.com/roman-kitaplari-c-1501702?siralama=coksatan", headers=myheaders)

hbpage_parsed = BeautifulSoup(hbpage.content,'html.parser')

def tolxml(oldAtt):
    lxmlList=[] #Burada fonksyonda oluturacağım temiz veriyi kaydetmek için bir liste oluşturdum
    for element in list(oldAtt):
        soup = BeautifulSoup(str(element),'lxml') #Burada ise veriyi html taglerinden temizledim
        text_1 = "".join(soup.text.split("\r\n")) #Verinin içinde bulunan satır atlama taglerini temizledim
        text_2 = "".join(text_1.split("  ")) #Verinin çindekki fazla boş karateleri temizledim
        lxmlList.append(text_2) # temiz verileri listeye ekledim
    return lxmlList

cleanAll_1 =[item['data-product'] for item in hbpage_parsed.find_all('button',attrs={"data-product" : True})] 
cleanAll =[]

for element in cleanAll_1:
    a = str(element).split(",")
    # print(a)
    cleanAll.append(a)

pricet,saticit,detayt,kategorit,yayincit=[],[],[],[],[]                                                         #
for a in range (len(cleanAll)):                          #
    pricet.insert(a,cleanAll[a][1])                       #
    saticit.insert(a,cleanAll[a][0])                      #
    detayt.insert(a,cleanAll[a][3])                       #
    kategorit.insert(a,cleanAll[a][5])                    #
    yayincit.insert(a,cleanAll[a][6])                     #

price,satici,detay,kategori,yayinci=[],[],[],[],[]
hbname,hbauthor,hbdate,hb=[],[],[],[]
detay_1=[]

for element in pricet:
    price.append(float(element[9:-1]))
for element in saticit:
    satici.append(element[16:])
for element in detayt:
    detay.append(element[14:]) 
for element in kategorit:
    kategori.append(element[15:])
for element in yayincit:
    yayinci.append(element[12:])   
for element in detay:
    a = element.split(" - ")
    if(a[0]!='"67 Peşimizde Olanlar'):
    # print(a)
        hbauthor.append(a[1])

        hbname.append(a[0])
# print(len(hbname))
# print(len(hbauthor))

for a in range (24):
    hbdate.append(sysdate)
    hb.append("Hepsiburada")
    # print(detay[a])

book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,book11,book12,book13,book14,book15,book16,book17,book18,book19,book20,book21,book22,book23,book24=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
attList=[hb,hbname,price,kategori,yayinci,hbauthor,hbdate]

for element in attList:
    # print(element)
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
    # book24.append(element[23])

listb=[book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,book11,book12,book13,book14,book15,book16,book17,book18,book19,book20,book21,book22,book23]#,book24]
def writetxt():
    log = open('logs/hepsi'+sysdate+'.txt', 'w') 
    log.write("Hepsiburada ayın en çok satan kitapları\n")
    for element in listb:
        z = str(element)
        log.write(z+"\n")    
        print(z)
    log.close
writetxt()