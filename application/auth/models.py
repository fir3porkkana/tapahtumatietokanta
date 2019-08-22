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
    #     stms = text("SELECT event.id, event.name FROM event"
    #                 " WHERE event.id NOT IN ("
    #                 "       SELECT userEvent.event_id FROM userEvent)"
    #                 "GROUP BY event.name")
    #     res = db.engine.execute(stms)

    #     response = []
    #     for row in res:
    #         response.append({"id":row[0], "name":row[1]})
        
    #     print(response)
        
    #     return response
