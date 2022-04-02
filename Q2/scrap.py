from ast import arg
from bs4 import BeautifulSoup
import requests
import re
import sys

argv = sys.argv[1:]

url = "https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht"

# Read number of list result form command line
limit = argv[0] if len(argv) else 100

# Fetch context form IMDB page
response = requests.get(url).content
soup = BeautifulSoup(response, "html.parser")
list = soup.find("tbody", {"class":""}).find_all("tr", limit=int(limit))

movies = []

for i in list:
    # find all td with titleColumn
    title = i.find("td",{"class":"titleColumn"})
    # extract all links of title
    link = i.find_all('a', href=True)
    movies.append({
        "title": title.text.strip('\n'),
        "link": link[0]['href']
    })

movies_with_cast = []
for movie in movies:
    # fetch details of movies
    url = 'https://www.imdb.com' + movie["link"]
    res_movie = requests.get(url)
    bs_movie = BeautifulSoup(res_movie.text,'html.parser')
    # Find all movie cast based in data id title-cast-item__actor
    movie_cast = bs_movie.find_all("a",{'data-testid':'title-cast-item__actor'})
    actors = []
    # Loop through whole cast html tags
    for cast in movie_cast:
        # Extract cast name for a tag
        actors.append(cast.text)
    movies_with_cast.append({ "movie": movie["title"], "cast": actors })

print(movies_with_cast)
    

       