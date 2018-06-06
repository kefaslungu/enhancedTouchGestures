# Enhanced touch gestures
# A touchscreen global plugin for NVDA
# Copyright 2013-2018 Joseph Lee and others, released under GPL.

# Implements needed improvements for various touchscreen gestures.

import globalPluginHandler
import touchHandler
import ui
from globalCommands import commands
import globalVars
import browseMode
import api
import winUser
import mouseHandler
import config
import windowUtils
import win32con
import tones
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
from NVDAObjects.UIA import UIA
import controlTypes
import gui
import wx

def playAudioCoordinates(x, y):
	screenWidth, screenHeight = api.getDesktopObject().location[-2:]
	mouseHandler.playAudioCoordinates(x,y,screenWidth,screenHeight,wx.Point(),config.conf['mouse']['audioCoordinates_detectBrightness'],config.conf['mouse']['audioCoordinates_blurFactor'])

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
			touchHandler.availableTouchModes.append("SynthSettings") # Synth settings ring layer.
			touchHandler.touchModeLabels["synthsettings"] = "synthsettings mode"
			touchHandler.touchModeLabels["web"] = "web mode"
			config.configProfileSwitched.register(self.handleConfigProfileSwitch)
			gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(EnhancedTouchGesturesPanel)
		else:
			self.prefsMenu = None
			self.touchSettings = None
		self.touchPassthroughTimer = None

	def terminate(self):
		try:
			self.prefsMenu.RemoveItem(self.touchSettings)
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
		if config.conf["touch"]["noTouchSupport"]:
			if touchHandler.handler:
				self.etsDebugOutput("etouch: automatically disabling touch handler")
				touchHandler.terminate()
			else:
				# Manual touch passthrough timer might be active.
				if self.touchPassthroughTimer.IsRunning:
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

	def script_toggleInputHelp(self, gesture):
		commands.script_toggleInputHelp(gesture)

	def script_reportCurrentFocus(self, gesture):
		commands.script_reportCurrentFocus(gesture)

	def script_title(self, gesture):
		commands.script_title(gesture)

	def script_reportStatusLine(self, gesture):
		commands.script_reportStatusLine(gesture)

	def script_speakForeground(self, gesture):
		commands.script_speakForeground(gesture)

	def script_navigatorObject_current(self, gesture):
		commands.script_navigatorObject_current(gesture)

	#Web navigation:

	# Web elements list:
	webBrowseElements=("normal", "Link", "Form field", "Heading", "Frame", "Table", "List", "Landmark")
	webBrowseMode = 0 # The starting index for the web browse mode, which flicks through objects.

	# Touch gestures please.

	def script_nextWebElement(self, gesture):
		self.webBrowseMode = (self.webBrowseMode+1) % len(self.webBrowseElements)
		ui.message(self.webBrowseElements[self.webBrowseMode])
		self.etsDebugOutput("etouch: switching web mode to %s"%self.webBrowseElements[self.webBrowseMode])
	script_nextWebElement.__doc__="Selects the next web navigation element."

	def script_prevWebElement(self, gesture):
		self.webBrowseMode = (self.webBrowseMode-1) % len(self.webBrowseElements)
		ui.message(self.webBrowseElements[self.webBrowseMode])
		self.etsDebugOutput("etouch: switching web mode to %s"%self.webBrowseElements[self.webBrowseMode])
	script_prevWebElement.__doc__="Selects the previous web navigation element."

	# The actual navigation gestures:
	# Look up the needed commands for readability purposes.
	browseModeCommands=(
		(browseMode.BrowseModeTreeInterceptor.script_nextLink, browseMode.BrowseModeTreeInterceptor.script_previousLink),
		(browseMode.BrowseModeTreeInterceptor.script_nextFormField, browseMode.BrowseModeTreeInterceptor.script_previousFormField),
		(browseMode.BrowseModeTreeInterceptor.script_nextHeading, browseMode.BrowseModeTreeInterceptor.script_previousHeading),
		(browseMode.BrowseModeTreeInterceptor.script_nextFrame, browseMode.BrowseModeTreeInterceptor.script_previousFrame),
		(browseMode.BrowseModeTreeInterceptor.script_nextTable, browseMode.BrowseModeTreeInterceptor.script_previousTable),
		(browseMode.BrowseModeTreeInterceptor.script_nextList, browseMode.BrowseModeTreeInterceptor.script_previousList),
		(browseMode.BrowseModeTreeInterceptor.script_nextLandmark, browseMode.BrowseModeTreeInterceptor.script_previousLandmark),
	)

	def script_nextSelectedElement(self, gesture):
		obj = api.getNavigatorObject().treeInterceptor
		if isinstance(obj, browseMode.BrowseModeTreeInterceptor):
			if self.webBrowseMode == 0: commands.script_navigatorObject_nextInFlow(gesture)
			else: self.browseModeCommands[self.webBrowseMode-1][0](obj, gesture)

	def script_prevSelectedElement(self, gesture):
		obj = api.getNavigatorObject().treeInterceptor
		if isinstance(obj, browseMode.BrowseModeTreeInterceptor):
			if self.webBrowseMode == 0: commands.script_navigatorObject_previousInFlow(gesture)
			else: self.browseModeCommands[self.webBrowseMode-1][1](obj, gesture)

	def script_touch_rightClick(self, gesture):
		self.etsDebugOutput("etouch: attempting to perform right-click")
		obj=api.getNavigatorObject() 
		try:
			p=api.getReviewPosition().pointAtStart
		except (NotImplementedError, LookupError):
			p=None
		if p:
			x=p.x
			y=p.y
		else:
			try:
				(left,top,width,height)=obj.location
			except:
				# Translators: Reported when the object has no location for the mouse to move to it.
				ui.message(_("object has no location"))
				return
			x=left+(width/2)
			y=top+(height/2)
		self.etsDebugOutput("etouch: mouse point found at %s, %s"%(x, y))
		winUser.setCursorPos(x,y)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTDOWN,0,0,None,None)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTUP,0,0,None,None)
	script_touch_rightClick.__doc__="Performs right click at the object under your finger"

	def script_touch_newExplore(self,gesture):
		touchHandler.handler.screenExplorer.moveTo(gesture.x,gesture.y,new=True)
		if config.conf["mouse"]["audioCoordinatesOnMouseMove"]:
			playAudioCoordinates(gesture.x,gesture.y)
	script_touch_newExplore.__doc__=commands.script_touch_newExplore.__doc__

	def script_touch_explore(self,gesture):
		touchHandler.handler.screenExplorer.moveTo(gesture.x,gesture.y)
		if config.conf["mouse"]["audioCoordinatesOnMouseMove"]:
			playAudioCoordinates(gesture.x,gesture.y)
	script_touch_explore.__doc__=commands.script_touch_explore.__doc__

	def script_touchKeyboardEnable(self, gesture):
		# Locate the touch keyboard button and activate it, simulating JAWS 17 gesture.
		keyboardButtonHwnd = windowUtils.findDescendantWindow(api.getDesktopObject().windowHandle, className="TIPBand")
		touchKeyboardButton = getNVDAObjectFromEvent(keyboardButtonHwnd, winUser.OBJID_CLIENT, 0)
		touchKeyboardButton.doAction()
		tones.beep(1000, 150)

	def resumeTouchInteraction(self, profileSwitch=False):
		if not touchHandler.handler:
			try:
				self.etsDebugOutput("etouch: attempting to enable touch handler")
				touchHandler.initialize()
				if not profileSwitch:
					ui.message("Touch passthrough off")
					import tones
					tones.beep(380, 100)
			except:
				if not profileSwitch: ui.message("Touch is not supported")
			finally:
				self.touchPassthroughTimer = None

	def script_toggleTouchPassthrough(self, gesture):
		# First, check if timer is running, and if so, enable touch interaction (manual toggle).
		if ((not touchHandler.handler and config.conf["touch"]["manualPassthroughToggle"])
		or (self.touchPassthroughTimer and self.touchPassthroughTimer.IsRunning())):
			self.etsDebugOutput("etouch: manually enabling touch handler")
			self.resumeTouchInteraction()
			return
		if touchHandler.handler:
			self.etsDebugOutput("etouch: disabling touch handler")
			touchHandler.terminate()
			ui.message("Touch passthrough on")
			import tones
			tones.beep(760, 100)
			if not config.conf["touch"]["manualPassthroughToggle"]:
				self.touchPassthroughTimer = wx.PyTimer(self.resumeTouchInteraction)
				self.touchPassthroughTimer.Start(config.conf["touch"]["commandPassthroughDuration"]*1000, True)
	script_toggleTouchPassthrough.__doc__ = "Temporarily disables touch interaction so you can interact with a touchscreen as though NVDA is not running"
	script_toggleTouchPassthrough.category = "Enhanced Touch Gestures"

	def script_prevSynthSettingValue(self, gesture):
		commands.script_increaseSynthSetting(gesture)

	def script_nextSynthSettingValue(self, gesture):
		commands.script_decreaseSynthSetting(gesture)

	def script_nextSynthSetting(self, gesture):
		commands.script_nextSynthSetting(gesture)

	def script_prevSynthSetting(self, gesture):
		commands.script_previousSynthSetting(gesture)

	__gestures={
		# Additional touch gestures added to global commands:
		# For object mode: moving focus, moving to focus, object name and dimentions.
		# For text mode, moving to top and bottom of text.
		"ts:4finger_double_tap":"toggleInputHelp",
		"ts:4finger_flickRight":"touchKeyboardEnable",
		"ts(object):3finger_flickLeft":"reportCurrentFocus",
		"ts(object):4finger_flickUp":"title",
		"ts(object):4finger_flickDown":"reportStatusLine",
		"ts(object):3finger_flickDown":"speakForeground",
		"ts(object):3finger_flickRight":"navigatorObject_current",
		"ts:tapAndHold":"touch_rightClick",
		"ts:tap":"touch_newExplore",
		"ts:hoverDown":"touch_newExplore",
		"ts:hover":"touch_explore",

		# Web browsing gestures:
		"ts(Web):flickDown":"nextWebElement",
		"ts(Web):flickUp":"prevWebElement",
		"ts(Web):flickRight":"nextSelectedElement",
		"ts(Web):flickLeft":"prevSelectedElement",

		# Settings gestures:
		"ts(SynthSettings):2finger_flickRight":"nextSynthSetting",
		"ts(SynthSettings):2finger_flickLeft":"prevSynthSetting",
		"ts(SynthSettings):2finger_flickUp":"prevSynthSettingValue",
		"ts(SynthSettings):2finger_flickDown":"nextSynthSettingValue",
	}

