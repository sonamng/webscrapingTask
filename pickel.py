

from bs4 import BeautifulSoup
import requests
import json
import pprint
def pickle_name_scrap():
    url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    api=requests.get(url)
    soup=BeautifulSoup(api.text,"html.parser")
    div_1=soup.find("div",class_="_1gX7")
    div_2=div_1.span.get_text()
    pickle=div_2.split(" ")
    split=int(pickle[1])
    split1=split//32+1
    list=[]
    position=0
    k=1
    while k<=split1:
        url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(k)
        api=requests.get(url)
        # print(api)
        soup=BeautifulSoup(api.text,"html.parser")
        main_div=soup.find("div",class_="_3RA-")
        div=main_div.find_all("div",class_="UGUy")
        # div=main_div.find("div",class_="").span.get_text()
        pickle_price=main_div.find_all("div",class_="_1kMS")
        link=main_div.find_all("div",class_="_3WhJ")

        i=0
        while i<len(div):
            position+=1
            pickle_name=div[i].get_text()
            price=pickle_price[i].get_text()
            link_1=(link[i].a["href"])
            dict={"position":position,"pickle_name":pickle_name,"price":price,"link1":link_1}
            list.append(dict)
            i=i+1
        k=k+1
        
    with open ("pickle_data.json","w")as file:
        json.dump(list,file,indent=5)
    return list
pickle_name_scrap()