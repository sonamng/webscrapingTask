

from bs4 import BeautifulSoup
from task_1 import scrap_movie
from task2 import group_by_year
import pprint
import json

# scrapped_data=group_by_year (scrap_movie)

scrapped_data=scrap_movie()
movie_by_year=group_by_year(scrapped_data)
def group_by_decade(movies):
     moviedec={}
     list1=[]
     for years in movies:
          mod=years%10
          decade=years-mod
          if decade not in list1:
               list1.append(decade)
     # print(list1)
     list1.sort()
     # print(list1)
     for x in list1:
          moviedec[years]=[]
     for i in moviedec:
          dec10=i+9
          for j in movies:
               if j<=dec10 and j>=i:
                    for v in movies[j]:
                         moviedec[i].append(v)
          with open("my_file3.json","w")as file:
               json.dump(moviedec[i],file,indent=3) 
     return moviedec
group_by_decade(movie_by_year)



