# Enhanced Touch Gestures #

* Autor: Joseph Lee
* Descărcați [versiunea stabilă][1]

Acest supliment oferă gesturi adiționale de atingere a ecranului pentru
NVDA. El de asemenea oferă un set de gesturi pentru o navigare mai ușoară.

Rețineți că aveți nevoie de NVDA 2018.1 sau mai nou instalat pe un computer
cu touchscreen care rulează Windows 8.1 sau 10.

## Comenzi

### Disponibile oriunde

* Atingere dublă cu 4 degete: comută modul de intrare al ajutorului.
* Țineți apăsat: efectuează clic dreapta pe obiect sub degetul
  dumneavoastră.
* Glisare la dreapta cu 4 degete: comută tastatura tactilă (de obicei o
  activează).

### Mod obiect

* Glisare în jos cu 3 degete: citește fereastra curentă.
* Glisare la stânga cu 3 degete: anunță obiectul curent cu focalizarea.
* Glisare la dreapta cu 3 degete: anunță obiectul navigator curent.
* Glisare în sus cu 4 degete: anunță titlul ferestrei curente.
* Glisare în jos cu 4 degete: anunță textul barei de stare.

## Mod tactil web

Acest mod tactil, disponibil în modul navigare, vă permite să parcurgeți
documentul prin elementul selectat. Pentru a comuta la modul web din
documentele modului de navigare, efectuați o atingere cu 3 degete. Din acest
mod, glisând în sus sau în jos cu un deget prin intermediul modurilor de
navigare a elementelor disponibile, în timp ce faceți clic dreapta sau
stânga cu un deget se deplasează la elementul următor sau anterior ales.După
ce vă îndepărtați de documentele de navigare, este utilizat modul de
atingere a obiectului.

## Setările sintetizatorului la modul de atingere

Aveți posibilitatea să utilizați acest mod pentru a modifica rapid setările
de sintetizator, cum ar fi alegerea unei voci și modificarea volumului. În
acest mod, utilizați glisarea cu două degete spre stânga sau spre dreapta
pentru a vă deplasa între setările sintetizatorului și utilizați gesturile
glisare cu două degete sus și jos pentru a modifica valorile. Aceste gesturi
reflectă asta în comenzile setărilor sintezei pe tastatură.

## Coordonată anunț bip

Dacă ați activat redarea coordonatelor mausului în setările acestuia, auziți
bipuri pentru a indica coordonata curentă a ecranului atunci când invocați
gesturile de explorare ale atingerii.

## Comanda de atingere passthrough

O comandă neatribuită este disponibilă pentru a vă permite să utilizați
gesturi de pe ecranul tactil ca și când NVDA nu se execută. Pentru a utiliza
acest lucru, trebuie să atribuiți o comandă (prin dialogul Gesturi de
intrare) sub categoria „gesturi de atingere îmbunătățite” pentru a vă
permite să faceți acest lucru timp de până la zece secunde, apoi mergeți la
meniul NVDA/Preferințe/Interacțiunea prin atingere, apoi configurați pauza
valorii comenzii de atingere NVDA între 3 și 10 secunde (valoarea implicită
este de 5 secunde).

## Dezactivează suportul tactil în profiluri

Dacă sunt active alte profiluri decât configurația obișnuită și dacă
accesați dialogul Interacțiune cu atingere, veți vedea o casetă de bifat
„dezactivează complet asistența tactilă”. Dacă bifați această casetă și
răspundeți da, în cazul în care vi se solicită, suportul tactil va fi
dezactivat complet. Acest lucru este util în aplicațiile care oferă
propriile comenzi de atingere. Pentru a restabili funcționalitatea tactilă,
debifați această casetă sau comutați manual la trecerea prin atingere.

## Versiunea 18.03

* Este necesar NVDA 2018.1.
* Fiindcă NVDA 2018.1 vine la pachet cu caseta de bifat „„scriere tactilă”,
  ea nu mai este inclusă în acest supliment.

## Versiunea 17.12

* Necesită NVDA 2017.4. De specificat: acest supliment poate gestiona acum
  comutările configurații profilurilor.
* Întrucât NVDA 2017.4 include anunțarea orientării ecranului, această
  caracteristică nu mai face parte din supliment.
* S-a adăugat o casetă de bifat ascunsă în dialogul interacțiunii tactile
  pentru dezactivarea completă a suportului tactil (disponibilă dacă sunt
  active alte profiluri decât configurația obișnuită).
* Dacă utilizați NVDA2018.1 sau mai nou, dialogul interacțiunii tactile va
  fi listat de două ori în submeniul de preferințe al NVDA-ului. Al doilea
  element este dialogul care vine la pachet cu suplimentul.
* În dialogul interacțiunii tactile pentru supliment, modul de scriere
  tactilă nu mai este afișat dacă se utilizează NVDA 2018.1 sau mai nou.

## Versiunea 17.10

* Datorită politicii de asistență de la Microsoft, Windows 8 (versiunea
  originală) nu mai este suportată.
* NVDA nu va mai anunța orientarea ecranului de două ori atunci când se
  rulează versiuni de dezvoltare snapshot NVDA 2017.4.

## Versiunea 17.07.1

* A fost adăugată o opțiune în dialogul de interacțiune prin atingere pentru
  comutarea manuală între activarea și dezactivarea trecerii prin atingere
  fără utilizarea unui cronometru.
* Cu opțiunea de trecere manuală dezactivată, dacă trecerea prin atingere
  este activat înainte de expirarea duratei de trecere, atingerea
  interacțiunii va fi activată.

## Versiunea 17.07

* A fost adăugat un nou dialog numit Interacțiunea prin atingere în meniul
  de preferințe al NVDA-ului pentru a configura cum să lucreze NVDA-ul cu
  ecranele tactile.
* După instalarea acestei versiuni, atunci când apăsați tastele de pe
  tastatura tactilă, trebuie să atingeți dublu tasta dorită. Puteți reveni
  la modul vechi, permițând introducerea de atingeri din dialogul
  Interacțiune prin atingere.
* A fost adăugată o comandă (neatribuită) pentru a-i permite NVDA-ului să
  ignore gesturile de atingere timp de 10 secunde.
* A fost adăugată o opțiune în dialogul Interacțiunea prin atingere pentru a
  permite NVDA să întrerupă interacțiunea tactilă între 3 și 10 secunde
  pentru a efectua direct gesturile de pe ecranul tactil (ca și când NVDA nu
  se execută, implicit este de 5 secunde).
* Au fost adăugate mesajele de diagnosticare la efectuarea click-urilor
  dreapta (atingeți și țineți apăsat) pentru a fi înregistrate în jurnalul
  NVDA (necesită NVDA 2017.1 sau mai nou).
* Datorită schimbărilor făcute la redarea coordonatelor ecranului, NVDA
  2017.1 este necesar.

#Versiunea 17.03

* A fost reparată o eroare în care bipul anunțării coordonatelor nu era
  redat, iar în locul lui o eroare de ton era redată la utilizarea NVDA
  2017.1 sau mai nou.

##Versiunea 16.12

* Modul tactil web funcționează în Microsoft Edge, Microsoft Word, și altele
  unde unde modul navigare este folosit.
* Au fost adăugate liste și puncte de reper pentru elementele modului tactil
  web.

## Versiunea 16.06

* Versiunea stabilă inițială.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets
