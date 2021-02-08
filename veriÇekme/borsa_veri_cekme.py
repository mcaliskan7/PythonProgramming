import requests
from bs4 import BeautifulSoup

url = "https://www.doviz.com/"
response = requests.get(url)

html_content = response.content
soup = BeautifulSoup(html_content,"html.parser")

for i,j,k in zip(soup.find_all("span",{"class":"name"}),soup.find_all("span",{"class":"value"}),soup.find_all("div",{"class":"change"})):
    print(i.text,":",j.text,"->",k.text.strip())
