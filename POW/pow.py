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

htmlTop = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <meta name="robots" content="index, follow" />
  <meta name="keywords" content="projection, cloud, map-a-planet, coordinates, planet, mapping, usgs, nasa, cartography, astrogeology, mars, moon, jupiter, saturn, voyager, cassini" />
  <meta name="description" content="USGS Astrogeology Cloud Imagery Processing" />
  <title>Imagery Processing Cloud - USGS Astrogeology Science Center - Submit page for Map Projection On the Web</title>
  <link href="favicon.ico" rel="shortcut icon" type="image/x-icon" />
  <!-- should use a dynamic stylesheet based on what service/referer -->
  <link rel="stylesheet" href="http://astrocloud.wr.usgs.gov/css/jobs.css" type="text/css" />
<!--[if IE]>
  <link rel="stylesheet" href="http://astrocloud.wr.usgs.gov/css/ie.css" type="text/css" />
<![endif]-->
</head>

<body>
  <div id="header">
    <a href="http://www.usgs.gov">
      <img class="logo" height="70" width="180" src="http://astrocloud.wr.usgs.gov/images/usgs_logo_main_2x.png" alt="USGS: Science for a Changing World"/>
    </a>
    <h1 id="title">Map Projection On the Web</h1>
        </div>
  <div id="wrapper">
    <div id="nav">
      <div id="username"></div>
      <ul class="links">
        <li><a href="http://astrocloud.wr.usgs.gov/index.php?view=login" target="_blank">Login</a></li>
        <li><a href="http://astrocloud.wr.usgs.gov/index.php?view=reset" target="_blank">Reset Your Password</a></li>
        <li><a href="http://astrocloud.wr.usgs.gov/index.php?view=edituser&act=request" target="_blank">Request User Account</a></li>
        <li><a href="http://pilot.wr.usgs.gov" target="_blank">Search Pilot</a></li>
      </ul>
    </div>
<!--
       <div style="background-image:url(http://astrocloud.wr.usgs.gov/images/pow-workflow.png)" class="banner"></div>
       <div class="tabs">
         <a href=""http://astrocloud.wr.usgs.gov/index.php?view=pow" class="active">Map Projection on the Web</a>
       </div>
-->
    <div id="content">
<div class="main-content">
'''

htmlBottom = '''
  <!--
  <h2>Integrated Tools</h2>
  <ul class="def-list">
    <li><span class="label"><a href="http://isis.astrogeology.usgs.gov/UserDocs">ISIS3</a></span> - ISIS (version 3) is an image processing software package. The focus of the software is to manipulate imagery collected by current and past NASA planetary missions sent to Mars, Jupiter, Saturn, and other solar system bodies.
    <li><span class="label"><a href="http://pilot.wr.usgs.gov">PILOT and UPC</a></span> – The Planetary Image LOcator Tool is a web based search tool for the Unified Planetary Coordinate (UPC) database of the Planetary Data System. PILOT features SPICE-corrected image locations and searching capabilities using a navigable map, user selectable image constraints (e.g., incidence angle, solar longitude, pixel resolution and phase angle), and facilitates bulk downloads and/or image processing using POW.
    <li><span class="label"><a href="http://www.gdal.org">GDAL</a></span> – Geospatial Data Abstraction Library is used for conversion from ISIS (version 3) format to GeoTiff, GeoJpeg2000, Jpeg, and PNG. Conversion to PDS format is handled by ISIS.
  </ul>
  <h2>References</h2>
  <ul class="def-list">
    <li><span class="label" style="color:black;">POW</span>
    <ul class="def-list">
      <li>Hare, T.M., et at., (2013), LPSC XLIV, abstract <a href="http://www.lpi.usra.edu/meetings/lpsc2013/pdf/2068.pdf">2068</a></li>
    </ul>
    <li><span class="label" style="color:black;">ISIS</span>
    <ul class="def-list">
      <li>Keszthelyi, L., et al., 2013, LPSC XLIV, abstract <a href="http://www.lpi.usra.edu/meetings/lpsc2013/pdf/2546.pdf">2546</a></li>
      <li>Sides S. et al., 2013, LPSC XLIV, abstract <a href="http://www.lpi.usra.edu/meetings/lpsc2013/pdf/1746.pdf">1746</a></li>
    </ul>
    <li><span class="label" style="color:black;">GDAL</span>
    <ul class="def-list">
      <li>Geospatial Data Abstraction Library <a href="http://www.gdal.org">GDAL</a></li>
    </ul>
    <li><span class="label" style="color:black;">PILOT</span>
    <ul class="def-list">
      <li>Bailen, M.S., et al, (2013), LPSC XLIV, abstract <a href="http://www.lpi.usra.edu/meetings/lpsc2013/pdf/2246.pdf">2246</a></li>
    </ul>
    <li><span class="label" style="color:black;">PDS</span>
    <ul class="def-list">
      <li>Planetary Data System Standards Reference, <a href="http://pds.nasa.gov/tools/standards-reference.shtml">v. 3.8, JPL D-7669, Part 2.</a></li>
    </ul>
    <li><span class="label" style="color:black;">UPC</span>
    <ul class="def-list">
      <li>Akins, S. W., et al, (2009), LPSC XL, abstract <a href="http://www.lpi.usra.edu/meetings/lpsc2009/pdf/2002.pdf">2002</a></li>
    </ul>
  </ul>
  -->
