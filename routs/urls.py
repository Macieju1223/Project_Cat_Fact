import time
import requests
class api:
    url_cat = 'https://catfact.ninja/fact'
    url_activity = "https://boredapi.com/api/activity"

    def get_time():
        """Method for local time"""
        return time.strftime('%D %H:%M:%S')
    
    def fact_ab_cat():
        """Request for cat facts"""
        req = requests.get(api.url_cat)
        req = req.json()
        return req
    
    def activity():
        """Request for activity"""
        req = requests.get(api.url_activity)
        req = req.json()
        return req
