import requests
from bs4 import BeautifulSoup
import json

url = "http://www.espncricinfo.com/pakistan-v-england-2015-16/engine/match/902643.html?innings=1;view=commentary"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)
p_text=""
article = soup.findAll("div", {"class": "commentary-event"})
f_json = open("json_commentary.json",'w')
for i in article:
    #p_text+='\n'+''.join(i.findAll(text = True))
    ptag = i.find("p")
    p_text += '\n'+ ''.join(ptag.findAll( text=True, recursive=True )).replace('\n',' ')
    overs = ''.join(i.find("div",{"class":"commentary-overs"}).findAll( text=True, recursive=True ))
    print(overs)

f = open("view-source_www.espncricinfo.com_pakistan-v-england-2015-16_engine_match_902643.html_innings=1_view=commentary.txt", 'w')
f.write(str(p_text))
