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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from powdialog import POWDialog
import os.path
import webbrowser

class POW:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'pow_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = POWDialog()
        #Once populated, populate the field list with a list of the fields
        self.dlg.inputlayers.currentIndexChanged[int].connect(self.inputlayerchange)
        self.dlg.inputlayers.setCurrentIndex(-1)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/pow/icon.png"),
            u"AstroPOW", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Astrogeology POW", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Astrogeology POW", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        """
        Main - executed when the plugin is clicked.
        """
        # show the dialog
        if not self.dlg.isVisible():
            print self.dlg
            self.dlg.show()

            #Populate the dialog dropdown with a list of layers
            self.layers = self.iface.legendInterface().layers()
            for layer in self.layers:
                if layer.type() == QgsMapLayer.VectorLayer:
                    self.dlg.inputlayers.addItem(layer.name())


            # Run the dialog event loop
            result = self.dlg.exec_()
            # See if OK was pressed
            if result == 1:
                if len(self.layer.selectedFeatures()) > 50:
                    QMessageBox.information(None,"Error:", "Please select less than 50 footprints.")

                elif len(self.layer.selectedFeatures()) == 0:
                    QMessageBox.information(None, "Error:", "Please select at least 1 footprint to process.")
                    self.cleanup()
                else:
                    urls = []
                    edridx = self.dlg.edrfieldname.currentIndex()
                    targetidx = self.dlg.targetname.currentIndex()
                    for l in self.layer.selectedFeatures():
                        attribs = l.attributes()
                        target = l.attributes()[targetidx]
                        urls.append(l.attributes()[edridx])

                    urlstring = ",".join(urls)
                    writepath = os.path.join(os.path.expanduser('~'), 'tmp.html')
                    with open(writepath, 'w') as f:
                        f.write(r'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">')
                        f.write(r'<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">')
                        f.write(r'<head>')
                        f.write(r'  <meta http-equiv="content-type" content="text/html; charset=utf-8" />')
                        f.write(r'</head>')
                        f.write(r'<body>')
                        f.write(r'   <h2 id="title">Submit page for Map Projection On the Web</h1>')
                        f.write(r'<div id="jobdetails">')
                        f.write(r'  <form action="http://astrocloud.wr.usgs.gov/index.php" method="post">')
                        f.write(r'    <input type="hidden" name="view" value="addjob"/>')
                        f.write(r'    <input type="hidden" name="type" value="POW"/>')
                        formURLs = '    <input type="hidden" name="urls" value="%s" />' % urlstring
                        #formURLs = '    <textarea name="urls" value="%s" rows="10" cols="100"></textarea>' % theURLs
                        f.write(formURLs)
                        #f.write(r'    <p>POW File URLs</p>')
                        #f.write(r'    <textarea name="urls" rows="6" cols="100"></textarea>')
                        #f.write(r'    <p>Target</p>')
                        formTarget = '    <input type="hidden" name="target" value="%s" />' % target
                        f.write(formTarget)
                        #f.write(r'    <input type="hidden" name="target" value="Mars" />')
                        f.write(r'    <input type="submit" value="Submit"/>')
                        #f.write(r'    <input type="hidden" name="__ncforminfo" value="rHjB90aZJn6UB6i_mcmeng1BEd1LHiTuwRUgh7jcYqWJwsER_qUO00PBAQwj05VKp6auERS67nZ6vBH-QDufrNWwbU9r6iJR"></form>')
                        f.write(r'</div>')
                        f.write('<br><b>Images:</b>\n<br>')
                        f.write('%s' % urlstring.replace(",","<br>\n"))
                        f.write(r'</body>')
                        f.write(r'</html>')
                    webbrowser.open('file:///' + writepath)
                    self.cleanup()

            else:
                self.cleanup()

    def inputlayerchange(self, index):
        """
        Watches layer combobox for a change and updates the edrfieldname combobox
        """
        print "I: ", index
        if index > -1:
            #Clear the combobox
            self.dlg.edrfieldname.clear()
            self.dlg.targetname.clear()
            #Set a currentname attribute for debugging
            self.currentlayername = str(self.dlg.inputlayers.currentText())
            #Get the selected layer
            self.layer = self.layers[index]
            #Populate the field names list
            self.field_names = [field.name() for field in self.layer.pendingFields()]

            for f in self.field_names:
                self.dlg.edrfieldname.addItem(f)
                self.dlg.targetname.addItem(f)

    def cleanup(self):
        """
        Cleans up the menu dialog items.
        """
        self.dlg.edrfieldname.clear()
        self.dlg.inputlayers.clear()
        self.dlg.targetname.clear()
