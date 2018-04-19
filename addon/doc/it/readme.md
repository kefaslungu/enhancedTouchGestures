# Enhanced Touch Gestures #

* Autore: Joseph Lee
* Download [versione stabile][1]

Questo componente aggiuntivo fornisce gesti aggiuntivi per NVDA. Fornisce
inoltre gesti che facilitano la modalità esplorazione

Note: this add-on requires NVDA 2018.1 or later running on a touchscreen
computer with Windows 8.1 or 10.

## Comandi

### Disponibili ovunque

* doppio tap con 4 dita: attiva modalità aiuto immissione dati
* Toccare e tenere premuto: effettua clic destro sull'oggetto sotto il dito.
* 4 dita verso destra: attiva/disattiva la tastiera virtuale a tocco (in
  genere la attiva).

### Modalità oggetti

* Tre dita verso il basso: legge la finestra corrente.
* Tre dita verso sinistra: legge l'oggetto che ha il focus.
* 3 dita verso destra: legge l'oggetto corrente del navigatore.
* 4 dita verso l'alto: legge il titolo della finestra corrente.
* 4 dita verso il basso: legge il testo della barra di stato.

## Modalità tocco web

Questa modalità di tocco, disponibile in modalità navigazione, permette di
esplorare un documento tramite un elemento selezionato. Per andare in
modalità web, da un documento in modalità esplorazione, effettuare un tocco
con tre dita. Da questo momento, effettuando un movimento verticale con un
dito si scorreranno gli elementi disponibili, mentre con un movimento verso
destra o sinistra si scorreranno quelli selezionati.

## Impostazioni sintetizzatore, modalità tocco

È possibile utilizzare questa modalità per modificare rapidamente le
impostazioni del sintetizzatore, come la scelta di una voce e cambiare il
volume. In questa modalità, utilizzare due dita verso sinistra o destra per
spostarsi tra le impostazioni del sintetizzatore e utilizzare due dita
verticalmente per cambiare i valori.

## Annuncio coordinate con beep

Questa opzione funziona se sono state abilitate le coordinate mouse dalle
impostazioni di NVDA.

## Touch command passthrough

An unassigned command is available to allow you to use touchscreen gestures
as though NVDA is not running. In order to use this, you need to assign a
command (via Input Gestures dialog) under Enhanced Touch Gestures category
to let you do this for up to ten seconds or toggle this manually. Then go to
NVDA menu/Preferences/Touch Interaction, then configure pause NVDA's touch
command value between 3 to 10 seconds (default is 5 seconds).

## Disable touch support in profiles

If profiles other than normal configuration is active and if you go to Touch
Interaction dialog, you'll see a checkbox named "completely disable touch
support". Checking this box and answering yes if prompted will completely
turn off touch support for that profile. This is useful in apps that provide
their own touch commands. To restore touch functionality, either uncheck
this checkbox or manually toggle touch passthrough.

## Version 18.04

* Resolves an issue where touch interaction category in NVDA Settings panel
  may cause error sounds to be heard due to changes made from this add-on.

## Version 18.03

* NVDA 2018.1 is required.
* Because NVDA 2018.1 comes with touch typing checkbox, the checkbox is no
  longer included in this add-on.

## Version 17.12

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

## Version 17.10

* Due to support policy from Microsoft, Windows 8 (original release) is no
  longer supported.
* NVDA will no longer announce screen orientation twice when running NVDA
  2017.4 development snapshots.

## Version 17.07.1

* Added an option in touch interaction dialog to manually toggle touch
  passthrough without use of a timer.
* With manual passthrough mode off, if touch passthrough is turned on before
  the passthrough duration expires, touch interaction would be enabled.

## Version 17.07

* Added a new dialog named Touch Interaction under NVDA's preferences menu
  to configure how NVDA works with touchscreens.
* After installing this version, when pressing keys on the touch keyboard,
  one must double tap the desired key. You can switch back to the old way by
  enabling touch typing from Touch Interaction dialog.
* Added a command (unassigned) to allow NVDA to ignore touch gestures for up
  to 10 seconds.
* Added an option in Touch Interaction dialog to allow NVDA to pause touch
  interaction between 3 to 10 seconds in order to perform touchscreen
  gestures directly (as though NVDA is not running; default is 5 seconds).
* Added debug logging messages when performing right clicks (tap and hold)
  to be recorded in the NVDA log (requires NVDA 2017.1 or later).
* Due to changes made when playing screen coordinates, NVDA 2017.1 or later
  is required.

##Version 17.03

* Risolto un problema che impediva la riproduzione delle coordinate audio
  con NVDA 2017.1 o successive.

##Version 16.12

* La modalità web a tocco funziona in Microsoft Edge, Microsoft Word e altri
  programmi dove viene usata la modalità navigazione.
* Aggiunti elenchi e punti di riferimento agli elementi web in modalità
  tocco

## Versione 16.06

* Versione iniziale stabile

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets
