from fastapi import APIRouter
import requests

from .mongo_db import mydb
from .urls import api

router = APIRouter(
    tags = ['/fact']
)


@router.get('/cats')
def get_cat_fact():
    req = api.fact_ab_cat()
    doc = [{
        "local time" : api.get_time(),
        "fact" : req['fact'],
        "length" : req['length']
    }]
    mydb.facts.insert_many(doc)
    return req['fact']

@router.get('/activity')
def get_activity():
    req = api.activity()
    doc = [{
        "activity" : req['activity'],
        "participants" : req['participants'],
        "price" : req['price'],
        "accessibility" : req['accessibility'],
        "local time" : api.get_time()
    }]
    mydb.activity.insert_many(doc)
    return req

@router.get('/all_facts')
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

@router.get('/all_activites')
def get_db_activities():
    activities_dict: dict = {}
    i = 0
    for activity in list(mydb.activity.find({})):
        i += 1
        activities_dict.update({
            i : {
                "activity" : activity['activity'],
                "local time" : activity['local time']
            }
        })
    return activities_dict
