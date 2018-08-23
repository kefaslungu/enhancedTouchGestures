# Enhanced Touch Gestures #

* Autor: Joseph Lee
* Descargar [versión estable][1]

Este complemento proporciona xestos táctiles adicionais para NVDA. Tamén
proporciona un conxunto de xestos para unha mellor navegación do modo
exploración.

Nota: este complemento require do NVDA 2018.2 ou posterior executándose nun
computador con pantalla táctil co Windows 8.1 ou 10.

## Ordes

### Dispoñible dende calquera lugar

* Doble toque con 4 dedos: conmuta o modo de axuda de entrada.
* Tocar e manter: leva a cabo clic dereito no obxecto baixo o teu dedo.
* Deslizamento de catro dedos cara a dereita: conmuta o teclado tactil
  (normalmente actívao).

### Modo Obxecto

* Deslizar 3 dedos cara abaixo: ler ventá actual.
* Deslizar 3 dedos á esquerda: anunciar obxecto co foco.
* Deslizar 3 dedos á dereita: anunciar actual navegador de obxectos.
* deslizar 4 dedos cara arriba: anunciar o título da ventá actual.
* Deslizar 4 dedos cara abaixo: anunciar texto da barra de estado.

## Modo Web táctil 

Este modo táctil, dispoñible no modo exploración, permíteche navegar o
documento por elementos seleccionados. Para cambiar a modo web, dende
documentos de modo exploración, realiza un toque con 3 dedos. Dende este
modo, desliza arriba ou abaixo cun dedo cíclicamente a través dos modos de
navegación dispoñibles, mentras que deslizando á dereita ou á esquerda cun
dedo móveste ó elemento seguinte ou ó anterior, respectivamente. Unha vez
saias dos documentos en modo exploración, utilízase o modo táctil obxeto.

## Modo táctil de opcións do sintetizador

Podes utilizar este modo to cambiar cíclicamente as opcións do sintetizador
como a elección dunha voz e o cambio do volume. Neste modo, utiliza o
desprazamento con dous dedos á esquerda e aá dereita para te mover entre
opcións do sintetizador e utiliza os xestos de desprazar dous dedos cara
arriba e cara abaixo para cambiar os valores. Estos xestos refrexan as ordes
do grupo de opcións do sintetizador no teclado.

## Anunciado de pitidos para coordenadas

Se habilitaches a opción Reproducir coordenadas do rato Nas Opcións do Rato,
escoitarás pitidos para indicar as coordenadas actuais da pantalla ó invocar
os xestos de exploración tactil.

## Deixar pasar orde tactil

Está dispoñible unha orde non asignada para permitirche usar xestos da
pantalla tactil coma se NVDA non estibera  en execución. Para poder usar
esto, necesitas asignar unha orde (a través do diálogo Xestos de Entrada) na
categoría Enhanced Touch Gestures para permitirche facer esto en ata 10
segundos ou cambialo manualmente. Entón vai ao menú
NVDA/Preferencias/Interacción Tactil, logo configura pausar a orde de valor
tzctil de NVDA entre 3 e 10 segundos (o predeterminado é 5 segundos).

## Deshabilitar soporte tactil en perfís

Se outros perfís distintos á configuración normal están activos e se vas ao
diálogo Interación Tactil, verás unha caixa de verificación chamada
"deshabilitar compretamente soporte tactil". Marcando esta caixa e
respondento si ao se cho pedir desactivará por compreto o soporte tactil
para ese perfil. Esto é útil en aplicacións que proporcionen as súas
proprias ordes tactiles. Para restaurar a funcionalidade tactil, desmarca
esta caixa de verificación ou activa manualmente deixar pasar toque.

## Versión 18.08

* Compatible con NVDA 2018.3 e versións futuras.

## Versión 18.06

* A configuración do complemento agora atópase na nova pantalla
  multicategoría Opcións do NVDA na categoría "Enhanced Touch Gestures". A
  consecuencia do que requírese do NVDA 2018.2.
* Arranxados os problemas de compatibilidade con wxPython 4.

## Versión 18.04

* Resolto un erro que podería causar a reprodución de sons de erro na
  categoría de Interacción Táctil no panel de Preferencias do NVDA debido a
  cambios feitos por este complemento.

## Versión 18.03

* Requírese NVDA 2018.1.
* Xa que NVDA 2018.1 vén cunha caixa de verificación Escritura Táctil, ésta
  xa non se inclúe no complemento.

## Versión 17.12

* Requírese do NVDA 2017.4. Específicamente, este complemento agora pode
  manexar cambios de perfil de configuración.
* Dado que o NVDA 2017.4 inclúe o anunciado da horientación da pantalla,
  esta característica xa non forma parte deste complemento.
* Engadida unha caixa de verificación oculta no diálogo Interación Tactil
  para desactivar compretamente o soporte tactil (dispoñible se os perfís
  distintos á configuración normal están activos).
* Se se usa NVDA 2018.1 en adiante, o diálogo Interación Tactil listarase
  dúas veces no menú Preferencias do NVDA. o segundo elemento é o diálogo
  que ven co complemento.
* No diálogo Interación Tactil para o complemento, o modo de escritura
  tactil xa non se amosa se se usa NVDA 2018.1 en adiante.

## Versión 17.10

* Debido a políticas de soporte de Microsoft, Windows 8 (versión orixinal)
  xa non se soporta.
* O NVDA xa non anunciará a orientación da pantalla dúas veces ao executar
  snapshots de desenvolvemento do NVDA 2017.4.

## Versión 17.07.1

* Engadida una opción no diálogo Interación Táctil para activar manualmente
  deixar pasar toque sen usar un temporizador.
* Co modo deixar pasar manual desactivado, se deixar pasar toque se activa
  antes de que expire a duración de deixar pasar, voltaríase a activar a
  interación táctil.

## Versión 17.07

* Engadido un novo diálogo chamado Interacción Tactil no menú Preferencias
  do NVDA para configurar cómo traballa o NVDA coas pantallas tactiles.
* Despois de instalar esta versión, ao se premer teclas no teclado tactil,
  Débese facer un doble toque na tecla desexada. Podes voltar ao vello xeito
  habilitando a escritura tactil dende o diálogo Interacción Tactil.
* Engadida unha orde (non asignada) para permitir ao NVDA ignorar xestos
  tactiles por ata 10 segundos.
* Engadida unha opción no diálogo Interacción Tactil para permitir ao NVDA
  pausar a interacción tactil entre 3 e 10 segundos para realizar xestos da
  pantalla táctil directamente (coma se o NVDA non se está a executar; por
  defecto é 5 segundos).
* Engadidas mensaxes de depuración no rexistro ao se realizar clic dereito
  (tocar e manter) para grabalos no rexistro do NVDA (require do NVDA 2017.1
  ou posterior).
* Debido a cambios feitos ao se reproducir as coordinadas da pantalla,
  requírese do NVDA 2017.1 ou posterior.

##Versión 17.03

* Correxido un fallo cando o pitido de anunciado de coordinadas non se
  reproducía ou reproducíase un ton de erro no seu lugar cando se utiliza
  NVDA 2017.1 ou anterior.

##Versión 16.12

* O modo web táctil funciona no Microsoft Edge, no Microsoft Word e outros
  onde se use o modo exploración.
* Engadidas listas e pontos de referencia aos elementos do modo web tactil.

## Versión 16.06

* Versión estable inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets
