
import requests
from bs4 import BeautifulSoup
import json
def scrap_sonam():
     url="https://webscraper.io/test-sites"
     set=requests.get(url)
     soup=BeautifulSoup(set.content,'html.parser')
     # print(soup)
     main_div=soup.find("div",class_="container test-sites")
     name=main_div.find_all("div",class_="col-md-7pull-right")
     
     list=[]
     sereal_no=0

     for i in name:
          sereal_no+=1
          commers_name=i.find("h2",class_="site-heading").a.get.text().strip()
          name=commers_name
          # print(commers_name)
          h1=i.find("h2",class_="site-heading").a["href"]
          h=h1
          url="https://webscraper.io"+h1
          url2=url
          a={"sereal_no":sereal_no,"name":name,"h":h}
          list.append(a)
          with open("commers.json","w")as file:
               json.dump(list,file,indent=4)
     return list
scrap_sonam()
     




































     
     




