import urllib.request,json
from .models import Quotes

api_url=None

def configure_request(app):
    global api_url
    api_url=app.config['API_URL']

def get_quotes():
    #get quotes using url request
    with urllib.request.urlopen(api_url) as url:
        get_quotes_data=url.read()
        get_quotes_response=json.loads(get_quotes_data)

        quotes_results=None

        if get_quotes_response['quote']:
            quotes_list=get_quotes_response['quotes']
            quotes_results=process_quotes_results(quotes_list)
        return quotes_results

def process_quotes_results(quotes_list):
    #to process quotes results snd transform them into a list of objects
    quotes_list=[]

    for quote in quotes_list:
        index=quote.get('id')
        author=quote.get('author')
        quote=quote.get('quote')

        quote=Quotes(index,author,quote)

        quotes_results.append(quote)

    return quotes_results