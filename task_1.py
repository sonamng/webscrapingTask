

import requests
from bs4 import BeautifulSoup
import json
def scrap_movie():
     url="https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
     page=requests.get(url)
     soup=BeautifulSoup(page.content,'html.parser')
     # print(soup)
     main_div=soup.find("div",class_="lister")
     tbody=main_div.find("tbody",class_="lister-list")
     name=tbody.find_all("tr")
     list=[]
     sereal_no=0
     for i in name:
          sereal_no+=1
          movie_name=i.find("td",class_="titleColumn").a.get_text()
          movie=movie_name
          movie_years=i.find("td",class_="titleColumn").span.get_text()[1:5]
          years=int(movie_years)
          movie_rating=i.find("td",class_="ratingColumn imdbRating" ).strong.get_text()
          rating=float(movie_rating)
          movie_url=i.find("td",class_="titleColumn").a["href"]
          url="https://www.imdb.com"
          a={"sereal_no":sereal_no,"movie_name":movie,"movie_years":years,"movie_rating":rating}
          list.append(a)
          with open("top_movie.json","w")as file:
               json.dump(list,file,indent=2)
     return list
scrap_movie()

