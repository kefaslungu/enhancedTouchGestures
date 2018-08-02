# Enhanced Touch Gestures (Udvidede berøringsbevægelser) #

* Forfatter: Joseph Lee
* Download [stabil version][1]

Dette tilføjelsesprogram tilføjer ekstra berøringskommandoer til NVDA. Det
giver et sæt bevægelser for lettere navigering i gennemsynstilstand.

Bemærk, at du skal bruge NVDA 2018.2 eller senere installeret på en computer
med berøringsfølsom skærm, og som kører Windows 8.1 eller 10.

## Kommandoer

### Tilgængelig over alt

* Dobbelt-tap med 4 fingre: Slå hjælpetilstand til/fra.
* Tap og hold: udfører et højreklik på objektet under din finger.
* Svirp til højre med 4 fingre: Slå berøringstastatur til/fra (som regel
  til).

### Objekttilstand

* Svirp ned med 3 fingre:Læs aktuelle vindue
* Svirp til venstre med 3 fingre: Annoncer objekt med fokus.
* Svirp til højre med 3 fingre: Annoncer aktuelle navigator-objekt.
* Svirp op med 4 fingre: Annoncer titel på aktuelle vindue.
* Svirp ned med 4 fingre: Annoncer tekst på statuslinjen.

## Web-berøringstilstand

Med denne berøringstilstand, som kan bruges i gennemsynstilstand, kan du
navigere i et dokument efter det valgte element. I dokumenter, der
understøtter gennemsynstilstand, kan du skifte til web-tilstand ved at tappe
med 3 fingre. I denne tilstand kan du svirpe op og ned med en finger for at
vælge den type element, du vil navigere efter. Du kan svirpe mod højre eller
venstre flytter til henholdsvis det næste eller forrige element af den
valgte type. Når du går ud af et dokument, som understøtter
gennemsynstilstand, vil objektberøringstilstand blive brugt.

## Berøringstilstand til indstilling af talesyntese

Du kan bruge denne tilstand til hurtigt at at skifte indstillinger for
talesyntese, f.eks. vælge en stemme og ændre lydstyrke. I denne tilstand kan
du svirpe til højre eller venstre med to fingre for at flytte mellem de
forskellige indstillinger for talesyntesen. Svirp op og ned for at ændre den
valgte indstilling. Disse bevægelser svarer til tastaturkommandoerne til
ringen for talesynteseindstillinger.

## Annoncering af koordinater, lydsignal

Hvis du har slået indstillingen "Afspil lydkoordinater under flytning af
mus" til under indstillinger for mus, vil du høre lydsignaler, som indikerer
de aktuelle skærmkoordinater, når du bruger udforskningsbevægelser.

## Slip berørngskommando igennem

En utildelt berøringskommando er tilgængelig, der lader dig benytte andre
berøringskommandoer som om NVDA ikke kørte. For at benytte denne funktion,
skal du tildel en kommando ved at benytte dialogen "Inputbevægelser" under
kategorien "Enhanced Touch Gestures". Dette kan vare op til ti sekunder,
eller dette kan slås fra manuelt. Gå herefter til
NVDA-menu>Præferencer>Indstillinger>Touch-interaktion, og konfigurer Pause i
NVDA's touch-understøttelse til mellem 3 og 10 sekunder. Som standard er det
5.

## Slå understøttelse for berøring fra i profiler

Hvis andre profiler end den normal konfiguration er aktiv, og hvis du går
til dialogboksen Berøringsinteraktion, vil du se check boxen "deaktivér
fuldstændigt berøringsunderstøttelse". Du vælger check boxen og svarer ja,
hvis du bliver bedt om du helt vil deaktivere berøringsunderstøttelse for
den pågældende profil. Dette er nyttigt i apps der anvender deres egne
touch-kommandoer. Hvis du vil gendanne touch funktionalitet, enten fjerne
markeringen i dette afkrydsningsfelt eller manuelt skifte touch passthrough.

## Version 18.08

* Compatible with NVDA 2018.3 and future versions.

