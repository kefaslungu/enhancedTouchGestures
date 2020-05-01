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
import mouseHandler
import config
import windowUtils
import tones
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
from NVDAObjects.UIA import UIA
import controlTypes
import gui
import wx
import extensionPoints

def playAudioCoordinates(x, y):
	# play audio coordinates function might be gone in a future NVDA release.
	if hasattr(mouseHandler, "playAudioCoordinates"):
		screenWidth, screenHeight = api.getDesktopObject().location[-2:]
		mouseHandler.playAudioCoordinates(x, y, screenWidth, screenHeight, wx.Point(), config.conf['mouse']['audioCoordinates_detectBrightness'], config.conf['mouse']['audioCoordinates_blurFactor'])

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
	origAvailTouchModes = len(touchHandler.availableTouchModes)+1

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		if touchHandler.touchSupported():
			# Turn off touch support at startup if told to do so.
			# This is useful if using NVDA on a shared computer.
			if not config.conf["touch"]["enabled"]:
				self.etsDebugOutput("etouch: disabling touch handler on startup")
				touchHandler.terminate()
				tones.beep(380, 100)
				wx.CallAfter(ui.message, "Touch interaction support is disabled")
			touchHandler.availableTouchModes.append("SynthSettings") # Synth settings ring layer.
			touchHandler.touchModeLabels["synthsettings"] = "synthsettings mode"
			touchHandler.touchModeLabels["web"] = "web mode"
			config.post_configProfileSwitch.register(self.handleConfigProfileSwitch)
			# Also react to touch handler enable/disable notification if changed from settings panel.
			ETSActionTouchHandlerSettingsChanged.register(self.handleConfigProfileSwitch)
			gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(EnhancedTouchGesturesPanel)
		self.touchPassthroughTimer = None

	def terminate(self):
		try:
			gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(EnhancedTouchGesturesPanel)
		except:
			pass

	# Certain touch objects.
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, UIA):
			if obj.UIAElement.cachedClassName == "CRootKey":
				clsList.insert(0, TouchKey)

	# Action handlers.

	def handleConfigProfileSwitch(self):
		# Because some apps have their own handlers for touch, do not let NVDA take over touchscreens.
		# There are also times when turning off touchscreen through a profile is useful.
		# Due to this mechanism, NVDA 2017.4 or later is required.
		# Touch handler toggle will become unnecessary once NVDA Core issue 9682 becomes a reality.
		if hasattr(touchHandler, "setTouchSupport"):
			if not config.conf["touch"]["enabled"]:
				# Manual touch passthrough timer might be active.
				if self.touchPassthroughTimer and self.touchPassthroughTimer.IsRunning:
					self.touchPassthroughTimer.Stop()
					self.touchPassthroughTimer = None
			else:
				self.resumeTouchInteraction(profileSwitch=True)
			return
		if not config.conf["touch"]["enabled"]:
			if touchHandler.handler:
				self.etsDebugOutput("etouch: automatically disabling touch handler")
				touchHandler.terminate()
			else:
				# Manual touch passthrough timer might be active.
				if self.touchPassthroughTimer and self.touchPassthroughTimer.IsRunning:
					self.touchPassthroughTimer.Stop()
					self.touchPassthroughTimer = None
		else:
			if touchHandler.handler is None:
				self.etsDebugOutput("etouch: automatically enabling touch handler")
				self.resumeTouchInteraction(profileSwitch=True)

	# A few setup events please (mostly for web navigation):

	def event_gainFocus(self, obj, nextHandler):
		# Crucial: Don't do anything unless if it is an installed copy and touchscreen support is active.
		if config.isInstalledCopy() and touchHandler.handler:
			# From 2015 onwards, browse mode module is used.
			if isinstance(obj.treeInterceptor, browseMode.BrowseModeTreeInterceptor) and "Web" not in touchHandler.availableTouchModes:
				touchHandler.availableTouchModes.append("Web") # Web browsing gestures.
			else:
				# If we're not in browser window, force object mode.
				if "Web" not in touchHandler.availableTouchModes: touchHandler.handler._curTouchMode = touchHandler.availableTouchModes[1]
				else:
					curAvailTouchModes = len(touchHandler.availableTouchModes)
					# If we have too many touch modes, pop all except the original entries.
					if curAvailTouchModes > self.origAvailTouchModes:
						for i in range(0, curAvailTouchModes-self.origAvailTouchModes): touchHandler.availableTouchModes.pop()
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

	#Web navigation:

	# Web elements list:
	webBrowseElements = ("normal", "Link", "Form field", "Heading", "Frame", "Table", "List", "Landmark")
	webBrowseMode = 0 # The starting index for the web browse mode, which flicks through objects.

	# Touch gestures please.

	@scriptHandler.script(
		description="Selects the next web navigation element.",
		gesture="ts(Web):flickDown"
	)
	def script_nextWebElement(self, gesture):
		self.webBrowseMode = (self.webBrowseMode+1) % len(self.webBrowseElements)
		ui.message(self.webBrowseElements[self.webBrowseMode])
		self.etsDebugOutput("etouch: switching web mode to %s"%self.webBrowseElements[self.webBrowseMode])

	@scriptHandler.script(
		description="Selects the previous web navigation element.",
		gesture="ts(Web):flickUp"
	)
	def script_prevWebElement(self, gesture):
		self.webBrowseMode = (self.webBrowseMode-1) % len(self.webBrowseElements)
		ui.message(self.webBrowseElements[self.webBrowseMode])
		self.etsDebugOutput("etouch: switching web mode to %s"%self.webBrowseElements[self.webBrowseMode])

	# The actual navigation gestures:
	# Look up the needed commands for readability purposes.
	browseModeCommands = (
		(browseMode.BrowseModeTreeInterceptor.script_nextLink, browseMode.BrowseModeTreeInterceptor.script_previousLink),
		(browseMode.BrowseModeTreeInterceptor.script_nextFormField, browseMode.BrowseModeTreeInterceptor.script_previousFormField),
		(browseMode.BrowseModeTreeInterceptor.script_nextHeading, browseMode.BrowseModeTreeInterceptor.script_previousHeading),
		(browseMode.BrowseModeTreeInterceptor.script_nextFrame, browseMode.BrowseModeTreeInterceptor.script_previousFrame),
		(browseMode.BrowseModeTreeInterceptor.script_nextTable, browseMode.BrowseModeTreeInterceptor.script_previousTable),
		(browseMode.BrowseModeTreeInterceptor.script_nextList, browseMode.BrowseModeTreeInterceptor.script_previousList),
		(browseMode.BrowseModeTreeInterceptor.script_nextLandmark, browseMode.BrowseModeTreeInterceptor.script_previousLandmark),
	)

	@scriptHandler.script(gesture="ts(Web):flickRight")
	def script_nextSelectedElement(self, gesture):
		obj = api.getNavigatorObject().treeInterceptor
		if isinstance(obj, browseMode.BrowseModeTreeInterceptor):
			if self.webBrowseMode == 0: commands.script_navigatorObject_nextInFlow(gesture)
			else: self.browseModeCommands[self.webBrowseMode-1][0](obj, gesture)

	@scriptHandler.script(gesture="ts(Web):flickLeft")
	def script_prevSelectedElement(self, gesture):
		obj = api.getNavigatorObject().treeInterceptor
		if isinstance(obj, browseMode.BrowseModeTreeInterceptor):
			if self.webBrowseMode == 0: commands.script_navigatorObject_previousInFlow(gesture)
			else: self.browseModeCommands[self.webBrowseMode-1][1](obj, gesture)

	@scriptHandler.script(
		description=_("Clicks the right mouse button at the current touch position. This is generally used to activate a context menu."),
		gesture="ts:tapAndHold"
	)
	def script_touch_rightClick(self, gesture):
		# NVDA Core issue 3886: NVDA 2020.1 includes right-click gesture.
		if hasattr(commands, "script_touch_rightClick"):
			commands.script_touch_rightClick(gesture)
			return
		self.etsDebugOutput("etouch: attempting to perform right-click")
		obj = api.getNavigatorObject() 
		try:
			p = api.getReviewPosition().pointAtStart
		except (NotImplementedError, LookupError):
			p = None
		if p:
			x = p.x
			y = p.y
		else:
			try:
				left, top, width, height = obj.location
			except:
				# Translators: Reported when the object has no location for the mouse to move to it.
				ui.message(_("object has no location"))
				return
			x = left+(width//2)
			y = top+(height//2)
		self.etsDebugOutput("etouch: mouse point found at %s, %s"%(x, y))
		winUser.setCursorPos(x, y)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTDOWN, 0, 0, None, None)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTUP, 0, 0, None, None)

	@scriptHandler.script(
		description=commands.script_touch_newExplore.__doc__,
		gestures=["ts:tap", "ts:hoverDown"]
	)
	def script_touch_newExplore(self, gesture):
		touchHandler.handler.screenExplorer.moveTo(gesture.x, gesture.y, new=True)
		if config.conf["mouse"]["audioCoordinatesOnMouseMove"]:
			playAudioCoordinates(gesture.x, gesture.y)

	@scriptHandler.script(
		description=commands.script_touch_explore.__doc__,
		gesture="ts:hover"
	)
	def script_touch_explore(self, gesture):
		touchHandler.handler.screenExplorer.moveTo(gesture.x, gesture.y)
		if config.conf["mouse"]["audioCoordinatesOnMouseMove"]:
			playAudioCoordinates(gesture.x, gesture.y)

	@scriptHandler.script(gesture="ts:4finger_flickRight")
	def script_touchKeyboardEnable(self, gesture):
		# Locate the touch keyboard button and activate it, simulating JAWS 17 gesture.
		keyboardButtonHwnd = windowUtils.findDescendantWindow(api.getDesktopObject().windowHandle, className="TIPBand")
		touchKeyboardButton = getNVDAObjectFromEvent(keyboardButtonHwnd, winUser.OBJID_CLIENT, 0)
		touchKeyboardButton.doAction()
		tones.beep(1000, 150)

	def resumeTouchInteraction(self, profileSwitch=False):
		import tones
		if hasattr(touchHandler, "setTouchSupport"):
			if touchHandler.touchSupported():
				touchHandler.setTouchSupport(True)
				if not profileSwitch:
					ui.message("Touch passthrough off")
					tones.beep(380, 100)
			else:
				if not profileSwitch: ui.message("Touch is not supported")
			self.touchPassthroughTimer = None
			return
		if not touchHandler.handler:
			try:
				self.etsDebugOutput("etouch: attempting to enable touch handler")
				touchHandler.initialize()
				if not profileSwitch:
					ui.message("Touch passthrough off")
					tones.beep(380, 100)
			except:
				if not profileSwitch: ui.message("Touch is not supported")
			finally:
				self.touchPassthroughTimer = None

	@scriptHandler.script(
		description="Temporarily disables touch interaction so you can interact with a touchscreen as though NVDA is not running",
		category="Enhanced Touch Gestures"
	)
	def script_toggleTouchPassthrough(self, gesture):
		# No, do not allow passthrough to be toggled if touch support is turned off completely.
		if not config.conf["touch"]["enabled"]:
			ui.message("Touch support is disabled, cannot toggle touch passthrough")
			return
		# First, check if timer is running, and if so, enable touch interaction (manual toggle).
		if ((not touchHandler.handler and config.conf["touch"]["manualPassthroughToggle"])
		or (self.touchPassthroughTimer and self.touchPassthroughTimer.IsRunning())):
			self.etsDebugOutput("etouch: manually enabling touch handler")
			self.resumeTouchInteraction()
			return
		if touchHandler.handler:
			self.etsDebugOutput("etouch: disabling touch handler")
			if hasattr(touchHandler, "setTouchSupport"): touchHandler.setTouchSupport(False)
			else: touchHandler.terminate()
			ui.message("Touch passthrough on")
			import tones
			tones.beep(760, 100)
			if not config.conf["touch"]["manualPassthroughToggle"]:
				self.touchPassthroughTimer = wx.PyTimer(self.resumeTouchInteraction)
				self.touchPassthroughTimer.Start(config.conf["touch"]["commandPassthroughDuration"]*1000, True)

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

