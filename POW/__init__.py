# -*- coding: utf-8 -*-
"""
/***************************************************************************
 POW
                                 A QGIS plugin
 USGS Astrogeology Processing on the Web
                             -------------------
        begin                : 2014-08-26
        copyright            : (C) 2014 by Jay Laura
        email                : jlaura@usgs.gov
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

def classFactory(iface):
    # load POW class from file POW
    from pow import POW
    return POW(iface)
