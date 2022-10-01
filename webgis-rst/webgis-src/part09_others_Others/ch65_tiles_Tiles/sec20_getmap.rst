; Author: Bu Kun ; Title: Use GetMap to generate slices

Use GetMap to generate slices
=============================

Here to see the basic principles of map tiles.

Show map slices using an HTML table
-----------------------------------

The following one uses four maps to stitch together into a larger map.
To illustrate the problem, an HTML table was used and four tiles were
placed in table cells in the appropriate locations.

.. raw:: html

   <table class="table table-bordered table-condensed" style="width: 420px; background-color:yellow">

.. raw:: html

   <tr>

.. raw:: html

   <td width="200">

.. raw:: html

   </td>

::

       <td width="200">
           <img src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=80,10,140,60&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles=">
   </td> </tr>
   <tr> <td width="200">
           <img src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=20,-40,80,10&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles=">
   </td>
   <td width="200">
           <img src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=80,-40,140,10&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles=">
   </td> </tr>

.. raw:: html

   </table>

Seamless stitching with DIV
---------------------------

The other way is to seamlessly “splicing” the four images together. The
effect is as follows, which is basically the actual effect of the
current map tile. It looks like a map, actually consisting of four
frames.

.. container::

   ::

      <ul style="margin:0;padding:0;">
          <li style="margin:0;padding:0;list-style-type:none;float:left;width:200px;">
              <img style="display:block;"
                   src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=20,10,80,60&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles="
              />
          </li>
          <li style="margin:0;padding:0;list-style-type:none;float:left;width:200px;">
              <img style="display:block;"
                   src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=80,10,140,60&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles="
              />
          </li>
          <li style="margin:0;padding:0;list-style-type:none;float:left;width:200px;">
              <img style="display:block;"
                   src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=20,-40,80,10&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles="
              />
          </li>
          <li style="margin:0;padding:0;list-style-type:none;float:left;width:200px;">
              <img style="display:block;"
                   src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=80,-40,140,10&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles="
              />
          </li>
      </ul>

.. container:: clear

parameter
---------

.. raw:: html

   <table class="table table-bordered table-condensed" style="width: 420px">

.. raw:: html

   <tr>

.. raw:: html

   <td width="200">

BBOX=20,10,80,60

.. raw:: html

   </td>

.. raw:: html

   <td width="200">

BBOX=80,10,140,60

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="200">

BBOX=20,-40,80,10

.. raw:: html

   </td>

.. raw:: html

   <td width="200">

BBOX=80,-40,140,10

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>
