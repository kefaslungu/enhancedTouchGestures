# NVDA触摸插件-Enhanced Touch Gestures #

* 作者: Joseph Lee
* 下载 [稳定版][1]
* NVDA compatibility: 2020.1 to 2020.3

此插件为NVDA提供了额外的触摸屏手势。它还提供了一组手势，以便于浏览模式导航。

注意：此插件需要在装有Windows 8.1或10的触摸屏计算机上运行NVDA版本需要 2020.1或以上。

## 快捷键

### 随处可用

* 4指双击：切换输入帮助模式。
* 四指轻弹：切换触摸键盘（通常启用它）。
* Control+Alt+NVDA+T: toggles touch interaction.

### 对象模式

* 3指向下滑动：读取当前窗口。
* 3指向左滑动：报告具有焦点的对象。
* 3指向右滑动：报告当前导航器对象。
* 4指向上滑动：报告当前窗口的标题。
* 4指向下滑动：报告状态栏文本。

## 网络触摸模式

此触摸模式（在浏览模式下可用）允许您按选定元素导航文档。要从浏览模式文档切换到Web模式，请执行3指点击。从该模式，用一个手指向上或向下轻拂循环通过可用的元素导航模式，而用一个手指向右或向左轻拂分别移动到下一个或前一个选择的元素。离开浏览模式文档后，将使用对象触摸模式。

## 语音合成器触摸模式设置

您可以使用此模式快速更改合成器设置，例如选择语音和更改音量。在此模式下，使用两个手指向左或向右滑动以在合成器设置之间移动，并使用两个手指向上和向下轻拂手势来更改值。这种手势反映了键盘上合成器设置响铃命令的手势。

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

## 版本20.06

* 使用 Flake8 解决了许多编码样式问题和潜在错误。

## 版本20.04

* 鼠标右键单击手势（一个手指点击并按住）现在是 NVDA 2020.1 的一部分。

## 版本20.01

* 现在需要NVDA 2019.3或更高版本。
* 如果完全关闭触摸支持，则触摸支持切换命令（包括触摸传递）将不再起作用。

## 版本19.11

* 为其他触摸命令添加输入帮助消息。

## 版本19.09

* 触摸支持现在可以从任何地方禁用，而不仅仅是从配置文件以外的正常配置文件。

## 版本19.07

* 内部更改以支持未来的NVDA版本。

## 版本18.12

* 内部更改以支持未来的NVDA版本。

## 版本18.08

* 兼容NVDA 2018.3和未来版本。

## 版本18.06

* 现在，“增强触摸手势”的设置已整合进NVDA新版设置。因此，需要NVDA 2018.2。
* 修复了wxPython 4的兼容性问题。

## 版本18.04

* 解决了NVDA设置面板中的触摸交互类别可能导致由于此附加组件所做的更改而听到错误声音的问题。

## 版本18.03

* 现在需要NVDA 2018.1。
* 由于NVDA 2018.1带有触摸输入复选框，因此此插件中不再包含该复选框。

## 版本17.12

* 现在需要NVDA 2017.4。具体来说，此附加组件现在可以处理配置文件切换。
* 由于NVDA 2017.4包含屏幕方向通知，因此此功能不再是此插件的一部分。
* 在“触摸交互”对话框中添加了一个隐藏复选框，以完全禁用触摸支持（如果正常配置以外的配置文件处于活动状态。
* If using NVDA 2018.1 or later, Touch Interaction dialog will be listed
  twice under NVDA's preferences menu. The second item is the dialog that
  comes with the add-on.
* 在插件的“触摸交互”对话框中，如果使用NVDA 2018.1或更高版本，则不再显示触摸键入模式。

## 版本17.10

* 由于Microsoft的支持策略，不再支持Windows 8（原始版本）。
* 运行NVDA 2017.4开发快照时，NVDA将不再宣布屏幕方向两次。

## 版本17.07.1

* 在触摸交互对话框中添加了一个选项，可以在不使用计时器的情况下手动切换触摸直通。
* 关闭手动直通模式后，如果在直通持续时间到期之前打开触摸直通，则会启用触摸交互。

## 版本17.07

* 在NVDA的首选项菜单下添加了一个名为Touch Interaction的新对话框，以配置NVDA如何与触摸屏配合使用。
* 安装此版本后，按下触摸键盘上的按键时，必须双击所需的按键。您可以通过在“触摸交互”对话框中启用触摸键入来切换回旧方法。
* 添加了一个命令（未分配），允许NVDA忽略触摸手势长达10秒。
* 在“触摸交互”对话框中添加了一个选项，允许NVDA暂停3到10秒之间的触摸交互，以便直接执行触摸屏手势（就像NVDA未运行;默认为5秒）。
* 在执行右键单击（点击并按住）以记录在NVDA日志中时需要添加调试日志消息（需要NVDA 2017.1或更高版本）。
* 由于在播放屏幕坐标时所做的更改，需要NVDA 2017.1或更高版本。

版本17.03

* 修复了使用NVDA 2017.1或更高版本时未播放坐标公告蜂鸣声或播放错误音的问题。

版本16.12

* Web触摸模式适用于Microsoft Edge，Microsoft Word和其他使用浏览模式的模式。
* 为web触摸模式元素添加了列表和标记。

## 版本16.06

* 发布初始版本。

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ets

[2]: https://addons.nvda-project.org/files/get.php?file=ets-dev
