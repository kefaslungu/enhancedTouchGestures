# Enhanced Touch Gestures #

* Autor: Joseph Lee
* Descargar [versión estable][1]
* Compatibilidad con NVDA: de 2018.2 a 2019.1

Este complemento proporciona gestos táctiles adicionales para NVDA. También
proporciona un conjunto de gestos para una mejor navegación del modo
exploración.

Nota: este complemento requiere de NVDA 2018.2 o posterior ejecutándose en
un ordenador con pantalla táctil con Windows 8.1 o 10.

## Órdenes

### Disponible desde cualquier lugar

* Doble toque con 4 dedos: conmuta el modo de ayuda de entrada.
* Tocar y mantener: lleva a cabo clic derecho en el objeto bajo tu dedo.
* Deslizamiento a la derecha con cuatro dedos: conmuta el teclado táctil
  (normalmente lo activa).

### Modo Objeto

* Deslizar 3 dedos hacia abajo: leer ventana actual.
* Deslizar 3 dedos a la izquierda: anunciar objeto con el foco.
* Deslizar 3 dedos a la derecha: anunciar actual navegador de objetos.
* deslizar 4 dedos hacia arriba: anunciar el título de la ventana actual.
* Deslizar 4 dedos hacia abajo: anunciar texto de la barra de estado.

## Modo Web táctil

Este modo táctil, disponible en modo exploración, te permite navegar el
documento por elementos seleccionados. Para cambiar a modo web, desde
documentos de modo exploración, realiza un toque con 3 dedos. Desde este
modo, desliza arriba o abajo con un dedo cíclicamente a través de los modos
de navegación disponibles, mientras que deslizando a la derecha o a la
izquierda con un dedo te mueves al elemento siguiente o al anterior,
respectivamente. Una vez te salgas de los documentos en modo exploración, se
utiliza el modo táctil objeto.

## Modo táctil de opciones del sintetizador

Puedes utilizar este modo para cambiar cíclicamente las opciones del
sintetizador tales como la elección de una voz y el cambio del volumen. En
este modo, utiliza el deslizamiento de dos dedos hacia la izquierda o la
derecha para moverte entre opciones del sintetizador y utiliza gestos de
deslizamiento de dos dedos arriba y abajo para cambiar los valores. Estos
gestos se reflejan en las órdenes del grupo de opciones del sintetizador del
teclado.

## Anunciar pitidos de coordenadas

Si has habilitado la opción Reproducir Coordenadas del Ratón en Opciones de
Ratón, escucharás pitidos para indicar las coordenadas actuales de la
pantalla al invocar los gestos de exploración de la pantalla táctil .

## Dejar pasar orden táctil

Está disponible una orden no asignada para permitirte utilizar gestos de la
pantalla táctil como si NVDA no estuviese en ejecución. Para poder utilizar
esto, necesitas asignar una orden (a través del diálogo Gestos de Entrada)
en la categoría Enhanced Touch Gestures para permitirte hacer esto en hasta
10 segundos o conmutarla manualmente. Entonces vé al menú
NVDA/Preferencias/Interacción Táctil, luego configura pausar la orden de
valor táctil de NVDA entre 3 y 10 segundos (el predeterminado es 5
segundos).

## Deshabilitar soporte táctil en perfiles

Si otros perfiles distintos a la configuración normal están activos y si vas
al diálogo Interacción Táctil, verás una casilla de verificación llamada
"deshabilitar completamente soporte táctil". Marcando esta casilla y
respondiento sí al pedírtelo desactivará por completo el soporte táctil para
ese perfil. Esto es útil en aplicaciones que proporcionen sus propias
órdenes táctiles. Para restaurar la funcionalidad táctil, desmarca esta
casilla de verificación o activa manualmente dejar pasar toque.

## Versión 18.08

* Compatible con NVDA 2018.3 y versiones futuras.

## Versión 18.06

* La configuración del complemento ahora se encuentra en la nueva pantalla
  multicategoría Opciones de NVDA en la categoría "Enhanced Touch
  Gestures". A consecuencia de ello, se requiere de NVDA 2018.2.
* Corregidos los problemas de compatibilidad con wxPython 4.

## Versión 18.04

* Resuelto un error que podía causar la reproducción de sonidos de error en
  la categoría de Interacción táctil en el panel de preferencias de NVDA
  debido a cambios hechos por este complemento.

## Versión 18.03

* Se requiere NVDA 2018.1.
* Debido a que NVDA 2018.1 viene con una casilla de verificación Escritura
  Táctil, ésta no se incluye ya en este complemento.

## Versión 17.12

* Se requiere de NVDA 2017.4. Específicamente, este complemento ahora puede
  manejar cambios de perfil de configuración.
* Dado que NVDA 2017.4 incluye el anunciado de horientación de la pantalla,
  esta característica ya no forma parte de este complemento.
* Añadida una casilla de verificación oculta en el diálogo Interacción
  Táctil para desactivar completamente el soporte táctil (disponible si los
  perfiles distintos a la configuración normal están activos).
* Si se utiliza NVDA 2018.1 en adelante, el diálogo Interacción Táctil se
  listará dos veces en el menú Preferencias de NVDA. El segundo elemento es
  el diálogo que viene con el complemento.
* En el diálogo Interacción Táctil para el complemento, el modo de escritura
  táctil ya no se muestra si se usa NVDA 2018.1 en adelante.

## Versión 17.10

* Debido a políticas de soporte de Microsoft, Windows 8 (versión original)
  ya no se soporta.
* NVDA ya no anunciará la orientación de la pantalla dos veces al ejecutar
  snapshots de desarrollo de NVDA 2017.4.

## Versión 17.07.1

* Añadida una opción en el diálogo Interacción táctil para conmutar
  manualmente dejar pasar un toque sin utilizar un temporizador.
* Con el modo dejar pasar manual desactivado, si dejar pasar toques está
  activado antes de que expire la duración de dejar pasar, la interacción
  táctil debería habilitarse.

## Versión 17.07

* Añadido un diálogo nuevo llamado Interacción Táctil en el menú
  Preferencias de NVDA para configurar cómo trabaja NVDA con las pantallas
  táctiles.
* Después de instalar esta versión, al pulsar teclas en el teclado táctil,
  se debe hacer doble toque en la tecla deseada. Puedes volver al modo
  antiguo habilitando la escritura táctil desde el diálogo Interacción
  Táctil.
* Añadida una orden (no asignada) para permitir a NVDA ignorar gestos
  táctiles por hasta 10 segundos.
* Añadida una opción en el diálogo Interacción Táctil para permitir a NVDA
  pausar la interacción táctil entre 3 y 10 segundos para realizar gestos de
  la pantalla táctil directamente (tal como si NVDA no está en ejecución;
  por defecto es 5 segundos).
* Añadidos mensajes de depuración en el registro al realizar clic derecho
  (tocar y mantener) para grabarlos en el registro de NVDA (requiere de NVDA
  2017.1 o posterior).
* Debido a cambios hechos al reproducir las coordenadas de la pantalla, se
  requiere de NVDA 2017.1 o posterior.

##Versión 17.03

* Corregido un fallo cuando el pitido de anunciado de coordenadas no se
  reproducía o se reproducía un tono de error en su lugar cuando se utiliza
  NVDA 2017.1 o anterior.

##Versión 16.12

* El modo web táctil funciona en Microsoft Edge, Microsoft Word y otros
  donde se utilice el modo exploración.
* Añadidas listas y puntos de referencia a los elementos del modo web
  táctil.

## Versión 16.06

* Versión estable inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets
