from tinydb import TinyDB

db = TinyDB('../db/db.json')
restaurantName = 'Kebab z dzika\nNIP: 1234567890\nZolnierska 49 72-200 Szczecin'

class SimplyException(Exception):
    pass
