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
from application import views

# Luetaan application-kansiosta views-tiedoston sisältö

# Tuodaan models-luokka käyttöön events-kansiosta
from application.events import models
from application.events import views

# Luodaan lopuksi tietokantataulut
db.create_all()
