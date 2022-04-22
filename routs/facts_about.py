from fastapi import APIRouter
import requests

from .mongo_db import mydb
from .urls import api

router = APIRouter(
    tags = ['/fact']
)


@router.get('/cats')
def get_cat_fact():
    req = requests.get(api.url_cat)
    req = req.json()
    rec = [{
        "local time" : api.get_time(),
        "fact" : req['fact']
    }]
    mydb.facts.insert_many(rec)
    return req['fact']

@router.get('/all')
def get_db_facts():
    facts_dic: dict = {}
    i = 0
    for fact in list(mydb.facts.find({})):
        i += 1
        facts_dic.update({
            i : {
                'fact' : fact['fact'],
                'local time' : fact['local time']
            }})
    return facts_dic
