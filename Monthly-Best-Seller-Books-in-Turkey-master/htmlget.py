import webbrowser, os
import bs4
import time
import requests as req
import itertools as it


class htmlGet():
    def __init__(self):
        
        self.subRaw,self.headers="",{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
        self.cakeNew,self.newCont=[],[]
        self.a,self.b="",""
        self.time=time.strftime("%Y%m%d-%H%M%S")
        self.name=(self.time+".html")
        

        super().__init__()
        self.webpage=input("Öncelikle verisine ulaşmak istediğiniz interned adresini girin>>")
        self.console=input(""" Şimdi veriyi okumak istiyorsanız 'o' yazın\n Veriyi temizlemek için 't' yazın\n>>""")
        if self.console=="o" :
            self.getAllHtml(self.webpage)
            print(self.b)
            print("HACIOSMANBEYMETROSUHACIOSMANBEYMETROSUHACIOSMANBEYMETROSUHACIOSMANBEYMETROSUHACIOSMANBEYMETROSU")
            # self.findSub()
            # print(self.cakeNew)
            
            # self.getCont()
            # self.makeHtml()
        elif self.console=="t":
            self.cleanData()
   
    #Bu func ile bir web sayfasının raw html kodunu alabilirim
    def getAllHtml(self,webpage):
        self.a = req.get(webpage, headers=self.headers)
        self.b = BeautifulSoup(self.a.content, 'html.parser')
        # print(self.b) --Bu satır html kodunun raw halini basar
        return self.b     
    #Bu func ile ekşi şeylerdeki yeni haberlerin linklerini alabilirim
    def findSub(self):
        self.subRaw= self.b.find_all('li',class_='top-seller-item')
        for element in self.subRaw:
            self.cakeNew.append(element)
            print(element)
    def getCont(self):
        for link in (self.cakeNew):
            a = list(self.getAllHtml(link)) 
            b = a[3].find_all('p')
            self.newCont.append(b)
            
    def makeHtml(self):
        html_adjust1="""<html>
        <head>
            <style type="text/css">
                #ornek_div{
                    background-color:#544B5D;
                    font-size:16px;
                    font-family: 'Roboto', sans-serif;
                    color:#DEF3E6;
                    }
                </style>
        <body>
            <div id="ornek_div"> <p>
             """
        html_adjust2="""
                    </p></div>
                    </body>
                    </html>

                     """
        html_1=html_adjust1
        html_2=html_adjust2
        Html_file= open(self.name,"w")
        Html_file.write(html_1)
        for element in self.newCont:
            print("WQEQEQE",element)
            html_cont=str(element)
            Html_file.write(html_cont)
        Html_file.write(html_2)
        Html_file.close()
        webbrowser.open('file://' + os.path.realpath(self.name))

    def cleanData(self):
        clean_html=""" <html>
                            <head>
                                <style type="text/css">
                                    #ornek_div{
                                        background-color:#00004d;
                                        font-size:16px;
                                        font-family: 'Roboto', sans-serif;
                                        color:peru;
                                        }
                                    </style>
                            <body>
                            <div id="ornek_div"> <p>
                            THIS PAGE IS CLEAN
                            </p></div>
                            </body>
                            </html>
                            """
        Html_file= open(self.name,"w")                            
        Html_file.write(clean_html)
        Html_file.close()
