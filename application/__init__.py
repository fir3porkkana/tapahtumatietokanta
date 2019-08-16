from flask import Flask
app = Flask(__name__)

# Tuodaa SQLAlchemy käyttöö
from flask_sqlalchemy import SQLAlchemy

# Käytetään events.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, että tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///events.db"

# Laitetaan sqlalchemy tulostamaan kaikki tehdyt sql-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan se db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Luetaan application-kansiosta views-tiedoston sisältö
from application import views

# Tuodaan models-luokka käyttöön events-kansiosta
from application.events import models
from application.events import views

# tuodaan models luotavaksi käyttäjäkansiosta

from application.auth import models
from application.auth import views

#kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please log in to use this functionality"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Luodaan lopuksi tietokantataulut
try: 
    db.create_all()
except:
    pass