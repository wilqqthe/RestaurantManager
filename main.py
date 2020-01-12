from tinydb import TinyDB, where
from Table import *

db = TinyDB('db.json')
tables = db.table("Tables")
