# enhancedTouchGestures/installTasks.py
# Copyright 2017-2022 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Routines are partly based on other add-ons,
# particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
addonHandler.initTranslation()


def onInstall():
	import winVersion
	import gui
	import wx
	if winVersion.getWinVer() < winVersion.WIN10:
		gui.messageBox(
			_(
				# Translators: Dialog text shown when attempting to install the add-on on an older version of Windows.
				"You are using an older version of Windows. "
				"This is the last version of Enhanced Touch Gestures add-on to support this version of Windows."
			),
			# Translators: title of the dialog shown when trying to install the add-on on an old version of Windows.
			_("Old Windows version"), wx.OK | wx.ICON_WARNING
		)
