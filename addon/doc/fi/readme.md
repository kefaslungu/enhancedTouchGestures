# Laajennetut kosketuseleet #

* Tekijä: Joseph Lee
* Lataa [vakaa versio][1]
* NVDA compatibility: 2018.2 to 2019.2

Tämä lisäosa tarjoaa lisää kosketuseleitä NVDA:han. Mukana on eleitä myös
helpompaa selaustilanavigointia varten.

Huom: Tämä lisäosa vaatii NVDA 2018.2:n tai uudemman ja
kosketusnäyttötietokoneen, jossa on asennettuna Windows 8.1 tai 10.

## Komennot

### Käytettävissä kaikkialla

* Kaksoisnapautus neljällä sormella: ottaa syöteohjeen käyttöön tai poistaa
  sen käytöstä.
* Napautus ja pitäminen: suorittaa hiiren oikean painikkeen napsautuksen
  sormesi alla olevalle objektille.
* Pyyhkäisy oikealle neljällä sormella: kosketusnäppäimistö näkyviin/pois.

### Objektitila

* Pyyhkäisy alas kolmella sormella: lue nykyinen ikkuna.
* pyyhkäisy vasemmalle kolmella sormella: ilmoita aktiivinen objekti.
* pyyhkäisy oikealle kolmella sormella: ilmoita nykyinen navigointiobjekti.
* pyyhkäisy ylös neljällä sormella: lukee nykyisen ikkunan otsikon.
* pyyhkäisy alas neljällä sormella: lukee tilarivin tekstin.

## Verkkotila

Tämän selaustilassa käytettävissä olevan kosketustilan avulla voit liikkua
asiakirjassa valitsemasi elementin mukaan. Siirry selaustila-asiakirjoissa
verkkokosketustilaan napauttamalla kolmella sormella. Tässä tilassa yhdellä
sormella pyyhkäisy ylös tai alas vaihtaa käytettävissä olevien
elementtinavigointitilojen välillä, kun taas vastaavasti pyyhkäisy yhdellä
sormella oikealle tai vasemmalle siirtää seuraavaan tai edelliseen valittuna
olevaan elementtiin. Kun siirryt pois selaustila-asiakirjasta,
objektikosketustila otetaan käyttöön automaattisesti.

## Syntetisaattoriasetusten tila

Voit käyttää tätä tilaa nopeaan syntetisaattoriasetusten säätämiseen, kuten
puheäänen valitsemiseen ja äänenvoimakkuuden muuttamiseen. Käytä kahden
sormen pyyhkäisyä vasemmalle tai oikealle siirtyäksesi asetusten välillä ja
kahden sormen pyyhkäisyä ylös tai alas muuttaaksesi arvoja. Nämä eleet
peilaavat näppäimistöllä käytettäviä syntetisaattorin asetusrenkaan
komentoja.

## Koordinaattien ilmoitusäänimerkki

Jos olet ottanut käyttöön hiiren koordinaattien ilmaisemisen
Hiiriasetukset-valintaikkunasta, kuulet äänimerkkejä, jotka ilmaisevat
nykyisen sijainnin näytöllä kosketuseleitä käyttäessäsi.

## Kosketuskomentojen läpivienti

Käytettävissä on määrittämätön komento, joka mahdollistaa kosketuseleiden
käytön enintään kymmenen sekunnin ajan tai manuaalisesti ikään kuin NVDA ei
olisi käynnissä. Voit käyttää tätä määrittämällä komennon
Syötekomennot-valintaikkunan Laajennetut kosketuseleet
-kategoriasta. Valitse tämän jälkeen NVDA-valikosta Asetukset/Kosketuksen
vuorovaikutus ja määritä asetuksen "Keskeytä NVDA:n kosketuskomento" arvoksi
jotain kolmen ja kymmenen sekunnin väliltä (oletus on 5).

## Poista käytöstä kosketustuki profiileissa

Jos jokin muu profiili kuin "(normaalit asetukset)" on aktiivisena ja jos
siirryt Kosketuksen vuorovaikutus -valintaikkunaan, löydät sieltä "Poista
kosketuksen vuorovaikutustuki kokonaan käytöstä" -valintaruudun. Kun se on
valittuna ja vastattu kysyttäessä kyllä, kosketustuki poistetaan kokonaan
käytöstä kyseisessä profiilissa. Tästä on hyötyä sovelluksissa, jotka
tarjoavat omia kosketuskomentojaan. Palauta kosketustuki käyttöön joko
poistamalla valintaruudun valinta tai vaihtamalla kosketuksen
läpivientitilaa manuaalisesti.

## Versio 18.08

* Yhteensopiva NVDA 2018.3:n ja sitä uudempien versioiden kanssa.

## Versio 18.06