## Version 18.06

* Tilføjelsesindstillinger er nu at finde i kategorien "Udvidede
  berøringsbevægelser" i NVDAs indstillingsdialog. Som følge heraf er NVDA
  2018.2 påkrævet.
* Rettede kompatibilitetsproblemer med wxPython 4.

## Version 18.04

* Løser et problem, hvor indstillingskategorien "Berøringsinteraktion"i
  NVDA-indstillingspanelet kan forårsage fejllyde, der høres på grund af
  ændringer foretaget af denne tilføjelse.

## Version 18.03

* NVDA 2018.1 er påkrævet.
* Fordi NVDA 2018.1 kommer med check box til at slå berøringsindtastning til
  og fra, er afkrydsningsfeltet ikke længere inkluderet i denne tilføjelse.

## Version 17.12

* Kræver NVDA 2017.4. Specifikt, kan denne tilføjelse nu håndtere skift af
  indstillingsprofiler.
* Da NVDA 2017.4 omfatter meddelelser om skærmens orientering, er denne
  funktion ikke længere en del af denne tilføjelse.
* Tilføjede en skjult check box i berøringsinteraktion, der lader dig slå
  understøttelse for berøring helt fra (tilgængelig hvis andre profiler end
  den normale indstillingsprofil er aktiv).
* Hvis du bruger NVDA 2018.1 eller nyere, vil du få vist dialoger til
  berøringsinteraktion to gange under NVDAs indstillingskategorier. Det
  andet punkt er den dialog, der tilhører tilføjelsen.
* Indstillingen til berøringsindtastning vises ikke længere i tilføjelsens
  egen dialog for berøringsindtastning, hvis du benytter NVDA 2018.2 eller
  nyere.

## Version 17.10

* På grund af støttepolitik fra Microsoft understøttes Windows 8 (original
  version) ikke længere.
* NVDA meddeler ikke længere skærmorientation to gange, når du kører NVDA
  2017.4 development snapshots.

## Version 17.07.1

* Tilføjet en mulighed i dialogboksen "Berøringsinteraktion" til at manuelt
  lade berøringsbevægelser slippe igennem, uden at bruge en timer.
* Med tilstanden til manuelt at slippe berøringsbevægelser igennem slået
  fra, og hvis berøringsbevægelser slippes igennem før varigheden udløber,
  slås berøringsinteraktion til.

## Version 17.07Version: [0.6][1]

* Tilføjet en ny dialogboks ved navn "Berøringsindtastning" under NVDAs menu
  under Præferencer til at konfigurere, hvordan NVDA fungere med
  berøringsskærme.
* Du skal trykke to gange på den ønskede tast på berøringstastaturet, når du
  har installeret denne version. Du kan skifte tilbage til den forrige
  metode ved at benytte dialogen "Beræringsindteraktion".
* Tilføjede en utildelt kommando, der lader NVDA ignorere alle
  berøringsbevægelser op til 10 sekunder.
* Tilføjet en mulighed i dialogen "Berøringsinteraktion", der tillader NVDA
  at pause berøringsinteraktion mellem 3 til 10 sekunder for at udføre
  bevægelser direkte (som om NVDA ikke kørte, standard er 5 sekunder).
* Tilføjede beskeder ang. fejlfinding når du udføre højreklik (tryk og hold
  nede), der skrives ind i din NVDA-logfil. Dette kræver NVDA 2017.1 eller
  nyere.
* På grund af ændringer, der foretages ved afspilning af skærmkoordinater,
  kræves NVDA 2017.1 eller nyere.

##Version 17.03

* Løst et problem, hvor bip når koordinater blev annoncerede ikke spillede
  eller en fejltone blev spillet i stedet, når du bruger NVDA 2017.1 eller
  nyere.

##Version 16.12

* Web-berøringstilstand fungerer i Microsoft Edge, Microsoft Word og andre
  hvor steder gennemsynstilstand benyttes.
* Tilføjede lister og landmærker til elementer af web-berøringstilstande.

## Version 16.06

* Første stabile version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets
