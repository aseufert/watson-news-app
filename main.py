import requests
import json
from pprint import pprint


with open('credentials.json') as f:
    data = json.load(f)
    news_key = data['newsapikey']
    watson_key = data['watson_key']


def main():
    url = 'https://newsapi.org/v2/top-headlines?country=us&sortBy=popularity&apiKey={}'.format(news_key)
    resp = requests.get(url, timeout=5).json()
    pprint(resp)

    for a in resp['articles']:
        if a['content']:
            print(a['content'])


if __name__ == '__main__':
    main()