# Add-on config database
confspec = {
	"touchTyping": "boolean(default=false)",
	"commandPassthroughDuration": "integer(min=3, max=10, default=5)",
	"manualPassthroughToggle": "boolean(default=false)",
	"noTouchSupport": "boolean(default=false)",
}
config.conf.spec["touch"] = confspec

class EnhancedTouchGesturesPanel(gui.SettingsPanel):
	# Translators: This is the label for the touch interaction settings dialog.
	title = _("Enhanced Touch Gestures")

	def makeSettings(self, settingsSizer):
		touchHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Never, EVER allow touch support to be disabled completely if using normal configuration (only manual passthrough will be allowed).
		if config.conf.profiles[-1].name is not None:
			# Translators: This is the label for a checkbox in the
			# Enhanced Touch Gestures settings panel.
			self.noTouchSupportCheckBox=touchHelper.addItem(wx.CheckBox(self, label=_("Completely disable touch interaction support")))
			self.noTouchSupportCheckBox.SetValue(config.conf["touch"]["noTouchSupport"])
		# Translators: The label for a setting in Enhanced Touch Gestures settings panel to allow users to interact directly with touchscreens for specified duration in seconds.
		self.commandPassthroughDuration=touchHelper.addLabeledControl(_("&Pause NVDA's touch support (duration in seconds)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=3, max=10, initial=config.conf["touch"]["commandPassthroughDuration"])
		# Translators: a checkbox to allow passthrough to be toggled manually.
		self.manualPassthroughCheckBox=touchHelper.addItem(wx.CheckBox(self, label=_("&Manually toggle touch passthrough")))
		self.manualPassthroughCheckBox.SetValue(config.conf["touch"]["manualPassthroughToggle"])

	def onSave(self):
		if config.conf.profiles[-1].name is not None:
			if not config.conf["touch"]["noTouchSupport"] and self.noTouchSupportCheckBox.IsChecked():
				message = _("You are about to turn off touch interaction support completely so the touchscreen can be used as though NVDA is not running. To enable touch support, you need to return to Enhanced Touch Gestures panel in NVDA Settings and uncheck 'disable touch interaction support' checkbox. Are you sure you wish to completely disable touch interaction support?")
				if gui.messageBox(message, _("Disable touch interaction support"), wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION) == wx.NO:
					return
			config.conf["touch"]["noTouchSupport"]=self.noTouchSupportCheckBox.IsChecked()
		config.conf["touch"]["commandPassthroughDuration"] = self.commandPassthroughDuration.Value
		config.conf["touch"]["manualPassthroughToggle"] = self.manualPassthroughCheckBox.IsChecked()
