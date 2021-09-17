# Comandos de Toque Realçados #

* Autor: Joseph Lee
* Baixar [versão estável][1]
* NVDA compatibility: 2021.2 and beyond

Este extra fornece comandos de ecrã sensível ao toque adicionais para o
NVDA. Também fornece um conjunto de comandos para uma navegação mais fácil
no modo de navegação.

Note: this add-on requires NVDA 2021.2 or later running on a touchscreen
computer with Windows 8.1, 10 or 11.

## Comandos:

### Disponíveis em qualquer lugar:

* Toque com quatro dedos: Activa/desactiva a ajuda de entrada.
* Quatro dedos para a direita: Geralmente, activa o teclado virtual.
* Quatro dedos à esquerda: alternar ditado (Windows+H; Windows 10 Versão
  1709 ou posterior).

### Revisão de objecto:

* Três dedos para baixo: lê a janela actual.
* Três dedos para a esquerda: indica o objecto sob o foco.
* Três dedos para a direita: indicam o objecto de navegação actual.
* Quatro dedos para cima: indica o título da janela actual.
* Quatro dedos para baixo: lê a barra de estado.

## Modo toque na Web

Este modo de toque, disponível no modo de navegação, permite-lhe navegar
pelo documento através do elemento seleccionado. Para mudar para o modo web,
a partir dos documentos do modo de navegação, dê 3 toques. A partir deste
modo, o deslocamento para cima ou para baixo com um dedo passa pelos modos
de navegação dos elementos disponíveis, enquanto se desloca para a direita
ou para a esquerda com um dedo move-se para o elemento escolhido seguinte ou
anterior, respectivamente. Uma vez que deixa o modo de navegação, o modo de
toque do objeto passa a ser usado.

## configurações de sintetizador do Modo de toque

Pode usar este modo para mudar rapidamente as configurações do sintetizador,
como escolher uma voz e alterar o volume. Neste modo, use de dois dedos para
a esquerda ou para a direita para se mover entre as configurações do
sintetizador e use dois dedos para cima e para baixo gestos para alterar os
valores. estes gestos são semelhantes aos comandos de teclado das
configurações dos sintetizadores.

## Version 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this
  add-on.

## Version 21.08

* Initial support for Windows 11.

## Version 21.01

* NVDA 2020.3 or later is required.
* No Windows 10 Versão 1709 e posteriores, fazer um movimento de quatro
  dedos à esquerda irá alternar o ditado (Windows+H).
* Remover o comando de alternância de suporte dedicado de interacção táctil
  do extra.
* Como o suporte de interacção táctil pode ser alternado a partir do painel
  de configurações de interacção táctil do NVDA, um painel dedicado de
  definições de comandos Tácteis Melhorados foi removido.

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

## Versão 18.08

* Compatível com NVDA 2018.3 e futuras versões.

## Versão 18.06

* Agora, as configurações adicionais encontram-se no novo ecrã
  multi-categoria Configurações do NVDA, na categoria "comandos de toque
  aprimorados". Como resultado, é necessário o NVDA 2018.2.
* Corrigidos problemas de compatibilidade com o wxPython 4.

## Versão 18.04

* Resolve um problema em que a categoria de interacção por toque no painel
  Configurações do NVDA pode causar sons de erro, devido a alterações feitas
  a partir deste extra.

## Versão 18.03

* É necessário o NVDA 2018.1
* Como o NVDA 2018.1 já trás incluída a caixa de selecção por toque, essa
  caixa de selecção deixou de fazer parte deste extra.

## Versão 17.12

* Requer NVDA 2017.4. Especificamente, este extra agora pode processar
  trocas de perfil de configuração.
* Como o NVDA 2017.4 inclui o anúncio da orientação do ecrã, esse recurso
  não faz mais parte deste extra.
* Adicionada uma caixa de selecção oculta na caixa de diálogo Interacção por
  toque para desativar completamente o suporte por toque (disponível se
  outros perfis além do da configuração normal estiverem activos).
* If using NVDA 2018.1 or later, Touch Interaction dialog will be listed
  twice under NVDA's preferences menu. The second item is the dialog that
  comes with the add-on.
* No diálogo de interacção de toque para o extra, o modo de digitar toque
  não é mostrado se usar versões do NVDA posteriores à 2018.1.

## Versão 17.10

* Devido à política de suporte da Microsoft, o Windows 8 (versão original)
  não é mais suportado.
* O NVDA não anunciará mais a orientação do ecrã duas vezes ao executar
  versões de desenvolvimento do NVDA 2017.4.

## Versão 17.07.1

* Adicionada uma opção no diálogo de interacção de toque para alternar
  manualmente a passagem de toque sem o uso de um temporizador.
* Com o modo de passagem manual desligado, se a passagem de toque for
  activada antes do final da duração da passagem, a interacção de toque será
  activada.

## Versão 17.07

* Adicionada uma nova caixa de diálogo denominada interacção por toque no
  menu de preferências do NVDA para configurar como o NVDA funciona com
  ecrãs sensíveis ao toque.
* Depois de instalar esta versão, ao pressionar as teclas no teclado
  virtual, é preciso tocar duas vezes a tecla desejada. Pode voltar para a
  maneira antiga, permitindo a digitação de toque na caixa de diálogo
  Interação táctil.
* Adicionado um comando (não atribuído) para permitir que o NVDA ignore os
  gestos de toque até 10 segundos.
* Adicionada uma opção na caixa de diálogo Interacção por toque para
  permitir que o NVDA interrompa a interacção de toque entre 3 a 10 segundos
  para executar gestos de ecrã sensível directamente (como se o NVDA não
  estivesse em execução, o padrão é 5 segundos).
* Adicionadas mensagens de log de depuração ao executar cliques corretos
  (tocar e segurar) para serem gravadas no log do NVDA (requer NVDA 2017.1
  ou posterior).
* Devido às alterações feitas ao reproduzir as coordenadas do ecrã, o NVDA
  2017.1 ou posterior é necessário.

##Version 17.03

* Corrigido um problema em que o sinal sonoro de coordenadas não era
  reproduzido ou surgia um beep de erro em vez disso ao usar o NVDA 2017.1
  ou posterior.

##Version 16.12

* O modo Web Touch funciona no Microsoft Edge, no Microsoft Word e em outros
  onde o modo de navegação é usado.
* Adicionadas listas e marcadores para elementos do modo web touch.

## Versão 16.06

* Versão inicial estável.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets
