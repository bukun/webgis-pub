; Author: Bu Kun
; Title: WMS GetMap access

# Use WMS Services GetMap in MapServer

The ``GetMap`` operation is used to generate a map, which can be a picture or a set of graphic elements.
``GetMap`` allows clients to request multiple servers to make overlapping map layers, processing pixel geometry with the same frame of reference, size, and scale.
These layers can be displayed in a certain order on the client side, and transparent pixel technology can be used to display map information from different sources according to human visual requirements.

The ``GetMap`` request usually uses HTTP/GET to call a basic WMS via URL encoding, and can also use HTTP/POST encoding to communicate with an SLD-capable WMS.
The ``GetMap`` request must specify the requested layers (Layers), the styles used by each layer (Styles), the spatial reference system (SRS), the bounding rectangle (BBox), the image format (Format) and size (Width, Height) and other parameters.

Web map services support the display of map views in picture or graphic format.
Image formats include public image formats such as GIF, PNG, JPEG, etc. These formats are supported by most Web browsers, and the display of other graphic formats may also require some helper programs to support. Graphics formats include SVG and WebCGM formats, which are not commonly used in WMS.

In addition, the optional ``Transparent`` parameter is used to specify whether the background of the map is transparent. The default value is ``False`` . A function that allows the returned result to be drawn transparently, so that maps for different requests can be overlaid. Each WMS preferably provides an image format that supports transparent display for overlaying with other map images.

A valid ``GetMap`` request will return a map consisting of georeferenced layers with the specified style, spatial reference system, bounding rectangle, size, format, and transparency.
An invalid ``GetMap`` request returns a formatted error message.
In the HTTP context, the content type of the return value is a MIME type.

## Request with GetMap

GetMap access to the published MapServer WMS service is described here.

The first is Mapfile:

->-> mfb2.map

Compared to the previous ``mfa1.map``:

->-> xx_diff_mfb1_mfa1.htmp

This Mapfile is configured with the WMS service. View function:

<a href="{SITE_URL}/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities" target="_blank">
Open a link
</a>

## View the map

Here, use the ``map`` mode of MapServer to view.

<a href="{SITE_URL}/cgi-bin/mapserv?map=/owg/mfb2.map&layer=states&mode=map" target="_blank">
View the map
</a>


## Configure with GetMap

### Without ``GetMap`` enabled

To use ``GetMap``, you need to enable the ``GetMap`` option in WMS:

If not enabled, the access URL will display :

    <ServiceExceptionReport version="1.3.0" xsi:schemaLocation="http://www.opengis.net/ogc http://schemas.opengis.net/wms/1.3.0/exceptions_1_3_0.xsd"><ServiceException>
    msWMSDispatch(): WMS server error. WMS request not enabled. Check wms/ows_enable_request settings.
    </ServiceException></ServiceExceptionReport>


<a href="{SITE_URL}/cgi-bin/mapserv?map=/owg/mfa1.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=-97.5,41.619778,-82.122902,49.38562&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles=" target="_blank">
Click to view
</a>

### Projection is not set up

Note that to use ``GetMap``, the projection must be set. If it is not set, the access will appear:

    <ServiceExceptionReport version="1.3.0" xsi:schemaLocation="http://www.opengis.net/ogc http://schemas.opengis.net/wms/1.3.0/exceptions_1_3_0.xsd"><ServiceException code="InvalidCRS">
    msWMSLoadGetMapParams(): WMS server error. Cannot set new CRS on a map that doesn't have any projection set. Please make sure your mapfile has a projection defined at the top level.
    </ServiceException></ServiceExceptionReport>
    


<a href="{SITE_URL}/cgi-bin/mapserv?map=/owg/mfb1.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=-97.5,41.619778,-82.122902,49.38562&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles=" target="_blank">
Click to view
</a>

### Correct access

Here is the correct way to access it. Note that the length and width parameters passed to the server graph in URL.

It looks like ``GETMAP`` is similar to MapServer's ``mode=map``.

<img class="img_border" alt="Map obtained with GetMap" src="{SITE_URL}/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=-180,-90,180,90&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles=">



<a href="{SITE_URL}/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=-180,-90,180,90&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles=" target="_blank">
Use GetMap
</a>


Note：

Version of WMS 1.1.1 and WMS 1.3.0 have different request parameter for coordinate system :
    
- `SRS=EPSG:4326` for 1.1.1 
- `CRS=CRS:84` for 1.3.0

## Get a partial map with GetMap

The range used above is consistent with the range of the entire data, and the results look no different. Let's zoom out to get a section of the map.

<img class="img_border" alt="Get a partial map with GetMap" src="{SITE_URL}/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=73,3,136,54&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles=">

<a href="{SITE_URL}/cgi-bin/mapserv?map=/owg/mfb2.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=states&BBOX=73,3,136,54&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=200&height=150&styles=" target="_blank">
Get a partial map with GetMap
</a>

According to the description, the parameter ``CRS = EPSG: 4326`` can also be used. But I didn't succeed. You may need to configure mapfile.

The above effect can also be achieved in MapServer CGI control, by setting the ``zoom`` level of browsing, the ``x`` and ``y`` coordinates of the map but ``GetMap`` is obviously more flexible. In addition to these, WMS has more advantages as a standard.