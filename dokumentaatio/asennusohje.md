# Asennusohje

_Kaikki tässä esitetyt komennot tulee suorittaa repositorion juuressa_

1. Kloonaa repositorio tietokoneellesi ruudun oikeassa laidassa olevien ohjeiden mukaisesti.
2. Mene repositorion juureen, ja aktivoi virtuaaliympäristö antamalla komento 

    `source venv/bin/activate`
    
3. Asenna sovelluksen riippuvuudet komennolla
    
    `pip install requirements.txt`

4. Käynnistä sovellus porttiin 5000 antamalla komento 

    `python3 run.py`
    
Tämän jälkeen sovellus pyörii lokaalisti portissa 5000


## Sovelluksen siirtäminen Herokuun

1. Alkajaisiksi, poistetaan pkg-resources joka voi aiheuttaa ongelmia Herokun puolella

    `pip freeze | grep -v pkg-resources > requirements.txt`

2. Tämän jälkeen luodaan sovellukselle paikka herokuun. Tämä onnistuu antamalla sovelluksen juuressa komento

    `heroku create [toivomasi nimi sovellukselle]`
    
    Kun paikka on luotu, tulee komentoriville linkki itse sovellukseen sekä sen repositorioon herokussa. Kopioi repositorion       linkki (muotoa git.heroku.com/[sovelluksen nimi].git), ja anna seuraavaksi komento
    
    `git add remote heroku [kopioimasi repositorion linkki]`
    
3. Sovellukselle on nyt paikka herokussa, ja lokaalisti projektilla on myös tämän paikan osoite tiedossa. Kun olemme siihen valmiita, voimme lähettää sovelluksen Herokuun seuraavanlaisesti:

    ```
    git add .
    git commit -m"first commit"
    git push heroku master
