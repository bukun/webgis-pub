.. Author: Bu Kun .. Title: Publish a vector layer

Publish a vector layer
======================

This section begins with using vector data in MapServer. Vector data is
similar to vector data in CAD software or illustrator. In addition to
the difference of geospatial location, another important aspect is that
vector data in GIS has no style information. CAD or illustrator mainly
focuses on drawing, and the vector data used need to be distinguished
and beautified by width, color and style. In GIS, these works are
completed by the map drawing stage. The same data can be drawn in
different thematic maps and different application scenarios.

Define vector layers in Mapfile
-------------------------------


Mapserver can create an image and save it to a local directory, or
deliver it directly to a web browser on demand (as in this example).
Note the above map, it is generated by the WebGIS server in the
server-side background, and then transmitted to the client. The code
behind in the page is:

::

   <img alt="" border="1"
    src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfa1.map&layer=world-country&mode=map" />

Instead of browsing it on the HTML page, you can just enter this URL:

http://webgis.pub /
cgi-bin/mapserv?map=/owg/example1-1.map&layer=world-country&mode=map

(Remember to replace the hostname or IP address; for example, use the
local hostname ``localhost``, or use the IP address directly, such as
``"127.0.0.1"``)


.. literalinclude:: ./mfa1.map
   :lineno-start: 1


Take a look at this Mapfile below. Lines ``07`` to ``19`` define the
first layer of the map.

The layer starts with ``LAYER`` and ends with ``END``. Based on the
spatial data of ``wcountry.shp1``, the polygon layer renders the global
administrative division data. The ``NAME`` keyword specifies the name of
the layer. The name itself is optional, but if you use one, it must be
no more than 20 characters. The layer name is used in the HTML template
layer as a ``CGI`` reference. A name must be specified if you want the
interactive layer to be able to be toggled on and off from the HTML
form.

The ``STATUS`` keyword determines whether the layer is rendered, and
whether its state can be changed. ``STATUS`` the default layer is always
rendered and can change state at the same time.

Lines ``12`` to ``18`` specify the only class object parameter at this
level. A class object is started with the keyword ``class`` and
terminated by the keyword ``END`` (line ``18``). While this application
will use classes more extensively than previous maps, with this layer,
you only need to specify a single default class that will include every
feature in the shapefile. The name of the class will appear on the
legend associated with the map. If a class has no name, it will still be
rendered, but it will not appear in the legend. The style object keyword
``COLOR`` specifies the color to paint, and ``OUTLINECOLOR`` specifies
the color to paint the border. Since this layer is a polygon, it will be
filled with the specified color. Note that if the layer is a line layer,
the ``COLOR`` value will specify the color of the line.

URL parameter description
-------------------------

The URL can be broken down into three parts:

The first part, ``http://webgis.pub/cgi-bin/mapserv?``, calls MapServer’s CGI
program. On a different system, it might be ``mapserv`` or
``mapserv.exe`` , or something else. If you directly call to open the
above URL, you will get this message:

::

   No query information to decode. QUERY_STRING is set, but empty.

To get the correct information, you need to add additional parameters.

To get the correct information, additional parameters need to be added.
The next three parts are the query string. The query string contains CGI
parameters (variables and their values), with each parameter separated
by a symbol (``&``).

Now looking at the query string, the first parameter ``map`` has a
value: ``/owg/mfa1.map``

The next parameter, ``layer=states``, tells mapserv to use the
``states`` layer. We named the layer object ``states`` in the Mapfile.

Next parameter ``layer=states`` Tell mapserv to use the ``states``
Layer. We name it layer objects in Mapfile ``states`` .

The last parameter, ``mode=map`` , tells mapserv what to do to output
MapFile in mode. In this case, it tells ``mapserv`` to dump the image
directly to the web browser (client), without first creating a temporary
image on the server.

The values for ``TYPE`` can be:
``'chart', 'circle', 'line', 'point', 'polygon', 'raster', 'query', 'annotation'``.

Map extent
----------

In the Mapfile, the correct range needs to be set in order to display
the data. For example, for China-wide data, the set range is:
``EXTENT 73 8 136 53``, the effect is as follows:

The complete Mapfile is:


.. literalinclude:: ./mfs1.map
   :lineno-start: 1


Different modes viewed by MapServer
-----------------------------------

Note the ``mode=map`` above, which is the viewing mode supported by
MapServer. MapServer’s ``mode`` CGI variable can take values other than
``map``. In addition to the ``map`` mode, there is also the ``browse``
mode. For example, if you use ``map=browse``, MapServer will dump the
image to a temporary directory on the server.

Using browse mode requires specifying the ``template`` parameter.
Generally, a template file needs to be defined first. Without a template
file, browse mode cannot work properly, which will be explained later.
In MapServer 6.x, the ``template`` parameter allows the use of the
OpenLayers keyword, which can be used to view MapServer results.

The following directly uses the default configuration of OpenLayers to
view the map. Note that the OpenLayers library of the MapServer website
needs to be called, so it will be slower for the first time.

http://webgis.pub/cgi-bin/mapserv?map=/owg/mfa1.map&layer=states&mode=browse&template=OpenLayers

For OpenLayers mode, see:

https://mapserver.org/uk/cgi/openlayers.html

You can try modifying the value of the keyword in MapFile and see the
result. These experiments will help you understand these keywords.
