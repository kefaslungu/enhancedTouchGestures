# Enhanced Touch Gestures #

* Autor: Joseph Lee
* Pobierz [wersja stabilna][1]
* NVDA compatibility: 2018.2 to 2019.2

Ten dodatek udostępnia gesty dotykowe dla NVDA oraz zestaw specjalnych
gestów do łatwiejszej nawigacji w trybie czytania.

Uwaga! Ten dodatek wymaga NVDA w wersji 2018.2 lub nowszej, uruchomionej na
komputerze z ekranem dotykowym i systemem operacyjnym Windows 8.1 lub 10.

## Polecenia

### Dostępne wszędzie

* Podwójne stuknięcie czterema palcami: przełącza pomoc wprowadzania.
* Stuknięcie i przytrzymanie: wykonuje kliknięcie prawym przyciskiem myszy
  na obiekcie pod palcem.
* Przesunięcie w prawo czterema palcami: Przełączanie klawiatury dotykowej
  (za zwyczaj ją włącza).

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

## Dźwięk oznajmiania położenia

Jeśli włączony jest dźwięk wskaźnika myszy,  będziesz słyszał dźwięki
określające aktualne położenie na ekranie, po wywołaniu gestu dotykowej
eksploracji.

## Przepuszczanie polecenia dotykowego

Nieprzypisane polecenie pozwala używać gestów ekranu tak, jakby NVDA nie był
uruchomiony. Aby użyć tej funkcji, przypisz je w kategorii Enhanced Touch
Gestures przez dialog zdarzeń wejścia. Pozwoli to wstrzymać reakcję na dotyk
do dziesięciu sekund lub przełączyć ją ręcznie. Następnie należy wejść do
meni NVDA/Ustawienia/Reakcja na Dotyk, i skonfigurować czas wstrzymania
poleceń dotykowych NVDA od 3 do 10 sekund. Wartość domyślna to 5 sekund.

## Wyłączanie wsparcia dotyku w profilach

Jeżeli aktywny jest inny profil niż standardowy, po wejściu do dialogu
reakcji na dotyk zobaczysz pole wyboru o nazwie "Wyłącz wsparcie
dotyku". Zaznaczenie tego pola i potwierdzenie przyciskiem Tak całkowicie
wyłączy wsparcie dotyku dla tego profilu. Jest to użyteczne w aplikacjach,
które posiadają własne gesty dotykowe. Aby przywrócić funkcjonalność dotyku,
odznacz to pole wyboru lub ręcznie przełącz przepuszczanie dotyku.

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
* W NVDA 2018.1 i nowszych, dialog reakcji na dotyk pojawi się dwukrotnie w
  meni ustawień NvDA. Drugi dialog jest oryginalną częścią dodatku.
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

##Wersja 17.03

* Poprawiono błąd, z powodu którego dźwięk oznajmiania położenia nie był
  odtwarzany lub zamiast niego pojawiał się dźwięk błędu. Działo się to w
  NVDA 2017.1 i nowszych.

##Wersja 16.12

* Dotykowy tryb czytania działa w Microsoft Edge, Microsoft Word i innych
  programach, gdzie używa się trybu przeglądu.
* Do elementów dotykowego trybu czytania dodano listy i punkty orientacyjne.

## Wersja 16.06

* Pierwsza wersja stabilna.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets
