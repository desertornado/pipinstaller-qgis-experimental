# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Pipinstaller
                                 A QGIS plugin
 A sperimental plugin to install python modules through pip module
                              -------------------
        begin                : 2014-03-03
        copyright            : (C) 2014 by Luca Mandolesi
        email                : pyarchinit@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os, sys

filepath = os.path.dirname(__file__)

pip_install_folder  = ('%s%s') % (filepath, os.path.join(os.sep, 'pip-1.5.4'))

sys.path.insert(0,pip_install_folder)
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from pipinstallerdialog import PipinstallerDialog


class Pipinstaller:

	def __init__(self, iface):
		# Save reference to the QGIS interface
		self.iface = iface
		# initialize plugin directory
		self.plugin_dir = os.path.dirname(__file__)
		# initialize locale
		locale = QSettings().value("locale/userLocale")[0:2]
		localePath = os.path.join(self.plugin_dir, 'i18n', 'pipinstaller_{}.qm'.format(locale))

		if os.path.exists(localePath):
			self.translator = QTranslator()
			self.translator.load(localePath)

			if qVersion() > '4.3.3':
				QCoreApplication.installTranslator(self.translator)

		# Create the dialog (after translation) and keep reference
		self.dlg = PipinstallerDialog()

	def initGui(self):
		# Create action that will start plugin configuration
		self.action = QAction(
			QIcon(":/plugins/pipinstaller/icon.png"),
			u"Pip installer modules", self.iface.mainWindow())
		# connect the action to the run method
		self.action.triggered.connect(self.run)

		# Add toolbar button and menu item
		self.iface.addToolBarIcon(self.action)
		self.iface.addPluginToMenu(u"&pipinstaller", self.action)

	def unload(self):
		# Remove the plugin menu item and icon
		self.iface.removePluginMenu(u"&pipinstaller", self.action)
		self.iface.removeToolBarIcon(self.action)

	# run method that performs all the real work
	def run(self):
		pluginGui = PipinstallerDialog()
		pluginGui.show()
		self.pluginGui = pluginGui # save
##		# show the dialog
##		self.dlg.show()
##		# Run the dialog event loop
##		result = self.dlg.exec_()
##		# See if OK was pressed
##		if result == 1:
##			pip_install = Pip_installation_process()
##			pip_install.run_installer()
##			# do something useful (delete the line containing pass and
##			# substitute with your code)
