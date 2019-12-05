# Dodatne dodirne geste (Enhanced touch gestures) #

* Autor: Joseph Lee
* Preuzmi [stabilnu verziju][1]
* NVDA kompatibilnost: 2018.2 do 2019.3

Ovaj dodatak omogućuje dodatne dodirne geste na ekranu za dodir u NVDA
čitaču. Ovaj dodatak također dodaje skup dodirnih gesti za lakšu navigaciju
u modusu čitanja.

Napomena: Dodatak zahtijeva NVDA 2018.2 ili noviji, instaliran na računalu
koje posjeduje ekran osjetljiv na dodir s instaliranim sustavom Windows 8.1
ili 10.

## Naredbe

### Svuda dostupne

* Dodir s četiri prsta: uključi ili isključi modus pomoći tijekom unosa.
* Dodirni i drži: izvodi desni klik na objektu pod prstom.
* Klizanje s četiri prsta u desno: uključi ili isključi dodirnu tastaturu
  (obično je uključuje).

### Objektni modus

* Klizanje s tri prsta prema dolje: čita trenutačni prozor.
* Klizanje s tri prsta u lijevo: izvještava o objektu koji ima fokus.
* Klizanje s tri prsta u desno: izvještava o trenutačnom navigacijskom
  objektu.
* Klizanje s četiri prsta prema gore: izgovara naslov trenutačnog prozora.
* Klizanje s četiri prsta prema dolje: čita tekst statusne trake.

## Dodirni modus za web

Ovaj dodirni modus – dostupan u modusu čitanja – omogućuje navigaciju po
označenom elementu. Za prebacivanje iz dokumenata u modusu čitanja u dodirni
modus za web, ekran treba dodirnuti s tri prsta. U ovom modusu, klizanjem
jednim prstom prema gore ili dolje prebacuje se između dostupnih modusa
navigacije po elementima. Klizanjem jednim prstom u desno ili u lijevo,
pomiče se na sljedeći ili prethodni element. Kad se izađe iz dokumenata u
modusu čitanja, koristi se dodirni modus za objekte.

## Postavke govorne jedinice u dodirnom modusu

Ovaj se modus koristiti za brzo mijenjenje postavki govorne jedinice, poput
odabira glasa ili promjene glasnoće. Klizanjem s dva prsta u lijevo ili
desno prelazi se između postavki govorne jedinice. Klizanjem s dva prsta
prema gore i dolje mijenjaju se vrijednosti. Ove su geste preslika prečaca s
tipkovnice.

## Izvještavanje koordinata zvukom

Ako je u postavkama miša aktivirana postavka „Reproduciraj koordinate miša”,
čut će se zvučni signali kao indikacija trenutačne koordinate ekrana kad se
koriste geste za istraživanje dodirom.

## Proslijeđivanje dodirne naredbe

Postoji nedodijeljena naredba za korištenje dodirnih gesti, kao da NVDA nije
pokrenut. Da bi se koristila, naredba se mora definirati (putem dijaloškog
okvira „Ulazne geste”) u kategoriji „Dodatne dodirne geste”, čime se
omogućuje korištenje ove naredbe u trajanju od do 10 sekundi. Naredbu je
moguće uključiti/isključiti i ručno. Zatim se putem NVDA
izbornik>Postavke>Interakcija dodirom, treba definirati pauza za dodirne
NVDA naredbe, u trajanju od 3 do 10 sekundi (standardno je postavljeno 5
sekundi).

## Verzija 19.11

* Dodane su poruke pomoći tijekom unosa za dodatne dodirne naredbe.

## Verzija 19.09

* Podrška za dodir se sad može svugdje isključiti, ne samo u profilima koji
  nisu normalni profili.

## Verzija 19.07

* Unutarnje promjene, kako bi se podržale buduća NVDA izdanja.

## Verzija 18.12

* Unutarnje promjene, kako bi se podržale buduća NVDA izdanja.

## Verzija 18.08

* Kompatibilno s NVDA 2018.3 i budućim verzijama.

## Verzija 18.06

* Postavke dodatka se sada nalaze u novom ekranu NVDA postavki s višestrukim
  kategorijama pod kategorijom „Dodatne dodirne geste”. Iz tog razloga je
  potreban NVDA 2018.2.
