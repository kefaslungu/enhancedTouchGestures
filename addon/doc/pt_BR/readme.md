# Gestos táteis aprimorados #

* Autor: Joseph Lee
* Baixe a [versão estável][1]

Este complemento provê gestos adicionais para telas táteis no NVDA. Também
provê um conjunto de gestos para uma navegabilidade mais fácil no modo de
navegação.

Note: this add-on requires NVDA 2018.2 or later running on a touchscreen
computer with Windows 8.1 or 10.

## Comandos

### Disponíveis em qualquer situação

* Toque duplo com 4 dedos: Alterna o modo de ajuda de entrada.
* Tocar e segurar: Executa clique direito no objeto sob o dedo.
* deslizar 4 dedos à direita: Alterna o teclado tátil (geralmente o ativa).

### Modo objeto

* Deslizar 3 dedos abaixo: Lê a janela atual.
* Deslizar 3 dedos à esquerda: Anuncia o objeto com foco.
* Deslizar 3 dedos à direita: Anuncia o objeto de navegação atual.
* Deslizar 4 dedos acima: Anuncia o tipo da janela atual.
* Deslizar 4 dedos abaixo: Anuncia o texto da barra de status.

## Modo tátil para a web

Este modo tátil, disponível no modo de navegação, possibilita percorrer o
documento pelo elemento selecionado. Para trocar para o modo web, estando
num documento de navegação, dê um toque com 3 dedos. Neste modo, deslizar
acima ou abaixo com 1 dedo alterna o modo de navegação entre os elementos
disponíveis, ao passo que deslizar à direita ou à esquerda com 1 dedo move
para o elemento escolhidod seguinte ou anterior, respectivamente. Uma vez
que você saia de um documento de navegação, o modo tátil para objetos é
usado.

## Modo tátil para opções de sintetizador

Você pode usar este modo para alterar rapidamente opções do sintetizador,
tais como escolher uma voz e alterar o volume. Neste modo, deslize com 2
dedos à esquerda ou à direita para mover entre as opções do sintetizador e
deslize com dois dedos acima e abaixo para mudar valores. Esses gestos
espelham os comandos do anel de opções do sintetizador pelo teclado.

## Bipe de anúncio de coordenadas

Caso você tenha habilitado a opção de indicar as coordenadas do mouse nas
opções de mouse, você ouvirá bipes que indicam as coordenadas de tela atuais
quando fizer uso de gestos de exploração da tela.

## Passagem de comandos táteis

Está disponível um comando não atribuído para possibilitar usar gestos
táteis como se o NVDA não estivesse rodando. Para usá-lo, você tem que
atribuir um comando (via diálogo de Gestos para Entrada), na categoria
gestos táteis aprimorados, para poder fazer isso por até dez segundos ou
alternar manualmente. Depois vá ao menu do NVDA/Preferências/Interação Tátil
e configure o valor do comando tátil Pausar NVDA entre 3 e 10 segundos (o
padrão é 5 segundos).

## Disable touch support in profiles

If profiles other than normal configuration is active and if you go to Touch
Interaction dialog, you'll see a checkbox named "completely disable touch
support". Checking this box and answering yes if prompted will completely
turn off touch support for that profile. This is useful in apps that provide
their own touch commands. To restore touch functionality, either uncheck
this checkbox or manually toggle touch passthrough.

## Version 18.06

* Add-on settings is now found in new multi-category NVDA Settings screen
  under "Enhanced Touch Gestures" category. As a result, NVDA 2018.2 is
  required.
* Fixed compatibility issues with wxPython 4.

## Version 18.04

* Resolves an issue where touch interaction category in NVDA Settings panel
  may cause error sounds to be heard due to changes made from this add-on.

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

## Versão 17.07.1

* Adicionada uma opção no diálogo de interação tátil para alternar
  manualmente a passagem tátil sem o uso de um temporizador.
* Com o modo manual de passagem desligado, se a passagem tátil fosse ligada
  antes que a duração da passagem expirasse, a interação tátil seria ligada.

## Versão 17.07

* Adicionado um novo diálogo chamado Interação Tátil no menu de preferências
  do NVDA para configurar como o NVDA trabalha com telas táteis.
* Após instalar esta versão, ao pressionar teclas no teclado tátil, deve-se
  dar toque duplo na tecla desejada. Você pode voltar ao modo antigo
  habilitando digitação por toque no diálogo de Interação Tátil.
* Adicionado um comando (não-atribuído) para possibilitar ao NVDA ignorar
  gestos táteis por até 10 segundos.
* Adicionada uma opção no diálogo de interação tátil para possibilitar ao
  NVDA pausar a interação tátil entre 3 e 10 segundos de modo a executar
  gestos táteis diretamente, como se o NVDA não estivesse rodando; o padrão
  é 5 segundos.
* Adicionado registro de mensagens de debug ao executar cliques direitos
  (tocar e segurar), a serem gravadas no log do NVDA (requer NVDA 2017.1 ou
  posterior).
* Devido a alterações feitas na parte de tocar coordenadas de tela, exige-se
  o NVDA 2017.1 ou posterior.

##Versão 17.03

* Corrigido um problema em que o bipe de anúncio de coordenadas não tocava
  ou um som de erro tocava no lugar, ao usar NVDA 2017.1 ou posterior.

##Versão 16.12

* O modo tátil para a web funciona em Microsoft Edge, Microsoft Word e
  outros onde o modo de navegação é usado.
* Acrescentadas listas e marcas de seção aos elementos do modo tátil para
  web.

## Versão 16.06

* Versão estável inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets
