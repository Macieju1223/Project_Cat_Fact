from fastapi import APIRouter
import requests

from .mongo_db import mydb
from .schem import mail
from .urls import api
from .send import send_email

router = APIRouter(
    tags = ['/mail']
)

@router.post('/put')
def post_mail(email: mail):
    num = len(list(mydb.mails.find({})))
    if not '@' in email.adress:
        return {'Syntax Error': 1000}
    adres = [{
        str(num + 1) : {
            "email" : email.adress,
            "local time" : api.get_time()
        }
    }]
    mydb.mails.insert_many(adres)
    return {"status" : 200}

@router.get('/send')
def send_mail():
    req = requests.get(api.url_cat)
    req = req.json()
    title = "Cat Fact!!"
    content = req['fact']
    send_email(title,content)
    return {"Status" : 200}

@router.get('/show_mails')
def show_mails():
    mails: dict = {}
    num = 0
    for mail in list(mydb.mails.find({})):
        num += 1
        mails.update({
            num : {
                "email" : mail[str(num)]['email'],
                "local time" : mail[str(num)]['local time']
            }
        })
    return mails