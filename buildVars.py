# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x: x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/src/56140dbec531e4d7591338e1dbc6192f3dd422a8/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name": "enhancedTouchGestures",
	# Add-on summary, usually the user visible name of the addon.
	# TRANSLATORS: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary": _("Enhanced Touch Gestures"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description": _("""A suite of additional touch commands, including navigation and help commands.
	Requires a touch-enabled computer with Windows 8.1 or later with NVDA 2017.4 or later installed."""),
	# version
	"addon_version": "20.06",
	# Author(s)
	"addon_author": "Joseph Lee <joseph.lee22590@gmail.com>",
	# URL for the add-on documentation support
	"addon_url": None,
	# File name for the add-on help file.
	"addon_docFileName": "readme.html",
	# Minimum NVDA version supported
	"addon_minimumNVDAVersion": "2020.1.0",
	# Last NVDA version supported/tested
	"addon_lastTestedNVDAVersion": "2020.3.0",
	# Minimum Windows version supported
	"addon_minimumWindowsVersion": "6.3.9600",
	# Add-on update channel (default is stable)
	"addon_updateChannel": None,
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "globalPlugins", "enhancedTouchGestures.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
