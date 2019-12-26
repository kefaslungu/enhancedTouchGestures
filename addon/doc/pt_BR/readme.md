# Gestos táteis aprimorados #

* Autor: Joseph Lee
* Baixe a [versão estável][1]
* NVDA compatibility: 2019.3 and beyond
* Download [older version][3] compatible with NVDA 2019.2.1 and earlier

Este complemento provê gestos adicionais para telas táteis no NVDA. Também
provê um conjunto de gestos para uma navegabilidade mais fácil no modo de
navegação.

Note: this add-on requires NVDA 2019.3 or later running on a touchscreen
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
para o elemento escolhido seguinte ou anterior, respectivamente. Uma vez que
você saia de um documento de navegação, o modo tátil para objetos é usado.

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
* Se estiver usando o NVDA 2018.1 ou posterior, a caixa de diálogo Interação
  por Toque será listada duas vezes no menu de preferências do NvDA. O
  segundo item é o diálogo que vem com o complemento.
* Na caixa de diálogo Interação por toque do complemento, o modo de
  digitação não é mais exibido se você usar o NVDA 2018.1 ou posterior.

## Versão 17.10

* Devido à política de suporte da Microsoft, o Windows 8 (versão original)
  não é mais suportado.
* O NVDA deixará de anunciar a orientação da tela duas vezes quando executar
  os snapshots de desenvolvimento do NVDA 2017.4.

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

[2]: https://addons.nvda-project.org/files/get.php?file=ets-dev

[3]: https://addons.nvda-project.org/files/get.php?file=ets-2019
