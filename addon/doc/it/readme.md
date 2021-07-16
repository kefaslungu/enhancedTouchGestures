# Enhanced Touch Gestures #

* Autore: Joseph Lee
* Scarica [versione stabile][1]
* NVDA compatibility: 2020.1 to 2021.1

Questo componente aggiuntivo fornisce gesti aggiuntivi per NVDA. Fornisce
inoltre gesti che facilitano la modalità navigazione.

Nota: questo componente aggiuntivo richiede NVDA 2020.1 o superiore
installato su un computer dotato di touchscreen, con sistema operativo
Windows 8.1 o 10.

## Comandi

### Disponibili ovunque

* doppio tap con 4 dita: attiva/disattiva modalità aiuto immissione.
* Flick con 4 dita verso destra: attiva/disattiva la tastiera virtuale a
  tocco (in genere la attiva).
* Control+Alt+NVDA+T: attiva/disattiva l'interazione a tocco.

### Modalità oggetti

* flick con Tre dita verso il basso: legge la finestra corrente.
* flick con Tre dita verso sinistra: legge l'oggetto che ha il focus.
* flick con 3 dita verso destra: legge l'oggetto corrente su cui si trova il
  navigatore.
* flick con 4 dita verso l'alto: legge il titolo della finestra corrente.
* flick con 4 dita verso il basso: legge il testo della barra di stato.

## Modalità tocco web

Questa modalità di tocco, disponibile in modalità navigazione, permette di
navigare un documento rispetto a un elemento selezionato. Per passare alla
modalità tocco web, da un documento in modalità navigazione, effettuare un
tocco con tre dita. Da questo momento, effettuando un flick verticale con un
dito si sceglieranno gli elementi in base ai quali spostarsi, mentre con un
flick verso destra o sinistra ci si sposterà all'elemento successivo o
precedente del tipo scelto. Quando si lascia la modalità navigazione, viene
utilizzata la modalità oggetti.

## Impostazioni sintetizzatore, modalità tocco

È possibile utilizzare questa modalità per modificare rapidamente le
impostazioni del sintetizzatore, come la scelta di una voce e cambiare il
volume. In questa modalità, utilizzare il flick con due dita verso sinistra
o destra per spostarsi tra le impostazioni del sintetizzatore e utilizzare
il flick con due dita in alto o in basso per cambiare i valori. Questi gesti
rispecchiano quelli per modificare al volo le impostazioni sintetizzatore da
tastiera.

## Novità nella versione 20.09

* Rimossa la possibilità che NVDA disattivi l'interazione a tocco per non
  più di dieci secondi (comando passa tocco a).
* Rimossa la funzionalità annuncio coordinate con beep.

## Novità nella versione 20.07

* Aggiunto un comando da tastiera per attivare/disattivare l'interazione a
  tocco o attivare/disattivare "passa tocco a" (Control+Alt+NVDA+T).
* Poiché NVDA 2020.1 e versioni successive include un comando a tocco per
  effettuare un click con il tasto destro del mouse (un tocco trattenuto con
  un dito), il comando è stato rimosso da questo add-on. In virtù di ciò, è
  richiesto NVDA 2020.1 e versioni successive.
* La possibilità che NVDA disattivi l'interazione a tocco per non più di
  dieci secondi (comando passa tocco a) è obsoleta. In futuro, questa
  funzionalità attiverà e disattiverà l'interazione a tocco.
* Nelle development snapshots di NVDA, a causa delle modifiche alla
  funzionalità interazione a tocco, il comando "passa tocco a" e la finestra
  impostazioni di Enhanced Touch Gestures saranno disabilitate. Il comando
  utilizzato per abilitare "passa tocco a" attiverà e disattiverà
  l'interazione a tocco.
* La funzionalità annuncio coordinate con beep è obsoleta e verrà rimossa in
  una prossima versione dell'add-on.
* L'annuncio coordinate con beep non si sentirà quando si usa la tastiera a
  tocco.
* NVDA non sembrerà più bloccato, né riprodurrà suoni di errore quando si
  utilizzano metodi di input moderni, come il pannello emoji, a tocco.
* NVDA mostrerà un messaggio di errore se la tastiera a tocco non può essere
  attivata (flick verso destra con quattro dita).

## Novità nella versione 20.06

* Risolti molti problemi legati allo stile del codice e bug potenziali con
  Flake8.

## Novità nella versione 20.04

* Il gesto "clic con il tasto destro del mouse" (toccare con un dito e
  tenere premuto)  è ora integrato in NVDA 2020.1.

## Novità nella versione 20.01

* E' richiesto NVDA 2019.3.
* Il comando che attiva e disattiva il supporto touch (compreso il comando
  per passare il gesto successivo al touchscreen) non funzionerà più se il
  supporto touch è disattivato completamente.

