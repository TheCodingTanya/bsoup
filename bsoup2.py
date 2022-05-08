import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Url: ')
count = int(input('Count: '))
position = int(input('Position: '))
for c in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count + 1
        if count > 18:
            break
        url = tag.get('href', None)

print(url)
