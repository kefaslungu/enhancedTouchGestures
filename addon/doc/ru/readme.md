# Enhanced Touch Gestures #

* Автор: Joseph Lee
* Загрузить [стабильную версию][1]
* NVDA compatibility: 2022.4 and later

Это дополнение предоставляет дополнительные жесты сенсорного экрана для
NVDA. Также, оно предоставляет набор жестов для облегчения навигации режима
обзора.

Примечание: этому дополнению требуется NVDA 2022.3 или позднее, запущенной
на сенсорном компьютере с Windows 10 или 11.

## Команды

### Доступно везде

* Двойное касание четырьмя пальцами: включить режим справки по вводу.
* Смахивание четырьмя пальцами вправо: Изменить состояние экранной
  клавиатуры (обычно, вызывает ее)
* Four finger flick left: toggle dictation (Windows+H; Windows 10 Version
  1709 or later).

### Объектный режим

* Смахивание тремя пальцами вниз: прочитать текущее окно.
* Смахивание тремя пальцами влево: Объявить объект в фокусе.
* Смахивание тремя пальцами вправо: Объявить текущий объект навигатора.
* Смахивание четырьмя пальцами вверх: Объявляет название текущего окна.
* смахивание четырьмя пальцами вниз: прочитать текст строки состояния.

## Сенсорный режим веб

Этот сенсорный режим, доступный в режиме обзора, позволяет осуществлять
навигацию  в документе по выбранным элементам. Чтобы переключиться в
Сенсорный режим веб из режима обзора документа, выполните двойное касание
тремя пальцами. В этом режиме пролистывания одним пальцем вверх или вниз
выбирают доступные действия с элементом, а пролистывания одним пальцем влево
или вправо перемещают к предыдущему и следующему элементам
соответственно. Когда вы покинете режим обзора документов, будет активирован
объектный режим.

## Сенсорный режим настроек синтезатора

Вы можете использовать этот режим для быстрого изменения настроек
синтезатора, таких как выбор голоса и изменения громкости. В этом режиме
используются пролистывания двумя пальцами влево или вправо, чтобы
перемещаться между настройками синтезатора и пролистывания двумя пальцами
вверх и вниз, чтобы изменить значения. Это зеркало жестов настроек
клавиатурных команд кольца синтезатора.

## Версия 23.02

* Требуется NVDA 2022.4 или позже.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Версия 23.01

* Требуется NVDA 2022.3 или позже.
* Windows 10 or later is required as Windows 8.1 is no longer supported by
  Microsoft as of January 2023.
* It is possible to reassign touch keyboard and dictation toggle commands
  from input gestures dialog under Enhanced Touch Gestures category.
* Removed read-only state workaround for touch keyboard keys as it is
  resolved in Windows 10.

## Версия 22.03

* Требуется NVDA 2021.3 или позже.
* A warning message will be displayed when attempting to install the add-on
  on Windows 7, 8, and 8.1.

## Версия 21.10

* NVDA 2021.2 or later is required due to changes to NVDA that affects this
  add-on.

## Версия 21.08

* Initial support for Windows 11.

## Версия 21.01

* Требуется NVDA 2020.3 или позже.
* On Windows 10 Version 1709 and later, doing a four finger flick left will
  toggle dictation (Windows+H).
* Remove dedicated touch interaction support toggle command from the add-on.
* As touch interaction support can be toggled from NVDA's touch interaction
  settings panel, a dedicated Enhanced Touch Gestures settings panel has
  been removed.

## Версия 20.09

* Removed ability to let NVDA turn off touch interaction for up to ten
  seconds (touch command passthrough).
* Удалена функция звукового оповещения о координатах.

## Версия 20.07

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

## Версия 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Версия 20.04

* Right mouse click gesture (one finger tap and hold) is now part of NVDA
  2020.1.

## Версия 20.01

* Требуется NVDA 2019.3 или позже.
* Touch support toggle command (including touch passthrough) will no longer
  function if touch support is turned off completely.

## Версия 19.11

* Added input help messages for additional touch commands.

## Версия 19.09

* Touch support can now be disabled from everywhere, not just from profiles
  other than normal profile.

## Версия 19.07

* Internal changes to support future NVDA releases.

## Версия 18.12

* Internal changes to support future NVDA releases.

## Версия 18.08

* Compatible with NVDA 2018.3 and future versions.

## Версия 18.06

* Add-on settings is now found in new multi-category NVDA Settings screen
  under "Enhanced Touch Gestures" category. As a result, NVDA 2018.2 is
  required.
* Fixed compatibility issues with wxPython 4.

## Версия 18.04

* Resolves an issue where touch interaction category in NVDA Settings panel
  may cause error sounds to be heard due to changes made from this add-on.

## Версия 18.03

* Требуется NVDA 2018.1.
* Because NVDA 2018.1 comes with touch typing checkbox, the checkbox is no
  longer included in this add-on.

## Версия 17.12

* Requires NVDA 2017.4. Specifically, this add-on can now handle
  configuration profile switches.
* As NVDA 2017.4 includes screen orientation announcement, this feature is
  no longer part of this add-on.
* Added a hidden checkbox in Touch Interaction dialog to completely disable
  touch support (available if profiles other than normal configuration is
  active).
* If using NVDA 2018.1 or later, Touch Interaction dialog will be listed
  twice under NVDA's preferences menu. The second item is the dialog that
  comes with the add-on.
* In Touch Interaction dialog for the add-on, touch typing mode is no longer
  shown if using NVDA 2018.1 or later.

## Версия 17.10

* Due to support policy from Microsoft, Windows 8 (original release) is no
  longer supported.
* NVDA will no longer announce screen orientation twice when running NVDA
  2017.4 development snapshots.

## Версия 17.07.1

* Added an option in touch interaction dialog to manually toggle touch
  passthrough without use of a timer.
* With manual passthrough mode off, if touch passthrough is turned on before
  the passthrough duration expires, touch interaction would be enabled.

## Версия 17.07

* Added a new dialog named Touch Interaction under NVDA's preferences menu
  to configure how NVDA works with touchscreens.
* After installing this version, when pressing keys on the touch keyboard,
  one must double tap the desired key. You can switch back to the old way by
  enabling touch typing from Touch Interaction dialog.
* Added a command (unassigned) to allow NVDA to ignore touch gestures for up
  to 10 seconds.
* Added an option in Touch Interaction dialog to allow NVDA to pause touch
  interaction between 3 to 10 seconds in order to perform touchscreen
  gestures directly (as though NVDA is not running; default is 5 seconds).
* Added debug logging messages when performing right clicks (tap and hold)
  to be recorded in the NVDA log (requires NVDA 2017.1 or later).
* Due to changes made when playing screen coordinates, NVDA 2017.1 or later
  is required.

##Версия 17.03

* Fixed an issue where coordinate announcement beep did not play or an error
  tone played instead when using NVDA 2017.1 or later.

##Версия 16.12

* Сенсорный режим веб работает в Microsoft EDGE, Microsoft Word и в других
  приложениях, где используется режим просмотра.
* Добавлены списки и ориентиры для элементов режимаweb touch.

## Версия 16.06

* Первая стабильная версия.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=enhancedTouchGestures
