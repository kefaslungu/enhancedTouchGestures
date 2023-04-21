# Enhanced Touch Gestures #

* Auteurr : Joseph Lee
* Télécharger [version stable][1]
* NVDA compatibility: 2022.4 and later

Cette extension fournit des gestes supplémentaires sur l'écran tactile pour
NVDA. Elle fournit également un ensemble de gestes pour parcourir facilement
lorsque vous êtes en mode navigation.

Note: this add-on requires NVDA 2022.3 or later running on a touchscreen
computer with Windows 10 or 11.

## Commandes

### Disponible partout

* Double tape 4 doigts : basculer en mode aide à la saisie.
* Glisser vers la droite quatre doigts : basculer clavier tactile
  (habituellement activer celui-ci).
* Four finger flick left: toggle dictation (Windows+H; Windows 10 Version
  1709 or later).

### Mode objet

* Glisser vers le bas 3 doigts : lecture de la fenêtre active.
* Glisser vers la gauche 3 doigts : annonce l'objet en focus.
* Glisser vers la droite 3 doigts : annonce l'objet navigateur courant.
* Glisser vers le haut 4 doigts : annonce le titre de la fenêtre active.
* Glisser vers le bas 4 doigts : annonce le texte de la barre d'état.

## Mode web tactile

Ce mode tactile, est disponible dans le mode navigation, il vous permet de
naviguer dans le document par l'élément sélectionné. Pour basculer en mode
web, depuis le mode navigation dans le document , il faut effectuer une tape
à trois doigts. Dans ce mode, en glissant vers le haut ou vers le bas avec
un seul doigt pour parcourir entre les éléments disponibles dans les modes
de navigation, tout en glissant vers la droite ou vers la gauche avec un
seul doigt pour vous déplacer vers l'élément choisi suivant ou précédent
respectivement. Une fois que vous sortez du mode navigation dans le
document, le mode objet tactile est utilisé.

## Paramètres synthétiseur mode tactile

Vous pouvez utiliser ce mode pour modifier rapidement les paramètres du
synthétiseur telles que choisir une voix et modifier le volume. Dans ce
mode, glisser vers la gauche ou vers la droite deux doigts pour se déplacer
entre les paramètres synthétiseur et glisser vers le haut ou vers le bas
deux doigts gestes pour modifier les valeurs. Ces gestes reflètes celle des
commandes en boucle des paramètres synthétiseur sur le clavier.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 8.1 is no longer supported by
  Microsoft as of January 2023.
* It is possible to reassign touch keyboard and dictation toggle commands
  from input gestures dialog under Enhanced Touch Gestures category.
* Removed read-only state workaround for touch keyboard keys as it is
  resolved in Windows 10.

## Version 22.03

* NVDA 2021.3 or later is required.
* A warning message will be displayed when attempting to install the add-on
  on Windows 7, 8, and 8.1.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this
  add-on.

## Version 21.08

* Initial support for Windows 11.

## Version 21.01

* NVDA 2020.3 or later is required.
* On Windows 10 Version 1709 and later, doing a four finger flick left will
  toggle dictation (Windows+H).
* Remove dedicated touch interaction support toggle command from the add-on.
* As touch interaction support can be toggled from NVDA's touch interaction
  settings panel, a dedicated Enhanced Touch Gestures settings panel has
  been removed.

## Version 20.09

* Removed ability to let NVDA turn off touch interaction for up to ten
  seconds (touch command passthrough).
* Removed coordinate announcement beep feature.

## Version 20.07

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

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Right mouse click gesture (one finger tap and hold) is now part of NVDA
  2020.1.

## Version 20.01

* NVDA 2019.3 or later is required.
* Touch support toggle command (including touch passthrough) will no longer
  function if touch support is turned off completely.

## Version 19.11

* Added input help messages for additional touch commands.

## Version 19.09

* Touch support can now be disabled from everywhere, not just from profiles
  other than normal profile.

## Version 19.07

* Internal changes to support future NVDA releases.

## Version 18.12

* Internal changes to support future NVDA releases.

## Version 18.08

* Compatible avec NVDA 2018.3 et les versions futures.

## Version 18.06

* Les paramètres de l'extension sont désormais disponibles dans le nouvel
  écran Paramètres NVDA multi-catégories sous la catégorie "Enhanced Touch
  Gestures". Par conséquent, NVDA 2018.2 est requis.
* Correction de problèmes de compatibilité avec wxPython 4.

## Version 18.04

* Résout un problème où la catégorie interaction tactile dans le panneau
  Paramètres de NVDA peut provoquer l'apparition de sons d'erreur en raison
  des modifications apportées à partir de cette extension.

## Version 18.03

* NVDA 2018.1 est requis.
* Parce que NVDA 2018.1 est livré avec la case à cocher frappe tactile, la
  case à cocher n'est plus incluse dans cette extension.

## Version 17.12

* Nécessite NVDA 2017.4. Plus précisément, cette extension peut désormais
  gérer les commutateurs de profil de configuration.
* Comme NVDA 2017.4 inclut l'annonce d'orientation de l'écran, cette
  fonctionnalité ne fait plus partie de cette extension.
* Ajout d'une case à cocher masquée dans le dialogue Interaction Tactile
  pour désactiver complètement le support tactile (disponible si des profils
  autres que la configuration normale sont actifs).
* If using NVDA 2018.1 or later, Touch Interaction dialog will be listed
  twice under NVDA's preferences menu. The second item is the dialog that
  comes with the add-on.
* Dans le dialogue Interaction Tactile de l'extension, le mode frappe
  tactile n'est plus affiché si vous utilisez NVDA 2018.1 ou une version
  ultérieure.

## Version 17.10

* En raison de la politique de support de Microsoft, Windows 8 (version
  originale) n'est plus supporté.
* NVDA n'annonce plus deux fois l'orientation de l'écran lors de l'exécution
  des versions snapshots de développement de NVDA 2017.4.

## Version 17.07.1

* Ajout d'une option dans le dialogue Interaction Tactile pour basculer
  manuellement une émulation tactile sans utilisation d'une minuterie.
* Avec le mode émulation manuelle désactivée, si l'émulation tactile  est
  activée avant l'expiration de la durée de l'émulation, l'interaction
  tactile serait activée.

## Version 17.07

* Ajout d'un nouveau dialogue intitulée Interaction Tactile dans le menu des
  préférences de NVDA pour configurer comment NVDA fonctionne avec les
  écrans tactiles.
* Après avoir installé cette version, lorsque vous appuyez sur les touches
  du clavier tactile, vous devez faire une double tape sur la touche
  désirée. Vous pouvez revenir à l'ancienne façon en activant la frappe
  tactile à partir du dialogue Interaction Tactile.
* Ajout d'une commande (non assignée) pour permettre à NVDA d'ignorer les
  gestes tactiles pendant 10 secondes maximum.
* Ajout d'une option dans le dialogue Interaction Tactile pour permettre à
  NVDA de suspendre l'interaction tactile entre 3 à 10 secondes afin
  d'effectuer des gestes d'écran tactile directement (comme si NVDA ne
  fonctionnait pas, la valeur par défaut est de 5 secondes).
* Ajout de messages de débogage lors d'un clic droit (taper et maintenir)
  pour être enregistré dans le journal NVDA (nécessite NVDA 2017.1 ou
  version ultérieure).
* En raison des modifications apportées lors de la sonorisation des
  coordonnées de l'écran, NVDA 2017.1 ou version ultérieure est requise.

##Version 17.03

* Correction d'un problème au cours duquel l'annonce de la coordonnée par
  des bips n'a pas été sonorisé ou une tonalité d'erreur a été sonorisé lors
  de l'utilisation de NVDA 2017.1 ou version ultérieure.

##Version 16.12

* Le mode web tactile fonctionne dans Microsoft Edge, Microsoft Word et
  d'autres où le mode navigation est utilisé.
* Ajout des listes et régions aux éléments du mode web tactile.

## Version 16.06

* Première version stable.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=enhancedTouchGestures
