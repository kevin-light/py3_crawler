import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError

base_url = 'http://weixin.sogou.com/weixin?'

headers = {
# 'Cookie':'CXID=0C149E61C7BC5EB6B54EB2725312D632; SUV=00F310F76551731B5939067764350347; sw_uuid=8845775450; sg_uuid=7637935519; ssuid=3970394084; dt_ssuid=5901305040; IPLOC=CN3100; ad=Zyllllllll2Bg9VRlllllVOtyUGlllllBqV8pZllll9lllllxqxlw@@@@@@@@@@@; SUID=1B7351653965860A59112A6E000EBAE0; ABTEST=0|1499245931|v1; SNUID=AEC5E4D3B6B0E638D39D64FFB6CB59D6; weixinIndexVisited=1; sct=2; JSESSIONID=aaagOEmBbmneCboMx3OZv; ppinf=5|1499246974|1500456574|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyNzolRTclOUMlOEIlRTYlOTclQTUlRTUlODclQkF8Y3J0OjEwOjE0OTkyNDY5NzR8cmVmbmljazoyNzolRTclOUMlOEIlRTYlOTclQTUlRTUlODclQkF8dXNlcmlkOjQ0Om85dDJsdVBwSjVsWEpGZWx6SEktSlZfYU5rYnNAd2VpeGluLnNvaHUuY29tfA; pprdig=NSxes9ua632r5x0jx9rwzB-hKYf0WYMvOZLHj4lBQqw8WgJQmnqVmP46OjcPAvgCCvwXH70_pO6smpTiTxljQhmmNyGK91qbwh2LQ4eBL3nH-9F0yONko1Ah2oYfBunU_4Ns0xX33-YD8bKCq6CmtA7oLlc_lnyz2CS1K52PWFU; sgid=27-29506951-AVlcsX6zLVOMX7ogbRBHaVc; ppmdig=1499246974000000b50c14b3d7b1d953035c5dc21fba481a',
# 'Host':'weixin.sogou.com',
# 'Upgrade-Insecure-Requests':'1',
# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

'Cookie':'sw_uuid=2830702991; sg_uuid=5392430425; ssuid=5689119089; dt_ssuid=8223478340; SUV=1495264153153728; CXID=E94D91E5216C768070A092250D975EC5; SUID=5F9AC1B73665860A590C94F7000A39CB; IPLOC=CN3100; ld=jkllllllll2B4MmQlllllVOpBykllllly9WrGlllll9lllll9klll5@@@@@@@@@@; usid=8b3vb5jnGtBK9HOO; SNUID=29225C299E9BCD0CF1505F759E5DDEC3; ABTEST=0|1499258952|v1; weixinIndexVisited=1; sct=2; JSESSIONID=aaafGiWJMDQyE6JC45OZv; ppinf=5|1499260514|1500470114|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyNzolRTclOUMlOEIlRTYlOTclQTUlRTUlODclQkF8Y3J0OjEwOjE0OTkyNjA1MTR8cmVmbmljazoyNzolRTclOUMlOEIlRTYlOTclQTUlRTUlODclQkF8dXNlcmlkOjQ0Om85dDJsdVBwSjVsWEpGZWx6SEktSlZfYU5rYnNAd2VpeGluLnNvaHUuY29tfA; pprdig=lDOxt5IoU9zUYJ5jF02unNAZIy90XUFPuPOLcoXXshzt-52rhiyiVPfQ7Cy9Ym2ddI1we_T7wevnubDJLrNgauHg53hVfrZFmaLqR1Pm1D3ZTFD0_1MdIuT3jENAUKw_NOo4FMmkISB6YdCyK39W8u3SmbBXVx9praDLAl1hPpg; sgid=27-29506951-AVlc5mIzDyGo373awXdIftQ; ppmdig=1499260514000000d286b57807d7259f1263a4e9e2238261',
'Host':'weixin.sogou.com',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'


    }

keyword = '风景'

def get_html(url):
    try:
        response = requests.get(url, allow_redirects=False,headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            print(302)
    except ConnectionError:
        return get_html(url)

def get_index(keyword,page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html

def main():
    for page in range(1,101):
        html = get_index(keyword,page)
        print(html)

if __name__ == '__main__':
    main()
