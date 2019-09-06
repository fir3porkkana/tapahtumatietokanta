from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable = False)
    username = db.Column(db.String(144), nullable = False)
    password = db.Column(db.String(144), nullable = False)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def find_events_with_no_users():
        stms = text("SELECT event.id, event.name FROM event"
                    " WHERE event.id NOT IN ("
                    "       SELECT userevent.event_id FROM userevent)"
                    "GROUP BY event.id")
        res = db.engine.execute(stms)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        
        print(response)
        
        return response
    
    @staticmethod
    def find_events_associated_with_specific_account(account_id):
        stms = text("SELECT event.id, event.name FROM event"
                    " JOIN userevent ON userevent.event_id = event.id"
                    " WHERE userevent.account_id = :account_id").params(account_id=account_id)
        res = db.engine.execute(stms)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
    
    @staticmethod
    def find_events_created_by_account(account_id):
        stms = text("SELECT event.id, event.name FROM event"
                    " WHERE event.creator_id = :account_id").params(account_id=account_id)
        res = db.engine.execute(stms)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response