# Enhanced touch gestures
# A touchscreen global plugin for NVDA
# Copyright 2013-2020 Joseph Lee and others, released under GPL.

# Implements needed improvements for various touchscreen gestures.

import globalPluginHandler
import touchHandler
import scriptHandler
import ui
from globalCommands import commands
import globalVars
import browseMode
import api
import winUser
import config
import windowUtils
import tones
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
from NVDAObjects.UIA import UIA
import controlTypes
import wx


# Touch keyboard enhancements
class TouchKey(UIA):

	def _get_states(self):
		# Same as NVDA Core issue 5178: suppress read-only state (reported by a user)
		# Borrowed from Mozilla objects in NVDAObjects/IAccessible/Mozilla.py.
		states = super(TouchKey, self).states
		states.discard(controlTypes.STATE_READONLY)
		return states


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Set up the touch environment for the add-on.
	origAvailTouchModes = len(touchHandler.availableTouchModes) + 1

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		if not touchHandler.touchSupported():
			return
		# Notify if touch support is off.
		# This is useful if using NVDA on a shared computer.
		if not config.conf["touch"]["enabled"]:
			self.etsDebugOutput("etouch: touch support disabled from NVDA")
			tones.beep(380, 100)
			wx.CallAfter(ui.message, "Touch interaction support is disabled")
		# Synth settings ring layer.
		touchHandler.availableTouchModes.append("SynthSettings")
		touchHandler.touchModeLabels["synthsettings"] = "synthsettings mode"
		touchHandler.touchModeLabels["web"] = "web mode"

	# Certain touch objects.
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			if obj.UIAElement.cachedClassName == "CRootKey":
				clsList.insert(0, TouchKey)

	# A few setup events please (mostly for web navigation):

	def event_gainFocus(self, obj, nextHandler):
		# Crucial: Don't do anything unless if it is an installed copy and touchscreen support is active.
		if config.isInstalledCopy() and touchHandler.handler:
			# From 2015 onwards, browse mode module is used.
			if (
				isinstance(obj.treeInterceptor, browseMode.BrowseModeTreeInterceptor)
				and "Web" not in touchHandler.availableTouchModes
			):
				touchHandler.availableTouchModes.append("Web")
			else:
				# If we're not in browser window, force object mode.
				if "Web" not in touchHandler.availableTouchModes:
					touchHandler.handler._curTouchMode = touchHandler.availableTouchModes[1]
				else:
					curAvailTouchModes = len(touchHandler.availableTouchModes)
					# If we have too many touch modes, pop all except the original entries.
					if curAvailTouchModes > self.origAvailTouchModes:
						for i in range(0, curAvailTouchModes - self.origAvailTouchModes):
							touchHandler.availableTouchModes.pop()
		nextHandler()

	# Debugging.

	def etsDebugOutput(self, msg):
		if globalVars.appArgs.debugLogging:
			from logHandler import log
			log.debug(msg)

	# Global commands: additional touch commands available everywhere.

	@scriptHandler.script(gesture="ts:4finger_double_tap")
	def script_toggleInputHelp(self, gesture):
		commands.script_toggleInputHelp(gesture)

	@scriptHandler.script(
		description=commands.script_reportCurrentFocus.__doc__,
		gesture="ts(object):3finger_flickLeft"
	)
	def script_reportCurrentFocus(self, gesture):
		commands.script_reportCurrentFocus(gesture)

	@scriptHandler.script(
		description=commands.script_title.__doc__,
		gesture="ts(object):4finger_flickUp"
	)
	def script_title(self, gesture):
		commands.script_title(gesture)

	@scriptHandler.script(
		description=commands.script_reportStatusLine.__doc__,
		gesture="ts(object):4finger_flickDown"
	)
	def script_reportStatusLine(self, gesture):
		commands.script_reportStatusLine(gesture)

	@scriptHandler.script(
		description=commands.script_speakForeground.__doc__,
		gesture="ts(object):3finger_flickDown"
	)
	def script_speakForeground(self, gesture):
		commands.script_speakForeground(gesture)

	@scriptHandler.script(
		description=commands.script_navigatorObject_current.__doc__,
		gesture="ts(object):3finger_flickRight"
	)
	def script_navigatorObject_current(self, gesture):
		commands.script_navigatorObject_current(gesture)

	# Web navigation:

	# Web elements list:
	webBrowseElements = ("normal", "Link", "Form field", "Heading", "Frame", "Table", "List", "Landmark")
	# The starting index for the web browse mode, which flicks through objects.
	webBrowseMode = 0

	# Touch gestures please.

	@scriptHandler.script(
		description="Selects the next web navigation element.",
		gesture="ts(Web):flickDown"
	)
	def script_nextWebElement(self, gesture):
		self.webBrowseMode = (self.webBrowseMode + 1) % len(self.webBrowseElements)
		ui.message(self.webBrowseElements[self.webBrowseMode])
		self.etsDebugOutput(f"etouch: switching web mode to {self.webBrowseElements[self.webBrowseMode]}")

	@scriptHandler.script(
		description="Selects the previous web navigation element.",
		gesture="ts(Web):flickUp"
	)
	def script_prevWebElement(self, gesture):
		self.webBrowseMode = (self.webBrowseMode - 1) % len(self.webBrowseElements)
		ui.message(self.webBrowseElements[self.webBrowseMode])
		self.etsDebugOutput(f"etouch: switching web mode to {self.webBrowseElements[self.webBrowseMode]}")

	# The actual navigation gestures:
	# Look up the needed commands for readability purposes.
	browseModeCommands = (
		(
			browseMode.BrowseModeTreeInterceptor.script_nextLink,
			browseMode.BrowseModeTreeInterceptor.script_previousLink
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextFormField,
			browseMode.BrowseModeTreeInterceptor.script_previousFormField
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextHeading,
			browseMode.BrowseModeTreeInterceptor.script_previousHeading
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextFrame,
			browseMode.BrowseModeTreeInterceptor.script_previousFrame
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextTable,
			browseMode.BrowseModeTreeInterceptor.script_previousTable
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextList,
			browseMode.BrowseModeTreeInterceptor.script_previousList
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextLandmark,
			browseMode.BrowseModeTreeInterceptor.script_previousLandmark
		),
	)

	@scriptHandler.script(gesture="ts(Web):flickRight")
	def script_nextSelectedElement(self, gesture):
		obj = api.getNavigatorObject().treeInterceptor
		if isinstance(obj, browseMode.BrowseModeTreeInterceptor):
			if self.webBrowseMode == 0:
				commands.script_navigatorObject_nextInFlow(gesture)
			else:
				self.browseModeCommands[self.webBrowseMode - 1][0](obj, gesture)

	@scriptHandler.script(gesture="ts(Web):flickLeft")
	def script_prevSelectedElement(self, gesture):
		obj = api.getNavigatorObject().treeInterceptor
		if isinstance(obj, browseMode.BrowseModeTreeInterceptor):
			if self.webBrowseMode == 0:
				commands.script_navigatorObject_previousInFlow(gesture)
			else:
				self.browseModeCommands[self.webBrowseMode - 1][1](obj, gesture)

	@scriptHandler.script(gesture="ts:4finger_flickRight")
	def script_touchKeyboardEnable(self, gesture):
		# Locate the touch keyboard button and activate it, simulating JAWS 17 gesture.
		keyboardButtonHwnd = windowUtils.findDescendantWindow(
			api.getDesktopObject().windowHandle, className="TIPBand"
		)
		touchKeyboardButton = getNVDAObjectFromEvent(keyboardButtonHwnd, winUser.OBJID_CLIENT, 0)
		try:
			touchKeyboardButton.doAction()
			tones.beep(1000, 150)
		except NotImplementedError:
			# Translators: message shown when touch keyboard button is not found.
			ui.message(_("Cannot activate touch keyboard"))

	@scriptHandler.script(
		description=commands.script_increaseSynthSetting.__doc__,
		gesture="ts(SynthSettings):2finger_flickUp"
	)
	def script_prevSynthSettingValue(self, gesture):
		commands.script_increaseSynthSetting(gesture)

	@scriptHandler.script(
		description=commands.script_decreaseSynthSetting.__doc__,
		gesture="ts(SynthSettings):2finger_flickDown"
	)
	def script_nextSynthSettingValue(self, gesture):
		commands.script_decreaseSynthSetting(gesture)

	@scriptHandler.script(
		description=commands.script_nextSynthSetting.__doc__,
		gesture="ts(SynthSettings):2finger_flickRight"
	)
	def script_nextSynthSetting(self, gesture):
		commands.script_nextSynthSetting(gesture)

	@scriptHandler.script(
		description=commands.script_previousSynthSetting.__doc__,
		gesture="ts(SynthSettings):2finger_flickLeft"
	)
	def script_prevSynthSetting(self, gesture):
		commands.script_previousSynthSetting(gesture)