* Lisäosan asetukset löytyvät nyt uudesta monikategoriaisesta
  Asetukset-ruudusta kohdasta "Laajennetut kosketuseleet". Tämän seurauksena
  edellytetään NVDA 2018.2:ta.
* Korjattu wxPython 4:n kanssa ilmenneitä yhteensopivuusongelmia.

## Versio 18.04

* Ratkaisee ongelman, jossa NVDA-asetusruudun
  Kosketusvuorovaikutus-kategoria saattaa aiheuttaa virheäänen kuulumisen
  tähän lisäosaan tehtyjen muutosten vuoksi.

## Versio 18.03

* NVDA 2018.1 vaaditaan.
* Koska NVDA 2018.1:ssä on kosketuskirjoituksen valintaruutu, sitä ei ole
  enää tässä lisäosassa.

## Versio 17.12

* Vaatii NVDA 2017.4:n. Lisäosa voi nyt käsitellä asetusprofiilien
  vaihdoksia.
* Koska NVDA 2017.4 sisältää näytön suunnan ilmoittamisen, kyseinen
  ominaisuus on poistettu tästä lisäosasta.
* Lisätty Kosketuksen vuorovaikutus -valintaikkunaan piilotettu
  valintaruutu, joka poistaa kosketustuen kokonaan käytöstä (käytettävissä,
  mikäli muu profiili kuin "(normaalit asetukset)" on aktiivisena).
* Mikäli käytetään NVDA 2018.1:tä tai uudempaa, Kosketuksen vuorovaikutus
  -vaihtoehto näkyy kahdesti Asetukset-valikossa. Toisena oleva eli alempi
  avaa tämän lisäosan valintaikkunan.
* Kosketuskirjoitustilaa ei enää näytetä lisäosan Kosketuksen vuorovaikutus
  -valintaikkunassa, mikäli käytetään NVDA 2018.1:tä tai uudempaa.

## Versio 17.10

* Windows 8:n alkuperäisversiota ei enää tueta Microsoftin tukipolitiikan
  vuoksi.
* Ruudun suuntaa ei enää ilmoiteta kahdesti NVDA 2017.4:n kehitysversioita
  käytettäessä.

## Versio 17.07.1

* Kosketuksen vuorovaikutus -valintaikkunaan lisätty asetus kosketuseleiden
  läpiviennin manuaaliseen käyttöön ottoon ja käytöstä poistamiseen ilman
  ajan määritystä.
* Kosketuksen vuorovaikutus otetaan käyttöön manuaalisen läpivientitilan
  ollessa pois käytöstä, mikäli läpivienti otetaan käyttöön ennen sen ajan
  umpeutumista.

## Versio 17.07

* Lisätty Asetukset-valikkoon uusi Kosketuksen vuorovaikutus -vaihtoehto,
  josta avautuu valintaikkuna, jossa on mahdollista määrittää, miten NVDA
  toimii kosketusnäyttöjä käytettäessä.
* Kun tämä versio on asennettuna, kosketusnäppäimistön näppäimiä on
  kaksoisnapautettava niiden painamiseksi. Voit vaihtaa takaisin vanhaan
  kirjoitustapaan ottamalla käyttöön kosketuskirjoituksen Kosketuksen
  vuorovaikutus -valintaikkunasta.
* Lisätty (määrittämätön) komento, jonka avulla NVDA ohittaa kosketuseleet
  enintään kymmenen sekunnin ajan.
* Lisätty Kosketuksen vuorovaikutus -valintaikkunaan asetus, jolla NVDA
  keskeyttää kosketusvuorovaikutuksen  3-10 sekunnin ajaksi, mikä
  mahdollistaa kosketuseleiden suoran suorittamisen (ikään kuin NVDA ei
  olisi käynnissä; oletus on 5 sekuntia).
* Lisätty virheenkorjauksen ilmoitukset hiiren oikean näppäimen
  napsautuksille (napauta ja pidä) NVDA:n lokiin tallennettaviksi
  (edellyttää NVDA 2017.1:tä tai uudempaa).
* Ruudun koordinaattien ilmaisuun tehtyjen muutosten vuoksi edellytetään
  NVDA 2017.1:tä tai uudempaa.

##Versio 17.03

* Korjattu ongelma, jossa koordinaatinilmoitusäänimerkkiä ei toistettu tai
  virheääni kuului sen asemesta NVDA 2017.1:tä tai uudempaa käytettäessä.

##Versio 16.12

* Verkkotila toimii Microsoft Edgessä, Microsoft Wordissa ja muualla, missä
  käytetään selaustilaa.
* Luettelot ja kiintopisteet lisätty verkkotilan elementteihin.

## Versio 16.06

* Ensimmäinen vakaa versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets
