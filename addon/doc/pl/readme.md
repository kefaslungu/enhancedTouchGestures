# Enhanced Touch Gestures #

* Autor: Joseph Lee
* Pobierz [wersja stabilna][1]
* NVDA compatibility: 2020.3 and beyond

Ten dodatek udostępnia gesty dotykowe dla NVDA oraz zestaw specjalnych
gestów do łatwiejszej nawigacji w trybie czytania.

Note: this add-on requires NVDA 2020.3 or later running on a touchscreen
computer with Windows 8.1, 10 or 11.

## Polecenia

### Dostępne wszędzie

* Podwójne stuknięcie czterema palcami: przełącza pomoc wprowadzania.
* Przesunięcie w prawo czterema palcami: Przełączanie klawiatury dotykowej
  (za zwyczaj ją włącza).
* Four finger flick left: toggle dictation (Windows+H; Windows 10 Version
  1709 or later).

### Tryb obiektu

* Przesunięcie w dół trzema palcami: odczytanie bieżącego okna.
* Przesunięcie w lewo trzema palcami: odczytaj obiekt posiadający fokus..
* Przesunięcie w prawo trzema palcami: odczytaj bieżący obiekt nawigacyjny.
* Przesunięcie w górę czterema palcami: odczytaj tytuł bieżącego okna.
* Przesunięcie w dół czterema palcami: odczytaj tekst paska stanu.

## dotykowy tryb czytania

Ten tryb gestów, dostępny w trybie czytania, pozwala nawigować po wybranych
elementach dokumentu. Aby przełączyć się w ten tryb z dokumentów trybu
czytania, wykonaj stuknięcie trzema palcami. W tym trybie, Przesunięcie w
górę lub w dół jednym palcem przełącza między dostępnymi sposobami
nawigacji, Przesunięcie jednym palcem w lewo lub prawo przenosi do
poprzedniego lub następnego wybranego elementu. Po wyjściu z dokumentu trybu
czytania, używany jest obiektowy tryb gestów dotykowych.

## Tryb dotykowej zmiany ustawień syntezatora

Możesz użyć tego trybu do szybkiej zmiany ustawień syntezatora, np. by
wybrać głos, albo zmienić głośność. Przesuń dwoma palcami w lewo lub prawo
aby przechodzić między ustawieniami. Przesuń dwoma palcami w górę lub w dół
aby zmieniać wartości danego ustawienia. Gesty te odpowiadają klawiszom
szybkiej zmiany ustawień syntezatora.

## Version 21.01

* NVDA 2020.3 or later is required.
* On Windows 10 Version 1709 and later, doing a four finger flick left will
  toggle dictation (Windows+H).
* Remove dedicated touch interaction support toggle command from the add-on.
* As touch interaction support can be toggled from NVDA's touch interaction
  settings panel, a dedicated Enhanced Touch Gestures settings panel has
  been removed.

## Wersja 20.04

* Removed ability to let NVDA turn off touch interaction for up to ten
  seconds (touch command passthrough).
* Removed coordinate announcement beep feature.

## Wersja 20.07

* Added a keyboard command to toggle touch interaction or enable/disable
  touch passthrough (Control+Alt+NVDA+T).
* As NVDA 2020.1 and later includes a touch command to perform right mouse
  click (one finger tap and hold), the command has been removed from this
  add-on. AS a result, NVDA 2020.1 or later is required.
* The ability to let NVDA turn off touch interaction for up to ten seconds
  (touch command passthrough) is deprecated. In the future this feature will
  toggle touch interaction instead.
* In NVDA development snapshots, due to touch interaction feature changes,
  touch command passthrough feature and Enhanced Touch Gestures settings
  panel will be disabled. The command used to enable touch command
  passthrough will toggle touch interaction instead.
* Coordinate announcement beep feature is deprecated and will be removed in
  a future add-on release.
* Coordinate announcement beep will not be heard while using touch keyboard.
* NVDA will no longer appear to do nothing or play error tones while
  exploring modern input facility such as emoji panel via touch.
* NVDA will present an error message if touch keyboard cannot be activated
  (four finger flick right).

## Wersja 20.06

* Naprawiono niektóre błędy stylistyczne związane z kodem,  a także
  naprawiono błędy związane z linterem Flake8.

## Wersja 20.04

* Polecenie prawego przycisku myszy (stuknięcie z przytrzymaniem jednym
  palcem) jest wbudowane w NVDA w wersji 2020.1.

## Wersja 20.01

* Wymagana jest wersja NVDA 2019.3 lub nowsza.
* Polecenie do przełączania trybu dotykowego (włączając w to dotykowe
  przełączanie) nie będzie więcej funkcjonowało, gdy wsparcie dotykowe jest
  kompletnie wyłączone.

## Wersja 19.11

* Dodano komunikaty pomocy dla dodatkowych poleceń dotykowych.

## Wersja 19.09

* Wsparcie dotykowe może być wyłączone z jakiegokolwiek miejsca, czyli nie
  tylko przy aktywnym normalnym profilu.

## Wersja 19.07

* Zmiany wewnętrzne dla wsparcia nowszych wersji NVDA.

## Wersja 18.12

* Zmiany wewnętrzne dla wsparcia nowszych wersji NVDA.

## Wersja 18.08

* Zgodne z NVDA 2018.3 i nowszymi.

## Wersja 18.06

* Od teraz ustawienia dodatku znajdują się w nowym, wielopanelowym oknie
  ustawień NVDA, w kategorii "Enhanced Touch Gestures" . Z powodu licznych
  zmian, wymagana jest wersja NVDA 2018.2.
* Naprawiono problemy zgodności z wxPython 4.

## Wersja 18.04

* Rozwiązuje problem, przez który kategoria reakcji na dotyk w panelu
  ustawień NVDA może wywoływać dźwięki błędu, z powodu zmian wprowadzonych w
  tym dodatku.

## Wersja 18.03

* Wymaga NVDA 2018.1.
* NVDA 2018.1 posiada już pole wyboru, które włącza wpisywanie dotykowe,
  dlatego zostało ono usunięte z dodatku.

## Wersja 17.12

* Wymaga NVDA 2017.4. Przede wszystkim, dodatek może już przełączać się
  między profilami.
* Ponieważ NVDA 2017.4 może ogłaszać orientację ekranu, usunięto tę funkcję
  z dodatku.
* Aby zupełnie wyłączyć wsparcie dotyku, Do dialogu reakcji na dotyk dodano
  ukryte pole wyboru, dostępne tylko wtedy gdy aktywny jest inny profil niż
  standardowy.
* If using NVDA 2018.1 or later, Touch Interaction dialog will be listed
  twice under NVDA's preferences menu. The second item is the dialog that
  comes with the add-on.
* W oknie dialogowym reakcji dotykowej dodatku, od wersji NVDA 2018.1 tryb
  wpisywania dotykowego nie jest już pokazywany.

## Wersja 17.10

* W związku z polityką wsparcia firmy Microsoft, Windows 8 nie jest już
  wspierany.
* NVDA nie będzie już dwukrotnie ogłaszać orientacji ekranu w wersjach
  rozwojowych  NVDA 2017.4.

## Wersja 17.07.1

* Do dialogu reakcji na dotyk dodano opcję służącą do ręcznego przełączania
  przepuszczania dotyku bez potrzeby użycia timera.
* Jeśli ręczny tryb przepuszczania jest wyłączony a przepuszczanie dotyku
  zostało włączone zanim wygasł jego czas, włączy się reakcja na dotyk.

## Wersja 17.07

* Do Meni Ustawień NVDA dodano okno dialogowe reakcji na dotyk. Służy ono do
  konfigurowania sposobu w jaki NVDA współpracuje z ekranami dotykowymi.
* Po instalacji tej wersji dodatku trzeba dwukrotnie stuknąć w żądany
  klawisz na klawiaturze dotykowej. Do poprzedniego sposobu można powrócić
  włączając wpisywanie dotykowe w oknie reakcji na dotyk.
* Dodano funkcję nieprzypisanego polecenia, dzięki której NVDA ignoruje
  gesty dotykowe przez czas do 10 sekund.
* Do okna dialogowego reakcji na dotyk dodano opcję, która pozwala NVDA
  wstrzymać reakcję na dotyk od 3 do 10 sekund. Dzięki temu można wykonywać
  gesty na ekranie dotykowym jakgdyby screenreader w ogóle nie był
  uruchomiony. Domyślna wartość wynosi 5 sekund.
* Dodano zapisywanie wiadomości debugowania w dzienniku NVDA podczas
  wykonywania prawego kliknięcia (stuknięcie i przytrzymanie). Wymagana
  wersja NVDA 2017.1 lub nowsza.
* W związku ze zmianami w odtwarzaniu współrzędnych ekranu, wymagana jest
  wersja NVDA 2017.1 lub nowsza.

##Version 17.03

* Poprawiono błąd, z powodu którego dźwięk oznajmiania położenia nie był
  odtwarzany lub zamiast niego pojawiał się dźwięk błędu. Działo się to w
  NVDA 2017.1 i nowszych.

##Version 16.12

* Dotykowy tryb czytania działa w Microsoft Edge, Microsoft Word i innych
  programach, gdzie używa się trybu przeglądu.
* Do elementów dotykowego trybu czytania dodano listy i punkty orientacyjne.

## Wersja 16.06

* Pierwsza wersja stabilna.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets

[2]: https://addons.nvda-project.org/files/get.php?file=ets-dev
