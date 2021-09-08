

from bs4 import BeautifulSoup
import requests
import json
import pprint
def E_commerce():
    url="https://webscraper.io/test-sites"
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    commerce=soup.find("div",class_="container test-sites")
    name=commerce.find_all("div",class_="col-md-7 pull-right")
    list=[]
    position=0
    for i in name:
        position+=1
        site=i.find("h2",class_="site-heading").a.get_text().strip()
        name_site=site
        url1=i.find("h2",class_="site-heading").a["href"]
        url2="https://webscraper.io"+(url1)
        url3=url2
        my_dict={"position":position,"name":name_site,"url":url3}
        list.append(my_dict)
        with open ("my_commrece.json","w")as file:
            json.dump(list,file,indent=4)
    return list
E_commerce()



