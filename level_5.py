import urllib
from urllib import urlopen
import re

web = urllib.urlopen("http://www.pythonchallenge.com/pc/def/peak.html").read().decode()
comments = re.findall("<!--(.*?)-->",web,re.DOTALL)
text = comments[-1]
print(text)

import pickle
web_1 = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

f = open("word" + ".txt", 'w')
for i in web_1:
    f.write("".join([k * v for k, v in i]))
    f.write("\n")

f.close()
