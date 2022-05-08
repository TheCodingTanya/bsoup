import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all  of the anchor tags
tags = soup('span')
count = 0
sum = 0
for tag in tags:
    s = int(tag.text)
    count+=1
    sum = sum +ｓ
print(count)
print(sum)
