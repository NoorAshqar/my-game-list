from flask_pymongo import pymongo
from flask import Flask
import urllib.parse

client = pymongo.MongoClient("mongodb+srv://xoro:"+urllib.parse.quote("p@ssvv0rd")+"@cluster0.rphug.mongodb.net/Portfolio?retryWrites=true&w=majority")
