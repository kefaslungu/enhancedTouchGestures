# unaprjeđene dodirne geste -enhanced touch gestures #

* Autor: Joseph Lee
* Preuzmi [stable version][1]

Ovaj dodatak omogućuje dodatne dodirničke geste u NVDA čitaču zaslona. Ovaj
dodatak također dodaje set dodirnih gesti za lakšu navigaciju u načinu
pregleda.

Note: this add-on requires NVDA 2018.1 or later running on a touchscreen
computer with Windows 8.1 or 10.

## Komande

### Dostupne svugdje

* četveroprstni dodir : uključi /isključi pomoč pri unosu.
* dodirni i drži: izvodi desni klik na objektu pod vašim prstom.
* Prevlačenje sa 4 prsta desno: uključuje i isključuje touch tastaturu
  (obično je uključuje).

### Objektni način

* troprstno klizanje prema dolje: čitanje trenutnog prozora.
* troprstno klizanje lijevo: izvještava o objektu koji ima fokus.
* troprstno klizanje u desno: izvještava o trenutnom objektu navigatora.
* četveroprstno klizanje prema gore: izgovara naslov trenutnog prozora.
* četveroprstno klizanje prema dolje: čita tekst statusne trake.

## Dodirni način za web

Ovaj dodirni način, dostupan u načinu pregleda, omogućava vam navigaciju po
označenom elementu. Da biste se prebacili u dodirni način za web, iz
dokumenata načina pregleda, izvedite troprstni dodir. iz ovog načina,
klizanje u lijevo ili desno jednim prstom prebacuje između dostupnih načina
navigacije - kretanja, dok se krećete desno ili lijevo jednim prstom pomiće
se na slijedeći ili prethodni element, doista. Jednom kad izađete iz
dokumenta načina pregleda, koristi se način objekta.

## dodirni način postavki govorne jedinice

Možete koristiti ovaj način kako biste brzo promijenili postavke govorne
jedinice poput odabira glasa ili promjene glasnoće. U ovom načinu, koristite
dvoprstno klizanje u lijevo ili desno kako biste se pomicali između postavki
govorne jedinice i koristite klizanje prstom u desno gore i dolje kako biste
promijenili vrijednosti. Ove su geste preslik prečaca sa tipkovnice.

## Izvještavanje koordinata zvukom

Ako ste omogućili postaku reproduciraj zvukove prilikom pomicanja miša u
postavkama miša, čut ćete zvučne signale kako biste čuli indikaciju zaslona
kad pozovete geste za istraživanje dodirom.

## Komanda za tipkanje jednim dodirom 

Možete koristiti dodatnu naredbu za korištenje dodirnih gesti dok NVDA nije
pokrenut. Morate definirati naredbu (koristeći dijaloški okvir Ulazne
dodirne geste u kategoriji Dodatne dodirne geste kako bisgte omogućili
korištenje ove značajke u intervalu do 10 sekundi te ručno uključivanje i
isključivanje ove značajke. Potom idite u NVDA izbornik/Postavke/Interakcija
dodirom i definirajte razmak između dodirnih komandi NVDA u intervalu između
3 i 10 sekundi (po zadanom je 5 sekundi).

## Onemogući podršku za dodir u profilima 

If profiles other than normal configuration is active and if you go to Touch
Interaction dialog, you'll see a checkbox named "completely disable touch
support". Checking this box and answering yes if prompted will completely
turn off touch support for that profile. This is useful in apps that provide
their own touch commands. To restore touch functionality, either uncheck
this checkbox or manually toggle touch passthrough.

## Version 18.04

* Ispravljena greška gdje kategorija Interakcija dodirom u postavkama NVDA
  može uzrokovati reprodukciju zvukova greške zbog promjena u dodatku.

## Version 18.03

* Zahtijeva NVDA 2018.1
* Zbog toga što NVDA 2018.1 dolazi s potvrdnim okvirom za tipkanje dodirom,
  taj potvrdni okvir više nije uključen u ovaj dodatak.

## Version 17.12

* Zahtijeva NVDA 2017.4. Konkretno, ovaj dodatak sada može pratiti
  prebacivanje između konfiguracijskih profila.
* S obzirom da NVDA inačica 2017.4 uključuje izvještavanje o orijentaciji
  zaslona, ova značajka više nije dio ovog dodatka.
* Dodan skriveni potvrdni okvir u dijaloškom okviru Interakcija dodirom koji
  kompletno onemogućava podršku dodirom (dostupno je ako su aktivni
  konfiguracijski profili koji nemaju uobičajenu konfiguraciju).
* If using NVDA 2018.1 or later, Touch Interaction dialog will be listed
  twice under NvDA's preferences menu. The second item is the dialog that
  comes with the add-on.
* In Touch Interaction dialog for the add-on, touch typing mode is no longer
  shown if using NVDA 2018.1 or later.

## Version 17.10

* Zbog politike podrške tvrtke Microsoft, Windows 8 (originalno izdanje)
  više nije podržan.
* NVDA više neće dvaput izvještavati o orijentaciji zaslona tijekom
  korištenja razvojnih inačica NVDA 2017.4.

## Version 17.07.1

* Dodana je opcija u dijaloškom okviru interakcije dodirom za uključivanje i
  isključivanje istraživanja jednim dodirom bez štoperice.
* Ako je ručno isključen mod istraživanja jednim dodirom, te ako je isti
  uključen prije nego što mod učenja istekne, interakcija dodirom će biti
  dostupna.

## Version 17.07

* Dodan je novi dijaloški okvir pod nazivom Interakcija dodirom u
  podizborniku postavki NVDA za definiranje kako će NVDA raditi sa zaslonima
  osjetljivim na dodir.
* Naqkon što instalirate ovu verziju, dok pritiščete tipke na touch
  tipkovnici, jednu željenu tipku morate dvaput dodirnuti. Možete se vratiti
  na stari način rada omogućavanjem tipkanja jednim dodirom iz dijaloškog
  okvira Interakcija dodirom.
* Dodana je naredba (neraspoređena) koja dozvoljava NVDA da ignorira dodirne
  geste u intervalu do 10 sekundi.
* Dodana je opcija u dijaloškom okviru interakcije dodirom koja dozvoljava
  NVDA da zaustavi interakciju dodirom u intervalu između 3 i 10 sekundi
  kako bi se direktno izvršile dodirne geste (kada NVDA nije pokrenut; po
  zadanom je 5 sekundi).
* Dodane poruke za otkrivanje grešaka tijekom izvođenja desnog klika
  (dodirni i zadrži) i njihovo pohranjivanje u NVDA log (zahtijeva NVDA
  inačicu 2017.1
* Implementirane promjene za prikazivanje koordinata na zaslonu zahtijevaju
  NVDA inačicu 2017.1 ili noviju.

##Version 17.03

* Riješen problem gdje se pri izvještavanju koordinata nije čuo zvuk ili se
  pojavljivao zvuk pogreške tijekom korištenja NVDA inačice 2017.1 ili
  novije.

##Version 16.12

* Web dodirni mod radi u programu Microsoft Edge, Microsoft Word i drugdje
  gdje je moguće koristiti mod pretraživanja.
* Dodani su popisi i orijentiri za elemente u web dodirnom okruženju.

## Inačica 16.06

* Inicijalna stabilna verzija.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ets
