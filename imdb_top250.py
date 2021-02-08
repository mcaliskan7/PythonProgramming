import requests
from bs4 import  BeautifulSoup

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)

html_content  = response.content

soup = BeautifulSoup(html_content,"html.parser")

a = float(input("Enter minimum rating: "))

film_information = soup.find_all("td",{"class":"titleColumn"})
rating = soup.find_all("td",{"class","ratingColumn imdbRating"})

for inf,rate in zip(film_information,rating):
    inf = inf.text
    rate = rate.text

    inf = inf.strip()
    inf = inf.replace("\n","")

    rate = rate.strip()
    rate = rate.replace("\n","")

    if float(rate)>=a:
        print("Film:",inf,"    Rating:",rate)