## Novità nella versione 19.11

* Aggiunti i messaggi di aiuto immissione per altri comandi touch.

## Novità nella versione 19.09

* Il supporto touch ora può essere disattivato ovunque, non solo da profili
  diversi dal profilo normale.

## Novità nella versione 19.07

* Modifiche interne per supportare le versioni future di NVDA.

## Novità nella versione 18.12

* Modifiche interne per supportare le versioni future di NVDA.

## Novità nella versione 18.08

* Compatibile con NVDA 2018.3 e versioni future.

## Novità nella versione 18.06

* Le impostazioni del componente aggiuntivo si trovano ora nella finestra
  multicategoria impostazioni di NVDA, alla categoria "enhanced Touch
  Gestures". Ne deriva che è necessario usare NVDA 2018.2.
* Risolti problemi di compatibilità con wxPython 4.

## Novità nella versione 18.04

* Risolve un problema in virtù del qwuale, nella categoria interazione a
  tocco nella finestra impostazioni di NVDA, si potevano sentire suoni di
  errore dovuti a modifiche apportate da questo add-on.

## Novità nella versione 18.03

* E' richiesto NVDA 2018.1.
* Poiché NVDA 2018.1 viene fornito con la casella di controllo digitazione a
  tocco, questa non è più inclusa in questo componente aggiuntivo.

## Novità nella versione 17.12

* Richiede NVDA 2017.4. Nello specifico, ora questo add-on può gestire i
  cambi di profilo di configurazione.
* Poiché NVDA 2017.4 include la vocalizzazione dell'orientamento dello
  schermo, questa caratteristica non fa più parte di questo add-on.
* Aggiunta una casella di controllo nascosta nella finestra Interazione a
  Tocco per disattivare completamente il supporto touch (disponibile se è
  attivo un profilo diverso dalla configurazione normale).
* Se si utilizza NVDA 2018.1 o superiore, la finestra Interazione a Tocco
  sarà elencata due volte nel menu preferenze di NVDA. Il secondo elemento è
  la finestra che viene fornita con il componente aggiuntivo.
* Nella finestra di dialogo Interazione a Tocco del componente aggiuntivo,
  la modalità tastiera touch non viene più mostrata se si utilizza NVDA
  2018.1 o superiore.

## Novità nella versione 17.10

* A causa delle politiche di supporto di Microsoft, Windows 8 (versione
  originale) non è più supportato.
* NVDA non vocalizzerà più due volte l'orientamento dello schermo quando si
  eseguono le snapshot di sviluppo di NVDA 2017.

## Novità nella versione 17.07.1

* Nella finestra di dialogo INterazione a Tocco, aggiunta un'opzione per
  attivare e disattivare manualmente il comando per passare il gesto
  successivo al touchscreen senza utilizzare un timer.
* Con il passaggio del gesto successivo al touchscreen manuale disattivato,
  se tale passaggio viene attivato prima della scadenza del tempo ad esso
  assegnato, l'interazione a tocco viene attivata.

## Novità nella versione 17.07

* Aggiunta una nuova finestra di dialogo chiamata Interazione a Tocco nel
  menu impostazioni di NVDA, per configurare come NVDA lavora con i
  touchscreen.
* Dopo aver installato questa versione, per premere tasti sulla tastiera
  touch, si deve toccare due volte il tasto desiderato. Si può tornare alla
  vecchia modalità attivando "digitazione a tocco" dalla finestra
  INterazione a Tocco.
* Aggiunto un comando non assegnato ad alcun gesto, che permette ad NVDA di
  ignorare i gesti touch per massimo 10 secondi.
* Aggiunta un'opzione nella finestra di dialogo Interazione a Tocco, per
  permettere ad NVDA di disattivare l'interazione a tocco per un tempo
  compreso tra 3 e 10 secondi, al fine di eseguire direttamente gesti
  touchscreen (come se NVDA non fosse in esecuzione; il default è 5
  secondi).
* Aggiunti i log dei messaggi di debug quando si eseguono clic destri (premi
  e tieni premuto), perché siano registrati nei log di NVDA (richiede NVDA
  2017.1 o successive).
* A causa di modifiche apportate alla funzione Coordinate Aurio, è
  necessario NVDA 2017.1 o successivo.

##Versione 17.03

* Risolto un problema che impediva la riproduzione delle coordinate audio
  con NVDA 2017.1 o successive.

##Versione 16.12

* La modalità tocco web funziona in Microsoft Edge, Microsoft Word e altri
  programmi dove viene usata la modalità navigazione.
* Aggiunti elenchi e punti di riferimento agli elementi disponibili in
  modalità tocco web.

## Novità nella versione 16.06

* Versione iniziale stabile.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets

[2]: https://addons.nvda-project.org/files/get.php?file=ets-dev
