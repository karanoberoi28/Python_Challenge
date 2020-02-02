import urllib
import re

web = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
comments = re.findall("<!--(.*?)-->",web,re.DOTALL)
text = comments[-1]

count = {}
for c in text:
    count[c] = count.get(c, 0) + 1

answer = "".join(re.findall("[A-Za-z]", text))
print(answer)
