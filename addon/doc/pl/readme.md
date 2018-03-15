# Rozszerzone gesty dotykowe/ Enhanced Touch Gestures #

* Autor: Joseph Lee
* Pobierz [wersja stabilna][1]

Ten dodatek udostępnia dodatkowe gesty dla NVDA. Dostarcza również zestawu
gestów dla łatwiejszej nawigacji w trybie czytania.

Note: this add-on requires NVDA 2018.1 or later running on a touchscreen
computer with Windows 8.1 or 10.

## Polecenia

### Dostępne wszędzie

* Podwójne stuknięcie czterema palcami: przełącza pomoc wprowadzania.
* Stuknięcie i przytrzymanie: wykonuje kliknięcie prawym przyciskiem myszy
  na obiekcie pod palcem.
* Four finger flick right: toggle touch keyboard (usually enables it).

### Tryb obiektu

* Machnięcie w dół trzema palcami: odczytanie bieżącego okna.
* Machnięcie w lewo trzema palcami: odczytaj obiekt posiadający punkt uwagi.
* Machnięcie w prawo trzema palcami: odczytaj bieżący obiekt nawigacyjny.
* Machnięcie w górę czterema palcami: odczytaj tytuł bieżącego okna.
* Machnięcie w dół czterema palcami: odczytaj tekst paska stanu.

## dotykowy tryb czytania

Ten tryb gestów, dostępny w trybie czytania, pozwala nawigować w dokumencie
po wybranych elementach. By przełączyć się w ten tryb,, z dokumentów trybu
czytania, wykonaj stuknięcie trzema palcami. W tym trybie, machnięcie w górę
lub w dół jednym palcem przełącza między dostępnymi sposobami nawigacji,
machnięcie jednym palcem w lewo lub prawo przesuwa do poprzedniego lub
następnego wybranego elementu. Po wyjściu z dokumentu trybu czytania,
używany jest obiektowy tryb gestów dotykowych.

## Tryb dotykowej zmiany ustawień syntezatora

Możesz użyć tego trybu do szybkiej zmiany ustawień syntezatora, np. by
wybrać głos, albo zmienić głośność. Użyj machnięcia dwoma palcami w lewo lub
prawo do przejścia pomiędzy ustawieniami, a gestów machnięcia dwoma palcami
w górę i dół do zmiany wartości ustawienia. Te gesty odpowiadają klawiszom
szybkiej zmiany ustawień syntezatora.

## Dźwięk oznajmiania położenia

Jeśli włączony jest dźwięk wskaźnika myszy,  będziesz słyszał dźwięki
określające aktualne położenie na ekranie, po wywołaniu gestu dotykowej
eksploracji.

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

* Fixed an issue where coordinate announcement beep did not play or an error
  tone played instead when using NVDA 2017.1 or later.

##Wersja 16.12

* Web touch mode works in Microsoft Edge, Microsoft Word and others where
  browse mode is used.
* Added lists and landmarks to web touch mode elements.

## Wersja 16.06

* Initial stable version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets
