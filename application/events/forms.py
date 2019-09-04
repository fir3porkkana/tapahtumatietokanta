from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class EventForm(FlaskForm):
    name = StringField("Event name", [validators.Length(min=2)])
    description = StringField("Event description")
    minimum = IntegerField("Minimum amount of participants")

    class Meta:
        csrf = False

class ModifyForm(FlaskForm):
    name = StringField("Event name", [validators.Length(min=2)])
    description = StringField("Event description")
    minimum = IntegerField("Minimum amount of participants")

    class Meta:
        csrf = False