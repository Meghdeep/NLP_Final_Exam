import requests
from bs4 import BeautifulSoup

url = "http://www.espncricinfo.com/pakistan-v-england-2015-16/engine/match/902643.html?innings=1;view=commentary"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)
p_text=""
article = soup.find_all("div", {"class": "commentary-text"}).findAll("p")
for i in article:
    p_text+='\n'+''.join(i.findAll(text = True))
print(p_text)
f = open("out.txt", 'w')
f.write(str(p_text))
