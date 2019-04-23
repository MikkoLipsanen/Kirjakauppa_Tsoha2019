# Kirjakauppa_Tsoha2019

## Kuvaus

Harjoitustyössä toteutetaan verkkokirjakaupan karsittu versio. Käyttäjä voi olla joko asiakas tai työntekijä. 
Asiakas voi etsiä kaupan valikoimissa olevia kirjoja kirjoittajan tai teoksen nimen perusteella.
Asiakas voi lisätä kirjoja ostoskoriin ja poistaa niitä sieltä, sekä tutkia ostoskorin sisältöä. 
Asiakas voi myös tehdä tilauksen, joka sisältää asiakkaan yhteystiedot ja tiedon tilatuista kirjoista.
Asiakas voi myös muokata omia asiakastietojaan. Työntekijä voi selata ja muokata kirjojen tietoja 
sekä lisätä ja poistaa kirjoja järjestelmästä. 

Aloitussivulla on listattuna kolme kullakin hetkellä suosituinta kirjaa, mitattuna tilausmäärillä.

Käyttäjälle on yksi tietokantataulu, jossa on yhtenä attribuuttina status (asiakas/työntekijä). Oma tietokantataulunsa
on myös kirjalle, ja ostoskori on näiden välinen monesta moneen-yhteyden toteuttava liitostaulu.
Tilaus on oma tietokantataulunsa, ja koska tilauksen ja kirjan välillä vallitsee myös monesta moneen-
suhde, on myös näiden välillä liitostaulu. Lisäksi käyttäjien roolit on tallennettu omaan tietokantatauluunsa,
jolla on monesta-moneen -suhde käyttäjän kanssa ja niinpä näitäkin tauluja yhdistää liitostaulu.

Toteutetussa versiossa käyttäjille on tarjolla kaksi roolia, *Asiakas* ja *Työntekijä*, joista voi valita
jomman kumman luotaessa uutta käyttäjärofiilia. Statusta voi myös vaihtaa profiilin muokkauksen yhteydessä.

## Asennusohje

Aloita asennus kloonaamalla repositorio omalle koneellesi.

```
$ git clone git@github.com:MikkoLipsanen/Kirjakauppa_Tsoha2019.git
$ cd Kirjakauppa_Tsoha2019

```

Luo seuraavaksi Python-virtuaaliympäristö ja aktivoi se.

```
$ python3 -m venv venv
$ source venv/bin/activate
```

Lataa sitten sovelluksen vaatimat riippuvuudet.

```
$ pip install -r requirements.txt
```

Käynnistä sovellus komennolla

```
$ python run.py
```

Sovellus löytyy nyt  selaimella osoitteesta

```
http://localhost:5000
```

## Käyttöohje

Sovelluksen käyttö on hyvä aloittaa käyttäjäprofiilin luomisella. Tämä onnistuu klikkaamalla aloitussivun yläpalkista 
*Lisää käyttäjä*-painiketta, josta päästään käyttäjätietolomakkeeseen. Lomakkeeseen lisätään perustiedot käyttäjästä,
ja valitaan myös statukseksi joko *Asiakas* tai *Työntekijä*. Jos valitaan statukseksi *Asiakas*, uudella käyttäjätunnuksella 
ja salasanalla kirjautumisen jälkeen yläpalkin pudotusvalikossa on tarjolla kolme vaihtoehtoa, *Muokkaa käyttäjätietoja*, 
*Ostoskori* ja *Tilaukset*. Kaikkia käyttäjäprofiilin tietoja pystyy muuttamaan muokkaa-näkymässä, mukaanlukien käyttäjän
statuksen muuttaminen. 

Yläpalkin *Kirjalista*-painikkeen kautta päästään tarkastelemaan tarjolla olevia kirjoja. Klikkaamalla kirjan nimeä siirrytään
yksittäisen kirjan näkymään, jossa *Lisää ostoskoriin*-painike nimensä mukaisesti lisää kirjan ostoskoriin. Lisäyksen jälkeen
kirja löytyy yläpalkin *Ostoskori*-näkymästä, josta se voidaan haluttaessa poistaa *Poista*-nappia painamalla. Koriin voidaan
lisätä haluttu määrä kirjoja, ja *Tee tilaus*-painike mahdollistaa osatoskorin sisällön muuttamisen tilaukseksi. Tilauksen
vahvistus-näkymässä on vielä mahdollista muuttaa esim. tilauksen toimitusosoitetta. Kun tilaus on vahvistettu klikkaamalla
*Vahvista tilaus*-nappia, se tallentuu asiakkaan tilausten joukkoon, ja tilauksen ja mahdollisten aiempien tilausten tietoja 
päästään katsomaan yläpalkin *Tilaukset*-painikkeen kautta.

Asiakas voi kirjautua ulos milloin tahansa yläpalkin *Kirjaudu ulos*-painikkeen kautta. Kirjalistan selaaminen ja yksittäisten
kirjojen tarkastelu on mahdollista myös ilman sisäänkirjautumista. 

Valitsemalla käyttäjän rooliksi *Työntekijä*, tulee yläpalkin valikon kautta mahdolliseksi lisätä uusi kirja tietokantaan. 
Kun lomakkeelle täytetään kirjan tiedot, tulee kirja näkyville muiden kirjojen joukkoon *Kirjalista*-näkymään. Täällä
työntekijällä on myös mahdollisuus poistaa kirjoja valikoimasta *Poista*-painikkeen avulla tai muuttaa valitun kirjan 
saatavuutta *Muuta*-painikkeella.

Kaikilla käyttäjillä on mahdollista *Kirjalista*-näkymässä hakea haluttua kirjaa joko kirjan tai kirjailijan nimen perusteella. 
Hakukriteeri valitaan pudotusvalikosta ja haku näyttää kaikki annettun merkkijonon sisältävät vaihtoehdot.
  
## Linkkejä

Sovellus on saatavilla verkossa [Herokussa](https://verkkokirjakauppa.herokuapp.com/)

Kirjautuminen onnistuu luomalla oman käyttäjäprofiilin tai käyttämällä testitunnuksia:

Käyttäjätunnus: **hello**

Salasana: **world**


[Projektin alustava UML-kaavio](documentation/tietokantakaavio.jpg)
[Tietokantataulut](documentation/db_tables.txt)
[Käyttötapauksia](documentation/user_stories.txt)

     
