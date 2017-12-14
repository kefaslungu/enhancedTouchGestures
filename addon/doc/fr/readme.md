# Enhanced Touch Gestures #

* Auteurr : Joseph Lee
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

Ce module complémentaire fournit des gestes supplémentaires sur l'écran
tactile pour NVDA. Il fournit également un ensemble de gestes pour parcourir
facilement lorsque vous êtes en mode navigation.

Note: this add-on requires NVDA 2017.4 or later running on a touchscreen
computer with Windows 8.1 or 10.

## Commandes

### Disponible partout

* Double tape 4 doigts : basculer en mode aide à la saisie.
* Taper et maintenir : effectue un clic droit sur l'objet sous votre doigt.
* Glisser vers la droite quatre doigts : basculer clavier tactile
  (habituellement activer celui-ci).

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

## Annonce la coordonnée par des bips

Si vous avez activé l'option Sonoriser les coordonnées quand la souris se
déplace dans les paramètres de la souris, vous entendrez des bips pour
indiquer la coordonnée actuelle de la souris sur l'écran lorsque vous
invoquez des gestes d'exploration tactile.

## Clavier tactile

Avec le module complémentaire installé, lorsque vous tapez sur le clavier
tactile, vous devez effectuer une double tape afin d'appuyer sur les touches
(appelées frape standard). Vous pouvez modifier en activant la frappe
tactile (vous lâcher la touche et la touche sera appuyée) en allant au menu
NVDA/Préférences/Interaction Tactile et cochez la case à cocher frappe
tactile.

## Émulation de commande tactile

Une commande non assignée est disponible pour vous permettre d'utiliser les
gestes de l'écran tactile comme si NVDA ne fonctionnait pas. Pour
l'utiliser, vous devez assigner une commande (via le dialogue Gestes de
commandes) dans la catégorie Enhanced Touch Gestures afin de vous permettre
de l'étendre jusqu'à dix secondes ou de le basculer manuellement. Ensuite,
allez dans le menu NVDA/Préférences/Interaction Tactile, puis le configurer
afin de suspendre la valeur   de la commande tactile de NVDA entre 3 à 10
secondes (par défaut 5 secondes).

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
* Ajout de listes et de régions aux éléments du mode web tactile.

## Version 16.06

* Première version stable.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets

[2]: https://addons.nvda-project.org/files/get.php?file=ets-dev
