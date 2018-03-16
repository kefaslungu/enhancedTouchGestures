# Enhanced Touch Gestures #

* Autor: Joseph Lee
* Descărcați [versiunea stabilă][1]

Acest supliment oferă gesturi adiționale de atingere a ecranului pentru
NVDA. El de asemenea oferă un set de gesturi pentru o navigare mai ușoară.

Note: this add-on requires NVDA 2018.1 or later running on a touchscreen
computer with Windows 8.1 or 10.

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

Acest mod tactil web, disponibil în modul navigare, vă permite să parcurgeți
documentul prin elementul selectat. Pentru a comuta la modul web, din
documentele modului de navigare, efectuați o atingere cu 3 degete. Din acest
mod, glisând în sus sau în jos cu un deget 

## Setările sintetizatorului la modul de atingere

Aveți posibilitatea să utilizați acest mod pentru a modifica rapid setările
de sintetizator, cum ar fi alegerea unei voci și modificarea volumului. În
acest mod, utilizați glisarea cu două degete spre stânga sau spre dreapta
pentru a vă deplasa între setările sintetizatorului și utilizați gesturile
glisare cu două degete sus și jos pentru a modifica valorile. 

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

## Disable touch support in profiles

If profiles other than normal configuration is active and if you go to Touch
Interaction dialog, you'll see a checkbox named "completely disable touch
support". Checking this box and answering yes if prompted will completely
turn off touch support for that profile. This is useful in apps that provide
their own touch commands. To restore touch functionality, either uncheck
this checkbox or manually toggle touch passthrough.

## Version 18.03

* NVDA 2018.1 is required.
* Because NVDA 2018.1 comes with touch typing checkbox, the checkbox is no
  longer included in this add-on.

## Versiunea 17.12

* Requires NVDA 2017.4. Specifically, this add-on can now handle
  configuration profile switches.
* As NVDA 2017.4 includes screen orientation announcement, this feature is
  no longer part of this add-on.
* Added a hidden checkbox in Touch Interaction dialog to completely disable
  touch support (available if profiles other than normal configuration is
  active).
* If using NVDA 2018.1 or later, Touch Interaction dialog will be listed
  twice under NvDA's preferences menu. The second item is the dialog that
  comes with the add-on.
* In Touch Interaction dialog for the add-on, touch typing mode is no longer
  shown if using NVDA 2018.1 or later.

## Versiunea 17.10

* Due to support policy from Microsoft, Windows 8 (original release) is no
  longer supported.
* NVDA will no longer announce screen orientation twice when running NVDA
  2017.4 development snapshots.

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
