from application import db
from application.models import Base

userevent = db.Table("userevent",
    db.Column("account_id", db.Integer, db.ForeignKey("account.id"), primary_key=True),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True),
)

class Event(Base):
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=True)
    cancelled = db.Column(db.Boolean, nullable=False)

    accounts = db.relationship("User", secondary=userevent, lazy="subquery", backref=db.backref("events", lazy=True))

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.cancelled = False

