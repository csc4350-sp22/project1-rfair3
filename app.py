import os
import random
import json
import requests
import wikipediaapi


from flask import Flask, render_template
from main import movie_title, movie_tag, movie_genre, _poster



app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0




@app.route('/')
def homepage():
    #random movie list ids:
    list = ["10426", "12153", "584", "5174", "16555"]
    item =  random.choice(list)	

#setting a random movie id equal to item. sets item equal to movie_id in the url below
    movie_id = item
    BASE_URL = "https://api.themoviedb.org/3"
    poster_url = "https://image.tmdb.org/t/p/original/"
    find = requests.get(f"{BASE_URL}/movie/{movie_id}", params={'api_key':os.getenv("api_key")})

#printing out the data from the randomized movie ids
    data = find.text
#pprint.pprint(find.json())

    parse_json=json.loads(data)

    movie_title = parse_json['title']
    movie_tag = parse_json['tagline']
    movie_pic = parse_json['poster_path']
    movie_genre = parse_json['genres']


    _poster = (POSTER_URL+movie_pic)


    #wiki pull through api
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(movie_title)
    wiki_url= page_py.fullurl

    print(movie_title,'\n',movie_tag,'\n',movie_genre,'\n',_poster, '\n', wiki_url)    


    
    return render_template(
    "index.html",
    title = movie_title,
    tagline = movie_tag,
    genre = movie_genre,
    pic = _poster,
    wiki = wiki_url
    )




app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)
