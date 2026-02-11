# Enhanced touch gestures
# A touchscreen global plugin for NVDA
# Copyright 2013-2026 Joseph Lee, Kefas Lungu, released under GPL.
# Implements needed improvements for various touchscreen gestures.

import globalPluginHandler
from collections.abc import Callable
import touchHandler
import keyboardHandler
import scriptHandler
import ui
from globalCommands import commands
import browseMode
import extensionPoints
import api
import config
import tones
from NVDAObjects import NVDAObject
import wx
from logHandler import log
import addonHandler

addonHandler.initTranslation()

# Notifies when browse mode state has changed, to enter or exit web mode.
post_browseModeStateChange = extensionPoints.Action()


# Disable the add-on completely if touch support is disabled (hardware or this is portable NVDA).
def touchSupportRequired(cls):
	return globalPluginHandler.GlobalPlugin if not touchHandler.touchSupported() else cls


@touchSupportRequired
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Translators: The gestures category for this add-on in input gestures dialog (2013.3 or later).
	scriptCategory = _("Enhanced Touch Gestures")
	# Set up the touch environment for the add-on.
	origAvailTouchModes = len(touchHandler.availableTouchModes) + 1

	def __init__(self):
		super().__init__()
		# Notify if touch support is off.
		# This is useful if using NVDA on a shared computer.
		if not config.conf["touch"]["enabled"]:
			log.debug("etouch: touch support disabled from NVDA")
			tones.beep(380, 100)
			wx.CallAfter(ui.message, "Touch interaction support is disabled")
		# Synth settings ring layer.
		touchHandler.availableTouchModes.append("SynthSettings")
		touchHandler.touchModeLabels["synthsettings"] = "synthsettings mode"
		touchHandler.touchModeLabels["web"] = "web mode"

	# A few setup events please (mostly for web navigation):

	def event_gainFocus(self, obj: NVDAObject, nextHandler: Callable[[], None]):
		# Crucial: Don't do anything unless if it is an installed copy and touchscreen support is active.
		if config.isInstalledCopy() and touchHandler.handler:
			# From 2015 onwards, browse mode module is used.
			if (
				isinstance(obj.treeInterceptor, browseMode.BrowseModeTreeInterceptor)
				and "Web" not in touchHandler.availableTouchModes
			):
				touchHandler.availableTouchModes.append("Web")
				# automatically switch to web mode if any brows mode window is active
				touchHandler.handler._curTouchMode = touchHandler.availableTouchModes[3]
			else:
				# If we're not in browser window, force object mode.
				if "Web" not in touchHandler.availableTouchModes:
					touchHandler.handler._curTouchMode = touchHandler.availableTouchModes[1]
				else:
					curAvailTouchModes = len(touchHandler.availableTouchModes)
					# If we have too many touch modes, restore the original entries.
					if curAvailTouchModes > self.origAvailTouchModes:
						touchHandler.availableTouchModes = touchHandler.availableTouchModes[:self.origAvailTouchModes]
		nextHandler()

	# Global commands: additional touch commands available everywhere.

	@scriptHandler.script(
		description=commands.script_toggleInputHelp.__doc__,
		gesture="ts:4finger_double_tap",
		speakOnDemand=True,
	)
	def script_toggleInputHelp(self, gesture):
		commands.script_toggleInputHelp(gesture)

	@scriptHandler.script(
		description=commands.script_reportCurrentFocus.__doc__,
		gesture="ts:4finger_flickLeft",
		speakOnDemand=True,
	)
	def script_reportCurrentFocus(self, gesture):
		commands.script_reportCurrentFocus(gesture)

	@scriptHandler.script(
		description=commands.script_title.__doc__, gesture="ts:4finger_flickUp", speakOnDemand=True
	)
	def script_title(self, gesture):
		commands.script_title(gesture)

	@scriptHandler.script(
		description=commands.script_reportStatusLine.__doc__,
		gesture="ts:4finger_flickDown",
		speakOnDemand=True,
	)
	def script_reportStatusLine(self, gesture):
		commands.script_reportStatusLine(gesture)

	@scriptHandler.script(
		description=commands.script_speakForeground.__doc__,
		gesture="ts(object):3finger_flickDown",
		speakOnDemand=True,
	)
	def script_speakForeground(self, gesture):
		commands.script_speakForeground(gesture)

	@scriptHandler.script(
		description=commands.script_navigatorObject_current.__doc__,
		gesture="ts:4finger_flickRight",
		speakOnDemand=True,
	)
	def script_navigatorObject_current(self, gesture):
		commands.script_navigatorObject_current(gesture)

	# the following doesn't need speak on demand, skip it.
	# audio ducking mode, cycle speech symbol level, screen curtain toggle, and quit NVDA.

	@scriptHandler.script(
		description=commands.script_cycleAudioDuckingMode.__doc__,
		gesture="ts:4finger_tap",
	)
	def script_audioDuckingMode(self, gesture):
		commands.script_cycleAudioDuckingMode(gesture)

	@scriptHandler.script(
		description=commands.script_cycleSpeechSymbolLevel.__doc__,
		gesture="ts:3finger_double_tap",
	)
	def script_speechSymbolLevel(self, gesture):
		commands.script_cycleSpeechSymbolLevel(gesture)

	@scriptHandler.script(
		description=commands.script_toggleScreenCurtain.__doc__,
		gesture="ts:3finger_triple_tap",
	)
	def script_toggleScreenCurtain(self, gesture):
		commands.script_toggleScreenCurtain(gesture)

	@scriptHandler.script(description=commands.script_quit.__doc__, gesture="ts:2finger_triple_tap")
	def script_quitNvda(self, gesture):
		commands.script_quit(gesture)

	# Web navigation:

	# Web elements list:
	webBrowseElements = (
		"Default",
		"Links",
		"Buttons",
		"Form fields",
		"Headings",
		"Frames",
		"Tables",
		"Lists",
		"Graphics",
		"Landmarks",
		"Embedded objects",
		"Text paragraphs",
	)
	# The starting index for the web browse mode, which flicks through objects.
	webBrowseMode = 0

	# Touch gestures please.
	# doesn't actually need touch on demand since the entire keyboard is also silenced.

	@scriptHandler.script(description="Selects the next web navigation element.", gesture="ts(Web):flickDown")
	def script_nextWebElement(self, gesture):
		self.webBrowseMode = (self.webBrowseMode + 1) % len(self.webBrowseElements)
		ui.message(self.webBrowseElements[self.webBrowseMode])
		log.debug(f"etouch: switching web mode to {self.webBrowseElements[self.webBrowseMode]}")

	@scriptHandler.script(
		description="Selects the previous web navigation element.", gesture="ts(Web):flickUp"
	)
	def script_prevWebElement(self, gesture):
		self.webBrowseMode = (self.webBrowseMode - 1) % len(self.webBrowseElements)
		ui.message(self.webBrowseElements[self.webBrowseMode])
		log.debug(f"etouch: switching web mode to {self.webBrowseElements[self.webBrowseMode]}")

	# The actual navigation gestures:
	# Look up the needed commands for readability purposes.
	browseModeCommands = (
		(
			browseMode.BrowseModeTreeInterceptor.script_nextLink,
			browseMode.BrowseModeTreeInterceptor.script_previousLink,
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextButton,
			browseMode.BrowseModeTreeInterceptor.script_previousButton,
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextFormField,
			browseMode.BrowseModeTreeInterceptor.script_previousFormField,
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextHeading,
			browseMode.BrowseModeTreeInterceptor.script_previousHeading,
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextFrame,
			browseMode.BrowseModeTreeInterceptor.script_previousFrame,
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextTable,
			browseMode.BrowseModeTreeInterceptor.script_previousTable,
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextList,
			browseMode.BrowseModeTreeInterceptor.script_previousList,
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextGraphic,
			browseMode.BrowseModeTreeInterceptor.script_previousGraphic,
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextLandmark,
			browseMode.BrowseModeTreeInterceptor.script_previousLandmark,
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextEmbeddedObject,
			browseMode.BrowseModeTreeInterceptor.script_previousEmbeddedObject,
		),
		(
			browseMode.BrowseModeTreeInterceptor.script_nextTextParagraph,
			browseMode.BrowseModeTreeInterceptor.script_previousTextParagraph,
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

	# Press Tab and Shift+Tab.

	@scriptHandler.script(
		# Translators: input help message for Enhanced touch Gestures command.
		description=_("Emulates pressing tab on the system keyboard"),
		gesture="ts:3finger_flickRight",
	)
	def script_pressTab(self, gesture):
		keyboardHandler.KeyboardInputGesture.fromName("tab").send()

	@scriptHandler.script(
		# Translators: input help message for Enhanced touch Gestures command.
		description=_("Emulates pressing shift+tab on the system keyboard"),
		gesture="ts:3finger_flickLeft",
	)
	def script_pressShiftTab(self, gesture):
		keyboardHandler.KeyboardInputGesture.fromName("shift+tab").send()

	@scriptHandler.script(
		description=commands.script_increaseSynthSetting.__doc__,
		gesture="ts(SynthSettings):2finger_flickUp",
		speakOnDemand=True,
	)
	def script_prevSynthSettingValue(self, gesture):
		commands.script_increaseSynthSetting(gesture)

	@scriptHandler.script(
		description=commands.script_decreaseSynthSetting.__doc__,
		gesture="ts(SynthSettings):2finger_flickDown",
		speakOnDemand=True,
	)
	def script_nextSynthSettingValue(self, gesture):
		commands.script_decreaseSynthSetting(gesture)

	@scriptHandler.script(
		description=commands.script_nextSynthSetting.__doc__,
		gesture="ts(SynthSettings):2finger_flickRight",
		speakOnDemand=True,
	)
	def script_nextSynthSetting(self, gesture):
		commands.script_nextSynthSetting(gesture)

	@scriptHandler.script(
		description=commands.script_previousSynthSetting.__doc__,
		gesture="ts(SynthSettings):2finger_flickLeft",
		speakOnDemand=True,
	)
	def script_prevSynthSetting(self, gesture):
		commands.script_previousSynthSetting(gesture)
