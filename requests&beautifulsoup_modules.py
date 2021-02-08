import requests
from bs4 import BeautifulSoup

url = "http://ee.yeditepe.edu.tr/"
response = requests.get(url)
"data is at response"

html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")

print(soup.prettify())

print(soup.find_all("a"))

for i in soup.find_all("a"):
    print(i.text)
    print(i.get("href"))

print(soup.find_all("div",{"class":"page-heading"}))
