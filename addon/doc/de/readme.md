# Erweiterte Berührungs-Gesten #

* Autor: Joseph Lee
* Herunterladen der [stabilen Version][1]
* [Testversion herunterladen][2]

Diese Erweiterung führt zusätzliche Touchscreen-Gesten in NVDA ein. Ein Satz
von Touchscreen-Gesten für den Lesemodus ist ebenfalls verfügbar.

Note: this add-on requires NVDA 2017.4 or later running on a touchscreen
computer with Windows 8.1 or 10.

## Befehle

### Überall verfügbar

* Mit vier Fingern zweimal tippen: Eingabehilfe ein-/ausschalten.
* Tippen und halten: Führt einen Rechtsklick auf dem objekt unter Ihrem
  Finger aus.
* Mit vier Fingern nach rechts streichen: Aktiviert die Bildschirmtastatur.

### Objektmodus

* Mit drei Fingern nach unten streichen: Aktuelles Fenster vorlesen.
* Mit drei Fingern nach links streichen: Fukussiertes Objekt ausgeben.
* Mit drei Fingern nach rechts streichen: Aktuelles Navigator-Objekt
  ausgeben.
* Mit vier Fingern nach oben streichen: Titelleiste ansagen.
* Mit vier Fingern nach unten streichen: Statusleiste ansagen.

## Web-Touch-Modus

In diesem Modus können Sie Elemente im Lesemodus auswählen. Um in den
Web-Touch-Modus zu wechseln, tippen Sie mit drei Fingern.

## Modus für Spracheinstellungen

In diesem Modus können Sie Spracheinstellungen wie Tonhöhe, Geschwindigkeit
oder Lautstärke ändern. Um zwischen den einstellungen zu wechseln, streichen
Sie mit 2 Fingern nach links oder rechts. Um eine Einstellung zu ändern,
streichen Sie mit 2 Fingern nach oben oder unten. Diese einstellungen ähneln
den Tastenkombinationen für den Synthesizer-Einstellungsring.

## Signalton für Koordinaten

Wenn der Signalton für Mauskoordinaten in den Mauseinstellungen aktiviert
ist, hören Sie Signaltöne, während Sie den Bildschirm erkunden.

## Touch-Tastatur

Wenn die Erweiterung installiert ist, müssen Sie beim Tippen auf der
Touch-Tastatur einen Doppeltipp ausführen, um die Zeichen einzutragen (so
genannte Standardeingabe). Sie können die Eingabe auf "Tippen beim Berühren"
oder touch typing umstellen. Dabei wird das Zeichen eingetragen, wenn sie
den Finger von der Taste wegnehmen. Touch typing können Sie aktivieren,
indem Sie im NVDA-Menü unter Einstellungen/Touch-Interaction gehen und das
Kontrollkästchen für das Tippen auf Berührung aktivieren.

## Touch-Befehl durchreichen

Es steht ein nicht zugewiesener Befehl zur Verfügung, mit dem Sie
Touchscreen-Gesten so verwenden können, als ob NVDA beendet wäre. Um dies
nutzen zu können, müssen Sie im Dialog Eingaben unter der Kategorie
erweiterte Berührungsgesten einen Befehl zuweisen. Mit diesem Befehl können
Sie bis zu zehn Sekunden lang diese Funktion nutzen. Die Zeit können Sie
auch manuell umschalten. Gehen Sie dazu in das
NVDA-Menü/Einstellungen/Touch-Interaction und konfigurieren Sie die
Pausenzeit für den Touch-Befehlswert von NVDA zwischen 3 und 10 Sekunden
(Standard ist 5 Sekunden).

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

* Eine Option im Dialogfeld für die Touch-Interaction wurde hinzugefügt, um
  das Durchreichen von  Touch-Gesten ohne Verwendung eines Timers manuell
  umzuschalten.
* Bei ausgeschaltetem manuellen Durchreichmodus würde die Touch-Interaction
  aktiviert werden, wenn das manuelle Durchreichen der Befehle vor dem
  ablaufen der Durchreichezeit eingeschaltet wird.

## Version 17.07

* Ein neues Dialog namens Touch-Interaction wurde unter NVDA-Menü /
  Einstellungen hinzugefügt, um das Verhalten von NVDA während der Nutzung
  von Touchscreens zu konfigurieren.
* Nach der Installation dieser Version muss man beim Drücken von Tasten auf
  der Touch-Tastatur die gewünschte Taste doppelt antippen. Sie können auf
  die alte Art und Weise zurückschalten, indem Sie die Touch-Typing-Eingabe
  im Dialogfeld"Touch-Interaction" aktivieren.
* Ein neuer, noch nicht zugewiesener Befehl wurde hinzugefügt, welcher die
  Berührungsgeste bis zu 10 Sekunden an das Gerät / die Anwendung
  durchreicht.
* Es wurde eine neue Option im Dialogfeld Touch-Interaction hinzugefügt. Sie
  erlaubt NVDA die Touch-Interaction zwischen 3 und 10 Sekunden
  durchzureichen, um Touchscreen-Gesten direkt auszuführen (als ob NVDA
  beendet wäre). Der Standardwert liegt bei 5 Sekunden.
* Debug-Logging-Meldungen werden nun beim Ausführen von Rechtsklicks (Tippen
  und Halten) im NVDA-Protokoll aufgezeichnet. Erfordert NVDA 2017.1 oder
  höher.
* Aufgrund von Änderungen bei der Wiedergabe von Bildschirmkoordinaten ist
  NVDA 2017.1 oder höher erforderlich.

##Version 17.03

* Ein problem wurde behoben, wo bei der Verwendung von NVDA 2017.1 oder
  höher der Piepton der Koordinatenansage nicht abgespielt oder ein Fehler
  wiedergegeben wurde.

##Version 16.12

* Web-Touch-Modus funktioniert in allen Anwendungen, wo der Lesemodus
  (browse mode) unterstützt wird. Dies sind beispielsweise Microsoft Edge,
  Microsoft Word, Kindle, Firefox usw.
* Listen und Sprungmarken sind nun Teile der Web-Touch-Elemente.

## Version 16.06

* Ehrstveröffentlichung der stabilen Version.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ets

[2]: http://addons.nvda-project.org/files/get.php?file=emo-dev
