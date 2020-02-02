import urllib
import re

web = urllib.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
comments = re.findall("<!--(.*?)-->",web,re.DOTALL)
text = comments[-1]

alphas = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+",text)
answer = "".join(alphas)

print(answer)
