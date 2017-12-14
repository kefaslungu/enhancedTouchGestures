# Laajennetut kosketuseleet #

* Tekijä: Joseph Lee
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tämä lisäosa tarjoaa lisää kosketuseleitä NVDA:han. Mukana on eleitä myös
helpompaa selaustilanavigointia varten.

Note: this add-on requires NVDA 2017.4 or later running on a touchscreen
computer with Windows 8.1 or 10.

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

## Kosketusnäppäimistö

Kun tämä lisäosa on asennettuna, kosketusnäppäimistöllä kirjoitettaessa on
tehtävä kaksoisnapautus näppäinten painamiseksi (kutsutaan
standardikirjoitukseksi). Voit muuttaa tämän kosketuskirjoitukseksi (jossa
sormi nostetaan näppäimeltä, jolloin sitä painetaan) valitsemalla
NVDA-valikosta Asetukset/Kosketuksen vuorovaikutus ja valitsemalla
kosketuskirjoitus-valintaruudun.

## Kosketuskomentojen läpivienti

Käytettävissä on määrittämätön komento, joka mahdollistaa kosketuseleiden
käytön enintään kymmenen sekunnin ajan tai manuaalisesti ikään kuin NVDA ei
olisi käynnissä. Voit käyttää tätä määrittämällä komennon
Syötekomennot-valintaikkunan Laajennetut kosketuseleet
-kategoriasta. Valitse tämän jälkeen NVDA-valikosta Asetukset/Kosketuksen
vuorovaikutus ja määritä asetuksen "Keskeytä NVDA:n kosketuskomento" arvoksi
jotain kolmen ja kymmenen sekunnin väliltä (oletus on 5).

## Disable touch support in profiles

If profiles other than normal configuration is active and if you go to Touch
Interaction dialog, you'll see a checkbox named "completely disable touch
support". Checking this box and answering yes if prompted will completely
turn off touch support for that profile. This is useful in apps that provide
their own touch commands. To restore touch functionality, either uncehck
this checkbox or manually toggle touch passthrough.

## Version 17.12

* Requires NVDA 2017.4. Specifically, this add-on can now handle
  configuration profile switches.
* As NVDA 2017.4 includes screen orientation announcement, this feature is
  no longer part of this add-on.
* Added a hidden checkbox in Touch Interaction dialog to completely disable
  touch support (available if profiles other than normal configuration is
  active).
* If using recent NVDA development snapshots, Touch Interaciotn dialog will
  be listed twice under NvDA's preferences menu. The second item is the
  dialog that comes with the add-on.
* In Touch Interaction dialog for the add-on, touch typing mode is no longer
  shown if using recent NVDA development snapshots.

## Version 17.10

* Due to support policy from Microsoft, Windows 8 (original release) is no
  longer supported.
* NVDA will no longer announce screen orientation twice when running NVDA
  2017.4 development snapshots.

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
