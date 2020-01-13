from tinydb import Query

from src.globalVariables.globalVariables import db


class IdGenerator:
    orderID = 0

    @classmethod
    def getOrderID(cls):
        cls.orderID += 1
        return cls.orderID

    @classmethod
    def getGlobalId(cls):
        try:
            total_id = db.table("GlobalIdGenerator").get(Query().total_id)['total_id']
        except:
            total_id = 0
        total_id += 1
        db.table("GlobalIdGenerator").upsert({"total_id": total_id}, Query().total_id)
        return total_id

    @classmethod
    def deleteFromDB(cls):
        db.purge_table("GlobalIdGenerator")
