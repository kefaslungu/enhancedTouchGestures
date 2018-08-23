# Erweiterte Touch-Gesten #

* Autor: Joseph Lee
* Herunterladen der [stabilen Version][1]

Diese Erweiterung führt zusätzliche Touchscreen-Gesten in NVDA ein. Neue
Touchscreen-Gesten für den Lesemodus sind ebenfalls verfügbar.

Hinweis: Diese Erweiterung benötigt NVDA 2018.2 oder höher auf einem
Touchscreen-Computer mit Windows 8.1 oder 10.

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

In diesem Modus können Sie Elementtypen im Lesemodus auswählen und zwischen
Elementen des ausgewählten Elementtyps navigieren. Um in den Webmodus zu
wechseln, tippen Sie aus dem Lesemodus mit 3 Fingern auf dem Bildschirm. Von
diesem Modus aus können Sie mit einem Finger nach oben oder unten durch die
verfügbaren Elementtypen blättern, während Sie mit einem Finger nach rechts
oder links zum nächsten bzw. vorherigen Element des ausgewählten Elementtyps
gelangen. Sobald Sie das Dokument im Lesemodus beenden bzw. zu einem anderen
Fenster wechseln, wo der Lesemodus deaktiviert oder nicht verfügbar ist,
wird automatisch die Objektnavigation aktiviert.

## Modus für Sprachausgabeneinstellungen

In diesem Modus können Sie Sprachausgabeneinstellungen wie Tonhöhe,
Geschwindigkeit oder Lautstärke ändern. Um zwischen den einstellungen zu
wechseln, streichen Sie mit 2 Fingern nach links oder rechts. Um eine
Einstellung zu ändern, streichen Sie mit 2 Fingern nach oben oder
unten. Diese Gesten ähneln den Tastenkombinationen für Einstellungen im
Einstellungsring (STRG+Umschalt+NVDA+Pfeiltasten).

## Signalton für Koordinaten

Wenn der Signalton für Mauskoordinaten in den Mauseinstellungen aktiviert
ist, hören Sie beim Erkunden des Bildschirms entsprechende Töne.

## Touch-Befehl durchreichen

Es steht ein nicht zugewiesener Befehl zur Verfügung, mit dem Sie
Touchscreen-Gesten so verwenden können, als ob NVDA beendet wäre. Dafür
müssen Sie im Dialog Eingaben unter der Kategorie erweiterte
Berührungsgesten einen Tastaturbefehl zuweisen. Mit diesem Befehl können Sie
bis zu zehn Sekunden lang diese Funktion nutzen. Die Zeit können Sie auch
manuell umschalten. Gehen Sie dazu in das
NVDA-Menü/Einstellungen/Touch-Interaction und konfigurieren Sie die
Pausenzeit für den Touch-Befehlswert von NVDA zwischen 3 und 10 Sekunden
(Standard ist 5 Sekunden).

## Deaktivieren der Unterstützung für NVDA Touch-Gesten in benutzerdefinierten Konfigurationsprofilen

Wenn benutzerdefinierte Profile aktiv sind und Sie zum Dialogfeld
Touch-Interaktion gehen, sehen Sie ein Kontrollkästchen mit dem Namen
"Unterstützung für Touch-Interaktion vollständig deaktivieren". Wenn Sie
dieses Kontrollkästchen aktivieren und mit Ja antworten, wird die
Touch-Unterstützung für das aktuelle Konfigurationsprofil vollständig
deaktiviert. Dies ist in Anwendungen mit eigenen Touch-Befehlen nützlich. Um
die Touch-Funktionalität von NVDA wieder zu aktivieren, deaktivieren Sie
entweder dieses Kontrollkästchen oder schalten Sie das Durchreichen der
Touch-Gesten manuell ein.

## Version 18.08

* Kompatibel mit NVDA 2018.3 und zukünftigen Versionen.

## Version 18.06

* Einstellungen für die Erweiterung finden Sie nun im neuen
  NVDA-Einstellungsbildschirm unter der Kategorie "Erweiterte
  Touch-Gesten". Daher ist NVDA 2018.2 erforderlich.
* Kompatibilitätsprobleme mit wxPython 4 behoben.

## Version 18.04

* Behebt ein Problem, bei dem die Touch-Interaktionskategorie im
  NVDA-Einstellungsfenster aufgrund von vorgenommenen Änderungen durch die
  Erweiterung zu Fehlertönen führen kann.

## Version 18.03

* NVDA 2018.1 ist erforderlich.
* Das Kontrollkästchen "Tippen auf Berührung" ist nun im NVDA selbst
  integriert, deshalb wurde dieses Kontrollkästchen aus der Erweiterung
  ausgegliedert.

## Version 17.12

* Erfordert NVDA 2017.4. Diese Erweiterung unterstützt nun auch das Wechseln
  der Konfigurationsprofile im NVDA.
* Da NVDA 2017.4 die Ansage der Bildschirmausrichtung  enthält, ist diese
  Funktion nicht mehr Bestandteil der Erweiterung.
* Ein verstecktes Kontrollkästchen im Dialogfeld"Touch-Interaktion" wurde
  hinzugefügt, um die Touch-Unterstützung vollständig zu deaktivieren. Dies
  ist nur für benutzerdefinierte Konfigurationsprofile verfügbar.
* Wenn Sie NVDA 2018.1 verwenden, wird der Dialog für Touch-Interaktion
  zweimal unter dem Einstellungsmenü von NVDA angezeigt. Das zweite Element
  ist der Dialog, der für die Erweiterung gilt. Der erste Dialog ist die im
  NVDA integrierte Touch-Interaktion.
* Im Erweiterungsdialog Touch Interaction nwird die Eingabeart "Tippen auf
  Berührung" nicht mehr angezeigt, wenn NVDA 2018.1 verwendet wird.

## Version 17.10

* Aufgrund der Support-Richtlinien von Microsoft wird Windows 8
  (Originalversion) nicht mehr unterstützt. Windows 8.1 ist daher
  erforderlich.
* NVDA wird die Bildschirmausrichtung nicht mehr zweimal ankündigen, wenn
  NVDA 2017.4 Entwicklungs-Snapshots ausgeführt werden.

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
  die alte Art der Eingabe zurückschalten, indem Sie die Eingabeart Tippen
  auf Berührung im Dialogfeld"Touch-Interaction" aktivieren.
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
