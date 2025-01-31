# Gestos Táteis Aprimorados #

* Autor: Joseph Lee

Este complemento fornece gestos adicionais para telas sensível ao toque no
NVDA. Também provê um conjunto de gestos para uma navegabilidade mais fácil
no modo de navegação.

Note: this add-on requires NVDA 2024.1 or later running on a touchscreen
computer with Windows 10 or 11.

## Comandos

### Disponíveis em qualquer lugar

* Toque duplo com 4 dedos: Alterna o modo de ajuda de entrada.
* Deslizar 4 dedos à direita: alterna o teclado tátil (geralmente o
  habilita).
* Deslizar quatro dedos à esquerda: alternar ditado (Windows+H; Windows 10
  Versão 1709 ou posterior).

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
para o elemento escolhido seguinte ou anterior, respectivamente. Uma vez que
você saia de um documento de navegação, o modo tátil para objetos é usado.

## Modo tátil para opções de sintetizador

Você pode usar este modo para alterar rapidamente opções do sintetizador,
tais como escolher uma voz e alterar o volume. Neste modo, deslize com 2
dedos à esquerda ou à direita para mover entre as opções do sintetizador e
deslize com dois dedos acima e abaixo para mudar valores. Esses gestos
espelham os comandos do anel de opções do sintetizador pelo teclado.

## Version 25.02

* Restored limited support for Windows 8.1.

## Version 25.01

* Download links for add-on releases are no longer included in add-on
  documentation. You can download the add-on from NV Access add-on store.
* Switched linting tool from Flake8 to Ruff and reformatted add-on modules
  to better align with NVDA coding standards.
* Removed support for automatic add-on updates feature from Add-on Updater
  add-on.

## Version 24.05

* NVDA 2024.1 or later is required.

## Version 23.06.1

* audio ducking moved to 4 finger tap due to conflict with speech stops NVDA
  command.

## Version 23.06

* Enhanced Touch gestures nvda-addon is now maintained by Kefas Lungu.
* All gestures in object mode are now available everywhere.
* New gestures are now available.

  * 3 finger double tap: Cycles through speech symbol levels which determine
    what symbols are spoken
  * 2 finger tripple tap: Quit NVDA!.
  * 4 finger tap: Cycles through audio ducking modes.
  * Triple tap: Toggles between beeps, speech, beeps and speech, and off.

* In web mode, it is now possible to Use buttons, graphics, and landmarks in
  addition to the already available browse element list.
* In web mode, NVDA is no longer going to say normal, but default when you
  switch to default navigation from other browse element list. For example,
  when switching from buttons, NVDA will now say default.

## Versão 23.02

* É necessário o NVDA 2022.4 ou posterior.
* É necessário o Windows 10 21H2 (atualização/compilação 19044 de novembro
  de 2021) ou posterior.

## Versão 23.01

* É necessário o NVDA 2022.3 ou posterior.
* É necessário ter o Windows 10 ou posterior, pois o Windows 8.1 não será
  mais suportado pela Microsoft a partir de janeiro de 2023.
* É possível reatribuir comandos de alternância de teclado de toque e ditado
  na caixa de diálogo de gestos de entrada, na categoria Gestos de toque
  aprimorados.
* Removida a solução alternativa de estado somente leitura para as teclas do
  teclado sensível ao toque, pois ela foi resolvida no Windows 10.

## Versão 22.03

* É necessário o NVDA 2021.3 ou posterior.
* Uma mensagem de aviso será exibida ao tentar instalar o complemento no
  Windows 7, 8 e 8.1.

## Versão 21.10

* O NVDA 2021.2 ou posterior é necessário devido a mudanças no NVDA que
  afetam este complemento.

## Versão 21.08

* Suporte inicial para Windows 11.

## Versão 21.01

* O NVDA 2020.3 ou posterior é requerido.
* No Windows 10 Versão 1709 e posteriormente, fazer um movimento de quatro
  dedos à esquerda alternará ditado (Windows+H).
* Removido o comando dedicado de alternância do suporte à interação por
  toque do complemento.
* Como o suporte à interação por toque pode ser alternado no painel de
  configurações de interação por toque do NVDA, um painel de configurações
  de Gestos Táteis Aprimorados foi removido.

## Versão 20.09

* Removida a capacidade de permitir que o NVDA desligue a interação por
  toque por até dez segundos (passagem de comando tátil).
