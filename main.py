import requests
import json
from pprint import pprint


with open('credentials.json') as f:
    data = json.load(f)
    news_key = data['newsapikey']
    watson_key = data['watson_key']


def watson(text):
    url = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone'
    headers = {
        'content-type': 'application/json'
    }
    params = (
        ('version', '2017-09-21'),
        ('sentences', False)
    )
    data = {
        'text': text
    }
    resp = requests.post(url, headers=headers, params=params, json=data, auth=('apikey', watson_key)).json()

    pprint(resp)


def main():
    url = 'https://newsapi.org/v2/top-headlines?country=us&sortBy=popularity&apiKey={}'.format(news_key)
    resp = requests.get(url, timeout=5).json()
    top_headline = resp['articles'][0]['title']

    print(top_headline)

    watson(top_headline)


if __name__ == '__main__':
    main()