* Ispravljena greška kompatibilnosti s wxPython 4.

## Verzija 18.04

* Ispravljena greška gdje kategorija Interakcija dodirom u postavkama NVDA
  može prouzročiti reprodukciju zvukova greške zbog promjena u dodatku.

## Verzija 18.03

* Zahtijeva NVDA 2018.1.
* Budući da NVDA 2018.1 dolazi s potvrdnim okvirom za tipkanje dodirom, taj
  potvrdni okvir više nije uključen u ovaj dodatak.

## Verzija 17.12

* Zahtijeva NVDA 2017.4. Konkretno, ovaj dodatak sada podržava mijenjenje
  konfiguracijskih profila.
* S obzirom da NVDA verzija 2017.4 uključuje izvještavanje o orijentaciji
  ekrana, ova značajka više nije dio ovog dodatka.
* Dodan skriveni potvrdni okvir u dijaloškom okviru Interakcija dodirom,
  koji kompletno onemogućava podršku dodirom (dostupno je, ako su
  konfiguracijski profili aktivni koji nemaju uobičajenu konfiguraciju).
* Ako se koriste nedavno objavljene razvojne verzije NVDA čitača, dijaloški
  okvir „Interakcija dodirom” bit će prikazan dvaput u podizborniku NVDA
  postavki. Druga stavka je dijaloški okvir koji dolazi s dodatkom.
* U dijaloškom okviru Interakcija dodirom ovog dodatka, modus tipkanja
  dodirom više se ne prikazuje, ako koristite nedavno objavljene razvojne
  verzije NVDA.

## Verzija 17.10

* Zbog Microsoft pravila za podršku, Windows 8 (originalno izdanje) više
  nije podržan.
* NVDA više neće dvaput izvještavati o orijentaciji zaslona tijekom
  korištenja razvojnih verzija NVDA 2017.4.

## Verzija 17.07.1

* Dodana je opcija u dijaloškom okviru interakcije dodirom za uključivanje i
  isključivanje istraživanja jednim dodirom bez štoperice.
* Ako je ručno isključen mod istraživanja jednim dodirom, te ako je isti
  uključen prije nego što mod učenja istekne, interakcija dodirom će biti
  dostupna.

## Verzija 17.07

* Dodan je novi dijaloški okvir pod nazivom „Interakcija dodirom” u
  podizborniku NVDA postavki za definiranje načina rada NVDA čitača s
  ekranima osjetljivim na dodir.
* Nakon instaliranja ove verzije, prilikom pritiskanja tipki na dodirnoj
  tipkovnici, željena tipka se mora dodirnuti dvaput. Moguće je prebaciti se
  na stari način rada, aktiviranjem tipkanja dodirom u dijaloškom okviru
  Interakcija dodirom.
* Dodana je naredba (nedodijeljena) koja dozvoljava NVDA čitaču ignorirati
  dodirne geste u intervalu do 10 sekundi.
* Dodana je opcija u dijaloškom okviru interakcije dodirom koja dozvoljava
  NVDA čitaču zaustaviti interakciju dodirom u intervalu između 3 i 10
  sekundi, kako bi se direktno izvršile dodirne geste (kad NVDA nije
  pokrenut; standardno je 5 sekundi).
* Dodane su poruke za otkrivanje grešaka tijekom izvođenja desnog klika
  (dodirni i zadrži) i njihovo spremanje u NVDA log (zahtijeva NVDA verziju
  2017.1 ili noviju).
* Zbog promjena u reproduciranju koordinata ekrana, zahtijeva NVDA verziju
  2017.1 ili noviju.

##Verzija 17.03

* Riješen problem gdje se pri izvještavanju koordinata nije čuo zvuk ili se
  pojavljivao zvuk pogreške tijekom korištenja NVDA verzije 2017.1 ili
  novije.

##Verzija 16.12

* Dodirni modus za web radi u programu Microsoft Edge, Microsoft Word i
  drugdje gdje je moguće koristiti modus pretraživanja.
* Dodani su popisi i orijentiri za elemente u dodirnom modusu za web.

## Verzija 16.06

* Inicijalna stabilna verzija.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets

[2]: https://addons.nvda-project.org/files/get.php?file=ets-dev
