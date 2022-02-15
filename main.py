import os
import random
import json
import requests
import wikipediaapi



#.env file
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())



#random movie list ids:
list = ["10426", "12153", "584", "5174", "16555"]
item =  random.choice(list)	



#setting a random movie id equal to item. sets item equal to movie_id in the url below
movie_id = item
BASE_URL = "https://api.themoviedb.org/3"
POSTER_URL = "https://image.tmdb.org/t/p/original/"
find = requests.get(f"{BASE_URL}/movie/{movie_id}", params={'api_key':os.getenv("api_key")})


#printing out the data from the randomized movie ids
data = find.text



parse_json=json.loads(data)

movie_title = parse_json['title']
movie_tag = parse_json['tagline']
movie_pic = parse_json['poster_path']
movie_genre = parse_json['genres']


#Adds the poster url plus the jpg to create 1 unique link
_poster = (POSTER_URL+movie_pic)



#wiki pull through api
wiki_wiki = wikipediaapi.Wikipedia('en')
page_py = wiki_wiki.page(movie_title)
wiki_url= page_py.fullurl




#prints out entire list generated though api
print(movie_title,'\n',movie_tag,'\n',movie_genre,'\n',_poster,'n',wiki_url)



        
