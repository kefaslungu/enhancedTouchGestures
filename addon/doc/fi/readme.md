# Laajennetut kosketuseleet #

* Tekijä: Joseph Lee
* Lataa [vakaa versio][1]
* NVDA compatibility: 2020.1 to 2021.1

Tämä lisäosa tarjoaa lisää kosketuseleitä NVDA:han. Mukana on eleitä myös
helpompaa selaustilanavigointia varten.

Huom: Tämä lisäosa edellyttää NVDA 2020.1:tä tai uudempaa ja
kosketusnäyttötietokonetta, jossa on asennettuna Windows 8.1 tai 10.

## Komennot

### Käytettävissä kaikkialla

* Kaksoisnapautus neljällä sormella: ottaa syöteohjeen käyttöön tai poistaa
  sen käytöstä.
* Pyyhkäisy oikealle neljällä sormella: tuo näkyviin kosketusnäppäimistön
  tai piilottaa sen.
* Ctrl+Alt+NVDA+T: Vaihtaa kosketusvuorovaikutuksen tilaa.

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

## Versio 20.09

* Poistettu mahdollisuus NVDA:n kosketusvuorovaikutuksen käytöstä
  poistamiseen enintään 10 sekunniksi (kosketuskomennon läpivienti).
* Poistettu koordinaattien ilmaisemisen äänimerkki

## Versio 20.07

* Lisätty näppäinkomento kosketuksen vuorovaikutuksen tilan vaihtamiseen tai
  kosketuksen läpiviennin käyttöön ottamiseen/käytöstä poistamiseen
  (Ctrl+Alt+NVDA+T).
* Koska NVDA 2020.1 sisältää kosketuskomennon oikean hiiripainikkeen
  napsauttamiselle (yhden sormen napautus ja pito), komento on poistettu
  tästä lisäosasta. Tästä johtuen lisäosa edellyttää NVDA 2020.1:tä tai
  uudempaa.
* Mahdollisuus NVDA:n kosketuksen vuorovaikutuksen käytöstä poistamiselle
  enintään 10 sekunniksi (kosketuskomennon läpivienti) on
  poistettu. Tulevaisuudessa tämä komento vaihtaa kosketuksen
  vuorovaikutuksen tilaa.
* Kosketuksen vuorovaikutukseen tehtyjen muutosten takia kosketuskomennon
  läpivientitoiminto ja Laajennetut kosketuseleet -asetuspaneeli poistetaan
  käytöstä NVDA:n kehitysversioissa. Kosketuskomennon läpiviennin käyttöön
  ottamiseen käytetty komento vaihtaa kosketuksen vuorovaikutuksen tilaa.
* Koordinaattien ilmaisemisen äänimerkkitoiminto on vanhentunut ja
  poistetaan lisäosan tulevassa versiossa.
* Koordinaattien ilmaisemisen äänimerkkiä ei kuulu kosketusnäppäimistöä
  käytettäessä.
* NVDA ei näytä enää tekevän mitään tai toista virheääniä tutkittaessa
  kosketuksella modernin syötön palvelua, kuten emojipaneelia.
* NVDA näyttää virheilmoituksen, jos kosketusnäppäimistöä ei voi aktivoida
  (pyyhkäisy oikealle neljällä sormella).

## Versio 20.06

* Ratkaistu useita koodaustyylin ongelmia sekä mahdollisia bugeja Flake8:n
  kanssa.

## Versio 20.04

* Hiiren oikean painikkeen napsautus (yhden sormen napautus ja pito)
  sisältyy nyt NVDA 2020.1:teen.

## Versio 20.01

* NVDA 2019.3 vaaditaan.
* Kosketustuen tilanvaihtokomento (kosketuksen läpivienti mukaan lukien) ei
  enää toimi, mikäli kosketustuki poistetaan kokonaan käytöstä.

## Versio 19.11

* Lisätty syöteohjeviestejä kosketuskomennoille.

## Versio 19.09

* Kosketustuki voidaan nyt poistaa käytöstä mistä tahansa, ei pelkästään
  muista kuin normaalista profiilista.

## Versio 19.07

* Sisäisiä muutoksia tulevien NVDA-versioiden tukemiseksi.

## Versio 18.12

* Sisäisiä muutoksia tulevien NVDA-versioiden tukemiseksi.

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
* Mikäli käytetään NVDA 2018.1:tä tai sitä uudempaa, Kosketuksen
  vuorovaikutus -vaihtoehto näkyy kahdesti Asetukset-valikossa. Toisena
  oleva eli alempi vaihtoehto avaa tämän lisäosan valintaikkunan.
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

[2]: https://addons.nvda-project.org/files/get.php?file=ets-dev
