import urllib.request,json
from .models import Quotes


def get_quotes():
    
    with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
        data=url.read()
        response=json.loads(data)
        return response


