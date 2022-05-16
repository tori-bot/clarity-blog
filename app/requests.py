import urllib.request,json
from .models import Quotes
from flask import abort


# API_URL=None

# def configure_request(app):
#     global API_URL
#     API_URL=app.config['API_URL']

def get_quotes():
    #get quotes using url request

    # response=requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    # if response.status_code==200:
    #     json_data=response.json()
    #     data=json_data['data']
    #     return data
    # else:
    #     abort(404)

    # url_quotes=API_URL
    with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
        data=url.read()
        response=json.loads(data)
        return response




#     api_url='http://quotes.stormconsultancy.co.uk/random.json'
#     with urllib.request.urlopen(api_url) as url:
#         get_quotes_data=url.read()
#         get_quotes_response=json.loads(get_quotes_data)

#         quotes_results=None

#         if get_quotes_response['quote']:
#             quotes_list=get_quotes_response['quotes']
#             quotes_results=process_quotes_results(quotes_list)
#         return quotes_results

# def process_quotes_results(quotes_list):
#     #to process quotes results snd transform them into a list of objects
#     quotes_list=[]

#     for quote in quotes_list:
#         index=quote.get('id')
#         author=quote.get('author')
#         quote=quote.get('quote')

#         quote=Quotes(index,author,quote)

#         quotes_results.append(quote)

#     return quotes_results