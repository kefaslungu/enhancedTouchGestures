# unaprjeđene dodirne geste -enhanced touch gestures #

* Autor: Joseph Lee
* Preuzmi [stable version][1]
* Download [development version][2]

Ovaj dodatak omogućuje dodatne dodirničke geste u NVDA čitaču zaslona. Ovaj
dodatak također dodaje set dodirnih gesti za lakšu navigaciju u načinu
pregleda.

Note: this add-on requires NVDA 2017.4 or later running on a touchscreen
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

## Touch tipkovnica

Ako imate instaliran dodatak, dok tipkate po touch tipkovnici, trebate
dodirnuti dvaput kako biste pritisnuli tipku (tzv. mod standardnog
tipkanja). Ovo možete promijeniti u mod tipkanja jednim dodirom, gdje se
tipka pritisne čim podignete prst sa trenutno fokusirane tipke. To možete
učiniti ulaskom u NVDA izbornik/Postavke/Interakcija dodirom i odabirom
stavke Tipkanje jednim dodirom.

## Komanda za tipkanje jednim dodirom 

Možete koristiti dodatnu naredbu za korištenje dodirnih gesti dok NVDA nije
pokrenut. Morate definirati naredbu (koristeći dijaloški okvir Ulazne
dodirne geste u kategoriji Dodatne dodirne geste kako bisgte omogućili
korištenje ove značajke u intervalu do 10 sekundi te ručno uključivanje i
isključivanje ove značajke. Potom idite u NVDA izbornik/Postavke/Interakcija
dodirom i definirajte razmak između dodirnih komandi NVDA u intervalu između
3 i 10 sekundi (po zadanom je 5 sekundi).

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

[2]: http://addons.nvda-project.org/files/get.php?file=ets