# Add-on config database
confspec = {
	"enabled": "boolean(default=True)",
	"touchTyping": "boolean(default=false)",
	"commandPassthroughDuration": "integer(min=3, max=10, default=5)",
	"manualPassthroughToggle": "boolean(default=false)",
}
config.conf.spec["touch"] = confspec

# Notify whenever touch handler settings panel values change.
ETSActionTouchHandlerSettingsChanged = extensionPoints.Action()

class EnhancedTouchGesturesPanel(gui.SettingsPanel):
	# Translators: This is the label for the touch interaction settings dialog.
	title = _("Enhanced Touch Gestures")

	def makeSettings(self, settingsSizer):
		touchHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		if not hasattr(touchHandler, "setTouchSupport"):
			# Translators: This is the label for a checkbox in the
			# Enhanced Touch Gestures settings panel.
			self.enableTouchSupportCheckBox = touchHelper.addItem(wx.CheckBox(self, label=_("Enable touch interaction support")))
			self.enableTouchSupportCheckBox.SetValue(config.conf["touch"]["enabled"])
		# Translators: The label for a setting in Enhanced Touch Gestures settings panel to allow users to interact directly with touchscreens for specified duration in seconds.
		self.commandPassthroughDuration = touchHelper.addLabeledControl(_("&Pause NVDA's touch support (duration in seconds)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=3, max=10, initial=config.conf["touch"]["commandPassthroughDuration"])
		# Translators: a checkbox to allow passthrough to be toggled manually.
		self.manualPassthroughCheckBox = touchHelper.addItem(wx.CheckBox(self, label=_("&Manually toggle touch passthrough")))
		self.manualPassthroughCheckBox.SetValue(config.conf["touch"]["manualPassthroughToggle"])

	def onSave(self):
		if hasattr(self, "enableTouchSupportCheckBox"):
			if config.conf["touch"]["enabled"] and not self.enableTouchSupportCheckBox.IsChecked():
				message = _("You are about to turn off touch interaction support completely so the touchscreen can be used as though NVDA is not running. To enable touch support, you need to return to Enhanced Touch Gestures panel in NVDA Settings and check 'enable touch interaction support' checkbox. Are you sure you wish to completely disable touch interaction support?")
				if gui.messageBox(message, _("Disable touch interaction support"), wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION) == wx.NO:
					return
			config.conf["touch"]["enabled"] = self.enableTouchSupportCheckBox.IsChecked()
		config.conf["touch"]["commandPassthroughDuration"] = self.commandPassthroughDuration.Value
		config.conf["touch"]["manualPassthroughToggle"] = self.manualPassthroughCheckBox.IsChecked()
		ETSActionTouchHandlerSettingsChanged.notify()
