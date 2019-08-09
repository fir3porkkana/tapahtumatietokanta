from flask_wtf import FlaskForm
from wtforms import StringField, validators

class EventForm(FlaskForm):
    name = StringField("Event name", [validators.Length(min=2)])
    description = StringField("Event description")

    class Meta:
        csrf = False