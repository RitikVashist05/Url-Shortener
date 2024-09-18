class Database:
    def __init__(self):
        self.url_store = {}

    def store_url(self, short_code, original_url):
        self.url_store[short_code] = original_url

    def get_url(self, short_code):
        return self.url_store.get(short_code)
