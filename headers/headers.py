import random
from fake_useragent import UserAgent


def header(url, cookie=None):
    try:
        url = str(url.split('://')[1])
    except:
        pass
    ua = UserAgent()
    useragent = random.choice(ua.data['browsers']['firefox'])

    headers = {
        'authority': url,
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': str(random.randint(100, 140)),
        'cookie': cookie,
        'origin': 'https://' + url,
        'referer': 'https://' + url + '/',
        'sec-gpc': '1',
        'user-agent': useragent
    }
    return headers
