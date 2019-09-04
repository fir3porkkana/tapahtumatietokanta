from application import db
from application.models import Base

from sqlalchemy.sql import text

userevent = db.Table("userevent",
    db.Column("account_id", db.Integer, db.ForeignKey("account.id"), primary_key=True),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True),
)

class Event(Base):
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=True)
    minimum = db.Column(db.Integer, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)

    accounts = db.relationship("User", secondary=userevent, lazy="subquery", backref=db.backref("events", lazy=True))

    def __init__(self, name, description, minimum, current_user_id):
        self.name = name
        self.description = description
        self.minimum = minimum
        self.creator_id = current_user_id

    @staticmethod
    def find_users_interested_in_specific_event(event_id):
        stms = text("SELECT account.id, account.name FROM account"
                    " JOIN userevent ON userevent.account_id = account.id"
                    " WHERE userevent.event_id = :event_id").params(event_id=event_id)
        res = db.engine.execute(stms)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
    
    @staticmethod
    def find_creator_of_event(creator_id):
        stms = text("SELECT account.name FROM account"
                    " WHERE account.id = :creator_id").params(creator_id=creator_id)
        res = db.engine.execute(stms)

        response = []
        for row in res:
            response.append({"name":row[0]})

        return response


