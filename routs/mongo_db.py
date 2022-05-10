from json import load
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

client = pymongo.MongoClient('mongo_db')

mydb = client['project_cat_facts']
cat_fact = mydb.facts
