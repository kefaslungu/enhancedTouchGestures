# Enhanced touch gestures
# A touchscreen global plugin for NVDA
# Copyright 2013-2014 Joseph Lee and others, released under GPL.

# Implements needed improvements for various touchscreen gestures.

import globalPluginHandler
import touchHandler
import ui
from globalCommands import commands
import virtualBuffers
import api
import winUser
import mouseHandler
import config

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Set up the touch environment for the add-on.
	origAvailTouchModes = len(touchHandler.availableTouchModes)

	# A few setup events please (mostly for web navigation):

	def event_gainFocus(self, obj, nextHandler):
		# Crucial: Don't do anything unless if it is an installed copy and touchscreen support is active.
		if config.isInstalledCopy() and touchHandler.handler:
			if isinstance(obj.treeInterceptor, virtualBuffers.VirtualBuffer):
				if "Web" not in touchHandler.availableTouchModes:
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
	webBrowseElements=["normal", "Link", "Form", "Heading", "Frame", "Table"]
	webBrowseMode = 0 # The starting index for the web browse mode, which flicks through objects.

	# Touch gestures please.

	def script_nextWebElement(self, gesture):
		self.webBrowseMode = 0 if self.webBrowseMode+1 == len(self.webBrowseElements) else self.webBrowseMode +1
		ui.message(self.webBrowseElements[self.webBrowseMode])
	script_nextWebElement.__doc__="Selects the next web navigation element."

	def script_prevWebElement(self, gesture):
		self.webBrowseMode = len(self.webBrowseElements)-1 if self.webBrowseMode == 0  else self.webBrowseMode -1
		ui.message(self.webBrowseElements[self.webBrowseMode])
	script_prevWebElement.__doc__="Selects the previous web navigation element."

	# The actual navigation gestures:

	def script_nextSelectedElement(self, gesture):
		obj = api.getNavigatorObject().treeInterceptor
		if isinstance(obj, virtualBuffers.VirtualBuffer):
			if self.webBrowseMode == 0: commands.script_navigatorObject_nextInFlow(gesture)
			elif self.webBrowseMode == 1: virtualBuffers.VirtualBuffer.script_nextLink(obj, gesture)
			elif self.webBrowseMode == 2: virtualBuffers.VirtualBuffer.script_nextFormField(obj, gesture)
			elif self.webBrowseMode == 3: virtualBuffers.VirtualBuffer.script_nextHeading(obj, gesture)
			elif self.webBrowseMode == 4: virtualBuffers.VirtualBuffer.script_nextFrame(obj, gesture)
			elif self.webBrowseMode == 5: virtualBuffers.VirtualBuffer.script_nextTable(obj, gesture)

	def script_prevSelectedElement(self, gesture):
		obj = api.getNavigatorObject().treeInterceptor
		if isinstance(obj, virtualBuffers.VirtualBuffer):
			if self.webBrowseMode == 0: commands.script_navigatorObject_previousInFlow(gesture)
			elif self.webBrowseMode == 1: virtualBuffers.VirtualBuffer.script_previousLink(obj, gesture)
			elif self.webBrowseMode == 2: virtualBuffers.VirtualBuffer.script_previousFormField(obj, gesture)
			elif self.webBrowseMode == 3: virtualBuffers.VirtualBuffer.script_previousHeading(obj, gesture)
			elif self.webBrowseMode == 4: virtualBuffers.VirtualBuffer.script_previousFrame(obj, gesture)
			elif self.webBrowseMode == 5: virtualBuffers.VirtualBuffer.script_previousTable(obj, gesture)

	def script_touch_rightClick(self, gesture):
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
		winUser.setCursorPos(x,y)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTDOWN,0,0,None,None)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTUP,0,0,None,None)
	script_touch_rightClick.__doc__="Performs right click at the object under your finger"

	def script_touch_newExplore(self,gesture):
		touchHandler.handler.screenExplorer.moveTo(gesture.tracker.x,gesture.tracker.y,new=True)
		if config.conf["mouse"]["audioCoordinatesOnMouseMove"]:
			w, h, screenWidth, screenHeight = api.getDesktopObject().location
			mouseHandler.playAudioCoordinates(gesture.tracker.x,gesture.tracker.y,screenWidth,screenHeight,config.conf['mouse']['audioCoordinates_detectBrightness'],config.conf['mouse']['audioCoordinates_blurFactor'])
	# Translators: Input help mode message for a touchscreen gesture.
	script_touch_newExplore.__doc__=_("Reports the object and content directly under your finger")

	def script_touch_explore(self,gesture):
		touchHandler.handler.screenExplorer.moveTo(gesture.tracker.x,gesture.tracker.y)
		if config.conf["mouse"]["audioCoordinatesOnMouseMove"]:
			w, h, screenWidth, screenHeight = api.getDesktopObject().location
			mouseHandler.playAudioCoordinates(gesture.tracker.x,gesture.tracker.y,screenWidth,screenHeight,config.conf['mouse']['audioCoordinates_detectBrightness'],config.conf['mouse']['audioCoordinates_blurFactor'])
	# Translators: Input help mode message for a touchscreen gesture.
	script_touch_explore.__doc__=_("Reports the new object or content under your finger if different to where your finger was last")

	__gestures={
		# Add-on specific touch gestures.

		# Additional touch gestures added to global commands:
		# For object mode: moving focus, moving to focus, object name and dimentions.
		# For text mode, moving to top and bottom of text.
		"ts:4finger_double_tap":"toggleInputHelp",
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
		"ts(Web):flickLeft":"prevSelectedElement"

		# Settings gestures:
		# Two finger left/right/up/down for synth settings ring, one finger flicks for other settings.
	}
