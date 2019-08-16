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

    # @staticmethod
    # def find_events_with_no_users():
    #     stms = text("SELECT event.name FROM event"
    #                 " WHERE COUNT(event.accounts) = 0")
    #     res = db.engine.execute(stms)

    #     response = []
    #     for row in res:
    #         response.append({"name":row})
        
    #     return response
