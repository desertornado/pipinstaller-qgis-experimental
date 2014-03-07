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
 This script initializes the plugin, making it known to QGIS.
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def classFactory(iface):
    # load Pipinstaller class from file Pipinstaller
    from pipinstaller import Pipinstaller
    return Pipinstaller(iface)
