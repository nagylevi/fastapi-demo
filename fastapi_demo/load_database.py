from bs4 import BeautifulSoup
import requests
import re
import sqlite3

# Downloading imdb top 250 movie's data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.select('td.titleColumn')
ratings = [b.attrs.get('data-value')
		for b in soup.select('td.posterColumn span[name=ir]')]

# create a empty list for storing movie information
list = []

# Iterating over movies to extract each movie's details
for index in range(0, len(movies)):
	
	# Separating movie into: 'place', 'title', 'year'
	movie_string = movies[index].get_text()
	movie = (' '.join(movie_string.split()).replace('.', ''))
	movie_title = movie[len(str(index))+1:-7]
	year = re.search('\((.*?)\)', movie_string).group(1)
	place = movie[:len(str(index))-(len(movie))]
	data = {"place": place,
			"movie_title": movie_title,
			"rating": ratings[index],
			"year": year,
			}
	list.append(data)

# Connect to the database and load the scraped movies
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()
movie_list = []
for movie in list:
	movie_list.append((movie['place'], movie['movie_title'], movie['year'], movie['rating']))

cursor.executemany("INSERT OR REPLACE INTO movies VALUES (?,?,?,?)", movie_list)
connection.commit()
connection.close()