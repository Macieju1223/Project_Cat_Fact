import time

class api:
    url_cat = 'https://catfact.ninja/fact'

    def get_time():
        return time.strftime('%D %H:%M:%S')
