﻿# Enhanced touch gestures
# A touchscreen global plugin for NVDA
# Copyright 2013-2017 Joseph Lee and others, released under GPL.

# Implements needed improvements for various touchscreen gestures.
# It also includes other support features such as announcing screen orientation.

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

# 17.03 hack: a function to play audio coordinates.
# In NvDA 2017.1, mouse handling extends to multi-monitor setups, hence a min point argument is needed.
def playAudioCoordinates(x, y):
	screenWidth, screenHeight = api.getDesktopObject().location[-2:]
	mouseHandler.playAudioCoordinates(x,y,screenWidth,screenHeight,wx.Point(),config.conf['mouse']['audioCoordinates_detectBrightness'],config.conf['mouse']['audioCoordinates_blurFactor'])

# Keep an eye on orientation changes via a window (credit: Power notification add-on from Tyler Spivey)
class Window(windowUtils.CustomWindow):
	className = u"NVDAOrientationTracker"

	def windowProc(self, hwnd, msg, wParam, lParam):
		# Resolution detection comes from an article found at https://msdn.microsoft.com/en-us/library/ms812142.aspx.
		if msg == win32con.WM_DISPLAYCHANGE:
			ui.message("Landscape" if lParam%0x10000 > lParam/0x10000 else "Portrait")

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
		self.orientationTracker = None
		if touchHandler.handler:
			touchHandler.availableTouchModes.append("SynthSettings") # Synth settings ring layer.
			touchHandler.touchModeLabels["synthsettings"] = "synthsettings mode"
			touchHandler.touchModeLabels["web"] = "web mode"
			self.orientationTracker = Window()
		self.prefsMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.touchSettings = self.prefsMenu.Append(wx.ID_ANY, _("&Touch Interaction..."), _("Touchscreen interaction settings"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onConfigDialog, self.touchSettings)
		self.touchPassthroughTimer = None

	def onConfigDialog(self, evt):
		gui.mainFrame._popupSettingsDialog(TouchInteractionDialog)

	def terminate(self):
		if self.orientationTracker is not None:
			self.orientationTracker = None
		try:
			self.prefsMenu.RemoveItem(self.touchSettings)
		except (RuntimeError, AttributeError, wx.PyDeadObjectError):
			pass

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
	# Translators: Input help mode message for a touchscreen gesture.
	script_touch_newExplore.__doc__=_("Reports the object and content directly under your finger")

	def script_touch_explore(self,gesture):
		touchHandler.handler.screenExplorer.moveTo(gesture.x,gesture.y)
		if config.conf["mouse"]["audioCoordinatesOnMouseMove"]:
			playAudioCoordinates(gesture.x,gesture.y)
	# Translators: Input help mode message for a touchscreen gesture.
	script_touch_explore.__doc__=_("Reports the new object or content under your finger if different to where your finger was last")

	def script_touchKeyboardEnable(self, gesture):
		# Locate the touch keyboard button and activate it, simulating JAWS 17 gesture.
		keyboardButtonHwnd = windowUtils.findDescendantWindow(api.getDesktopObject().windowHandle, className="TIPBand")
		touchKeyboardButton = getNVDAObjectFromEvent(keyboardButtonHwnd, winUser.OBJID_CLIENT, 0)
		touchKeyboardButton.doAction()
		tones.beep(1000, 150)

	def script_touch_hoverUp(self,gesture):
		#Specifically for touch typing with onscreen keyboard keys
		obj=api.getNavigatorObject()
		if isinstance(obj, TouchKey) and config.conf["touch"]["touchTyping"]:
			obj.doAction()

	def resumeTouchInteraction(self):
		if not touchHandler.handler:
			try:
				touchHandler.initialize()
				ui.message("Touch passthrough off")
				import tones
				tones.beep(380, 100)
			except:
				ui.message("Touch is not supported")
			finally:
				self.touchPassthroughTimer = None

	def script_toggleTouchPassthrough(self, gesture):
		if touchHandler.handler:
			touchHandler.terminate()
			ui.message("Touch passthrough on")
			import tones
			tones.beep(760, 100)
			self.touchPassthroughTimer = wx.PyTimer(self.resumeTouchInteraction)
			self.touchPassthroughTimer.Start(config.conf["touch"]["commandPassthroughDuration"]*1000, True)
	script_toggleTouchPassthrough.__doc__ = "Temporarily disables touch interaction so you can interact with a touchscreen as through NVDA is not running"
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
		# Add-on specific touch gestures.

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
		"ts:hoverUp":"touch_hoverUp",
		

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
}
config.conf.spec["touch"] = confspec

class TouchInteractionDialog(gui.SettingsDialog):
	# Translators: This is the label for the touch interaction settings dialog.
	title = _("Touch Interaction")

	def makeSettings(self, settingsSizer):
		touchHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: This is the label for a checkbox in the
		# touch interaction settings dialog.
		self.touchTypingCheckBox=touchHelper.addItem(wx.CheckBox(self, label=_("&Touch typing mode")))
		self.touchTypingCheckBox.SetValue(config.conf["touch"]["touchTyping"])
		# Translators: The label for a setting in touch interaction dialog to allow users to interact directly with touchscreens for specified duration in seconds.
		self.commandPassthroughDuration=touchHelper.addLabeledControl(_("&Pause NVDA's touch support (duration in seconds)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=3, max=10, initial=config.conf["touch"]["commandPassthroughDuration"])

	def postInit(self):
		self.touchTypingCheckBox.SetFocus()

	def onOk(self,evt):
		config.conf["touch"]["touchTyping"]=self.touchTypingCheckBox.IsChecked()
		config.conf["touch"]["commandPassthroughDuration"] = self.commandPassthroughDuration.Value
		super(TouchInteractionDialog, self).onOk(evt)