</div>
</div>
<div id="footer">
        <div class="site-links">
          <a href="http://astrocloud.wr.usgs.gov/">home</a>&nbsp;&nbsp;|&nbsp;&nbsp;
          <a href="mailto:astroweb@usgs.gov" >contact</a>&nbsp;&nbsp;|&nbsp;&nbsp;
          <a href="http://isis.astrogeology.usgs.gov/IsisSupport/viewforum.php?f=52" target="_blank">support</a>&nbsp;&nbsp;|&nbsp;&nbsp;
          <a href="http://astrodocs.wr.usgs.gov/index.php/PILOT:Main" target="_blank">help</a>
        </div>
        <div class="gov-links">
          <a href="http://www.doi.gov" target=_top>U.S. Department of the Interior</a> &nbsp;|&nbsp;
          <a href="http://www.usgs.gov" target=_top>U.S. Geological Survey</a>
        </div>
      </div>
  </body>
</html>
'''

htmlHelp = '''
<b>Note:</b> Before submission make sure you are logged in.
To verify, click the "Login" link above. If you are not yet
logged in you will be prompted for your username and password.
If this is your first time on POW, you will need to first request
a user account (link above).
Once you are verified, come back to this page and click the Submit button.<br>
'''

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
                        f.write(htmlTop)
                        f.write(r'<div id="jobdetails">')
                        f.write(r'  <form action="http://astrocloud.wr.usgs.gov/index.php" method="post">')
                        f.write(r'    <input type="hidden" name="view" value="addjob"/>')
                        f.write(r'    <input type="hidden" name="type" value="POW"/>')
                        formURLs = '    <input type="hidden" name="urls" value="%s" />' % urlstring
                        f.write(formURLs)
                        formtarget = '    <input type="hidden" name="target" value="%s" />' % target
                        f.write(formtarget)
                        f.write(r'    <input type="submit" value="Submit"/><br><br>')
                        f.write(htmlHelp)
                        f.write(r'</div>')
                        f.write('<br><h2>Images to be submitted:</h2>\n<br>')
                        f.write('%s' % urlstring.replace(",","<br>\n"))
                        f.write('<br>\n<br>')
                        f.write(htmlBottom)
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

            edridx = self.field_names.index('edr_source')
            targetidx = self.field_names.index('targetname')

            self.dlg.edrfieldname.setCurrentIndex(edridx)
            self.dlg.targetname.setCurrentIndex(targetidx)


    def cleanup(self):
        """
        Cleans up the menu dialog items.
        """
        self.dlg.edrfieldname.clear()
        self.dlg.inputlayers.clear()
        self.dlg.targetname.clear()
