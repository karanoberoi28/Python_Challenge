import urllib
from urllib import urlopen
import re

web = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php").read().decode()
comments = re.findall("<!--(.*?)-->",web,re.DOTALL)
text = comments[-1]
print(text)

digit = [int(i) for i in text.split() if i.isdigit()]
link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
num = "12345"

for i in range(0,digit[0]):
    content = urlopen(link % num).read().decode('utf-8')
    pattern = re.compile("and the next nothing is (\d+)")
    match = pattern.search(content)
    if content == "Yes. Divide by two and keep going.":
        num = str(int(float(num)/2))
    elif match == None:
        break
    else:
        num = match.group(1)
        
print(content)
