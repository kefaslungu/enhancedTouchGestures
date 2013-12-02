# Touch Browse Mode
# A touchscreen global plugin for NVDA
# Copyright 2013 Joseph Lee and others, released under GPL.

# Implements needed improvements for web navigation using touchscreens.

import globalPluginHandler # Global plugin please.
import touchHandler # The brain of this plugin.
import ui # Output.
from globalCommands import commands # For certain touch commands.
import virtualBuffers # Web navigation.
from baseObject import ScriptableObject
import api

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Set up the touch environment for the add-on.
	origAvailTouchModes = len(touchHandler.availableTouchModes)

	# A few setup events please (mostly for web navigation):

	def event_gainFocus(self, obj, nextHandler):
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

		# Web browsing gestures:
		"ts(Web):flickDown":"nextWebElement",
		"ts(Web):flickUp":"prevWebElement",
		"ts(Web):flickRight":"nextSelectedElement",
		"ts(Web):flickLeft":"prevSelectedElement"

		# Settings gestures:
		# Two finger left/right/up/down for synth settings ring, one finger flicks for other settings.
	}
