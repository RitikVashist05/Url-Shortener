from utils import generate_short_code
from database import Database

class URLShortener:
    def __init__(self):
        self.db = Database()

    def shorten_url(self, original_url):
        short_code = generate_short_code()
        while self.db.get_url(short_code):  
            short_code = generate_short_code()
        self.db.store_url(short_code, original_url)
        return short_code

    def expand_url(self, short_code):
        return self.db.get_url(short_code)

