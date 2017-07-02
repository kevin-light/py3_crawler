# import urllib.request
#
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())