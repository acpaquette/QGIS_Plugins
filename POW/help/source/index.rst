.. pow documentation master file, created by
   sphinx-quickstart on Sun Feb 12 17:11:03 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Astrogeology Map Processing on the Web (POW)'s documentation!
==========================================================================

POW is a QGIS plugin which provides a GIS based data selection method for submission to the `USGS Astrogeology Map Processing on the Web`_ tool.

In order to use this plugin for processing, you must have `registered for a POW account`_   Registration is completely free and assists in tracking usage of the system.

To use the plugin, simply select less than 50 footprints from a vector footprint shapefile, identify the column which contains the path to a PDS hosted EDR datafile and the column that contains a target name.  On submission, the plugin will open a webbrowser with a submit button and a list of the selected data products.  Clicking submit on the browser will POST the job to the POW web service.

Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _USGS Astrogeology Map Processing on the Web: http://astrocloud.wr.usgs.gov
.. _registered for a POW account: http://astrocloud.wr.usgs.gov/index.php?view=edituser&act=request.