* Removido o recurso bipe de anúncio de coordenadas.

## Versão 20.07

* Adicionado um comando de teclado para alternar a interação por toque ou
  habilitar/desabilitar a passagem tátil (Control+Alt+NVDA+T).
* Como o NVDA 2020.1 e posteriores inclui um comando tátil para executar o
  clique com o botão direito do mouse (tocar com um dedo e segurar), o
  comando foi removido deste complemento. Como resultado, é necessário o
  NVDA 2020.1 ou posterior.
* A capacidade de permitir que o NVDA desligue a interação por toque por até
  dez segundos (passagem de comando tátil) foi descontinuada. Ao invés no
  futuro, esse recurso alternará a interação por toque.
* Nos desenvolvimentos  instantâneos do NVDA, devido a alterações no recurso
  de interação por toque, o recurso de passagem de comando tátil e o painel
  de configurações dos Gestos táteis aprimorados serão desativados. O
  comando usado para ativar a passagem de comando tátil alternará a
  interação por toque.
* O recurso de bipe de anúncio de coordenadas foi descontinuado e será
  removido em uma versão futura do complemento.
* O bipe de anúncio de coordenadas não será ouvido ao usar o teclado
  virtual.
* O NVDA não parece mais fazer nada ou reproduzir tons de erro enquanto
  explora os recursos de entrada modernos, como o painel emoji via toque.
* O NVDA apresentará uma mensagem de erro se o teclado virtual não puder ser
  ativado (varrer com quatro dedos à direita).

## Versão 20.06

* Foram resolvidos muitos problemas de estilo de codificação e possíveis
  erros com o Flake8.

## Versão 20.04

* O gesto de clicar com o botão direito do mouse (tocar com um dedo e
  segurar) agora faz parte do NVDA 2020.1.

## Versão 20.01

* O NVDA 2019.3 ou posterior é requerido.
* O comando de alternância de suporte a toque (incluindo passagem tátil) não
  funcionará mais se o suporte a toque estiver completamente desligado.

## Versão 19.11

* Adicionadas mensagens de ajuda de entrada para comandos de toque
  adicionais.

## Versão 19.09

* O suporte à toque agora pode ser desativado de qualquer lugar, não apenas
  de perfis diferentes do perfil normal.

## Versão 19.07

* Alterações internas para suportar versões futuras do NVDA.

## Versão 18.12

* Alterações internas para suportar versões futuras do NVDA.

## Versão 18.08

* Compatível com o NVDA 2018.3 e versões futuras.

## Versão 18.06

* As configurações do complemento agora são encontradas na nova tela
  multicategoria Configurações do NVDA, na categoria "Gestos Táteis
  Aprimorados". Como resultado, o NVDA 2018.2 é necessário.
* Corrigidos problemas de compatibilidade com o wxPython 4.

## Versão 18.04

* Resolve um problema em que a categoria de interação por toque no painel
  Configurações do NVDA pode causar sons de erro a serem ouvidos devido a
  alterações feitas neste complemento.

## Versão 18.03

* O NVDA 2018.1 é requerido.
* Como o NVDA 2018.1 vem com a caixa de seleção digitação tátil, a caixa de
  seleção não está mais incluída neste complemento.

## Versão 17.12

* Requer o NVDA 2017.4. Especificamente, este complemento agora pode
  manipular interruptores de perfil de configuração.
* Como o NVDA 2017.4 inclui anúncio de orientação de tela, este recurso não
  faz mais parte deste complemento.
* Adicionada uma caixa de seleção oculta na caixa de diálogo Interação por
  toque para desativar completamente o suporte ao toque (disponível se
  outros perfis além da configuração normal estiverem ativos).
* Se estiver usando o NVDA 2018.1 ou posterior, o diálogo Interação por
  Toque será listado duas vezes no menu de preferências do NVDA. O segundo
  item é a caixa de diálogo que vem com o complemento.
* Na caixa de diálogo Interação por toque do complemento, o modo de
  digitação não é mais exibido se você usar o NVDA 2018.1 ou posterior.

## Versão 17.10

* Devido à política de suporte da Microsoft, o Windows 8 (versão original)
  não é mais suportado.
* O NVDA deixará de anunciar a orientação da tela duas vezes quando executar
  os desenvolvimentos  instantâneos do NVDA 2017.4.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=enhancedTouchGestures
