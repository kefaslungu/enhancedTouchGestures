# Enhanced Touch Gestures #

* Auteurr : Joseph Lee
* Télécharger [version stable][1]
* Compatibilité NVDA: 2018.2 à 2019.1

Ce module complémentaire fournit des gestes supplémentaires sur l'écran
tactile pour NVDA. Il fournit également un ensemble de gestes pour parcourir
facilement lorsque vous êtes en mode navigation.

Notez que ce module complémentaire requiert NVDA 2018.2 ou une version
ultérieure s'exécutant sur un ordinateur tactile avec Windows 8 ou 10.

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

## Émulation de commande tactile

Une commande non assignée est disponible pour vous permettre d'utiliser les
gestes de l'écran tactile comme si NVDA ne fonctionnait pas. Pour
l'utiliser, vous devez assigner une commande (via le dialogue Gestes de
commandes) dans la catégorie Enhanced Touch Gestures afin de vous permettre
de l'étendre jusqu'à dix secondes ou de le basculer manuellement. Ensuite,
allez dans le menu NVDA/Préférences/Interaction Tactile, puis le configurer
afin de suspendre la valeur   de la commande tactile de NVDA entre 3 à 10
secondes (par défaut 5 secondes).

## Désactiver le support tactile dans les profils

Si des profils autres que la configuration normale sont actifs et que vous
accédez au dialogue Interaction Tactile, une case à cocher nommée
"Désactiver complètement le support tactile" s'affiche. Si vous cochez cette
case et que vous répondez oui si vous y êtes invité, le support  tactile de
ce profil sera complètement désactivé. Ceci est utile dans les applications
qui fournissent leurs propres commandes tactiles. Pour restaurer la
fonctionnalité tactile, décochez cette case à cocher ou basculer
manuellement l'émulation tactile.

## Version 18.08

* Compatible avec NVDA 2018.3 et les versions futures.

## Version 18.06

* Les paramètres du module complémentaire sont désormais disponibles dans le
  nouvel écran Paramètres NVDA multi-catégories sous la catégorie "Enhanced
  Touch Gestures". Par conséquent, NVDA 2018.2 est requis.
* Correction de problèmes de compatibilité avec wxPython 4.

## Version 18.04

* Résout un problème où la catégorie interaction tactile dans le panneau
  Paramètres de NVDA peut provoquer l'apparition de sons d'erreur en raison
  des modifications apportées à partir de ce module complémentaire.

## Version 18.03

* NVDA 2018.1 est requis.
* Parce que NVDA 2018.1 est livré avec la case à cocher frappe tactile, la
  case à cocher n'est plus inclus dans ce module complémentaire.

## Version 17.12

* Nécessite NVDA 2017.4. Plus précisément, ce module complémentaire peut
  désormais gérer les commutateurs de profil de configuration.
* Comme NVDA 2017.4 inclut l'annonce d'orientation de l'écran, cette
  fonctionnalité ne fait plus partie de ce module complémentaire.
* Ajout d'une case à cocher masquée dans le dialogue Interaction Tactile
  pour désactiver complètement le support tactile (disponible si des profils
  autres que la configuration normale sont actifs).
* Si vous utilisez NVDA 2018.1 ou une version ultérieure le dialogue
  Interaction Tactile apparaîtra deux fois sous le menu des préférences de
  NVDA. Le deuxième élément est le dialogue fournie avec le module
  complémentaire.
* Dans le dialogue Interaction Tactile du module complémentaire, le mode
  frappe tactile n'est plus affiché si vous utilisez NVDA 2018.1 ou une
  version ultérieure.

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
* Ajout de listes et de régions aux éléments du mode web tactile.

## Version 16.06

* Première version stable.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets
