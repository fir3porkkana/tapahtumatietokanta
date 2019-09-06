# Projektista uupumaan jääneet ominaisuudet

Alun perin suunnitelmissa oli liittää jokaiseen tapahtumaan erillinen tapahtumapaikka ja aika, joista kummatkin olisi toteutettuna omana tietokantataulunaan sekä niiden perusteella olisi voinut mm. rajata tapahtumia.


Kuitenkin, kurssin kuluessa tapahtumalle attribuuttina annettava kuvaus hoiti molempien virkaa ja attribuutiksi annettava Minimum kuvaa pienintä määrää osallistujia, joilla tapahtuma järjestetään.


Tällä hetkellä sovellukseen voi lisätä tapahtumia, joilla on nimi, kuvaus sekä minimiosallistujamäärä. Tämä myös asettaa käyttäjien kontolle vastuun siitä, että tapahtumat ovat oikeasti järkeviä sekä organisoija kertoo kuvauksessa kaiken tarpeellisen osallistujille. Asian olisi voinut totetuttaa paremmin vaikkapa eriyttämällä paikan/osoitteen ja ajan erillisiksi attribuuteiksi. Adminoikeuksilla lisättävien enumien taakse edellämainittuja ei kuitenkaan olisi ollut mielekästä laittaa, sillä toiminnallisuus olisi yhtä tyhjän kanssa jos tavallinen ei-adminkäyttäjä haluaa järjestää jonkin tapahtuman jossakin muussa paikassa kuin mitä enum antaisi vaihtoehdoksi, ja tällöin tieto olisi välitetty kuvauksen kautta joka tapauksessa (kuten nytkin). 


Ylläolevan ongelman voisi ratkaista esimerkiksi googlen karttaintegraatiolla, mutta se ylittää tämän projektin puitteet.
