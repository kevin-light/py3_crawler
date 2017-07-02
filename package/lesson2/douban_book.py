import re
import requests

content = requests.get('https://book.douban.com/').text
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?"more-meta".*?"author">(.*?)</span>.*?"year">(.*?)</span>.*?</li>',re.S)
results = re.findall(pattern,content)
# print(results)
for result in results:
    url,name,author,data = result
    author = re.sub('\s','',author)
    data = re.sub('\s','',data)
    print(url,name,author,data)