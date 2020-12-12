# enhancedTouchGestures/installTasks.py
# Copyright 2017-2020 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Routines are partly based on other add-ons,
# particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
addonHandler.initTranslation()


def onInstall():
	import sys
	import gui
	import wx
	if sys.getwindowsversion().build < 9600 and gui.messageBox(
		_(
			# Translators: Dialog text shown when attempting to install the add-on on an unsupported version of Windows
			# (minSupportedVersion is the minimum version required for this add-on).
			"You are using an older version of Windows. This add-on requires Windows 8.1 or later. "
			"Are you sure you wish to install this add-on anyway?"
		),
		# Translators: title of the dialog shown when attempting to install the add-on on an old version of Windows.
		_("Old Windows version"), wx.YES | wx.NO | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION
	) == wx.NO:
		raise RuntimeError("Old Windows version detected")
