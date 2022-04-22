from json import load
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

client = pymongo.MongoClient(os.getenv("DATABASE"))

mydb = client['project_cat_facts']
cat_fact = mydb.facts
