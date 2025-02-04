
======================================================
WebGIS related standards of OGC
======================================================


OGC stands for Open Geospatial Consortium-OGC, which Committed to the standardization of software, data and services in the geographic information industry.


OGC was named Open GIS Consortium from 1994 to 2004, and later changed its name due to business needs.


OGC is a non-profit voluntary international standardization organization that leads the development of spatial geographic information standards and basic positioning services. In the field of spatial data interoperability, the interoperability method based on the public interface access mode is a basic operation method. Through the International Organization for Standardization (ISO/TC211) or technical consortium (such as OGC) to develop interface specifications for spatial data interoperability,
GIS software vendors develop spatial data read and write functions that follow this interface specification, which can realize the interoperability of heterogeneous spatial databases.

The standards formulated and promoted by OGC include WMS, WMTS, WFS, WCS, CSW, WPS and other Web service specifications, as well as related GML, KML and GeoRSS specifications.


Introduction of relevant standardization organizations
=================================================================


**OGC (Open Geospatial Consortium):**

It is an international organization specializing in the standardization of international standards for geospatial information technology. It was established in 1994 and currently has more than 400 members, including companies, research institutes, high schools and government agencies from different countries and regions. One of the important work of OGC is the OWS (OGC Web Services) research program, the purpose of which is to establish a standard framework, enable geographic information to be seamlessly used in a variety of Web, wireless, location-based services and mainstream information technology applications.

**ISO/TC 211 (International Organization for Standardization Geographic Information Technology Committee 211):**

ISO/TC 211 is a technical committee established by an international organization in 1994 to develop standards for geospatial information. The number of standards developed by TC 211 starts from 19101. In general, ISO's standards are more abstract, while OGC's standards are relatively more specific. In recent years, ISO/TC 211 has worked closely with the OGC. For example, OGC's WMS standard is also an ISO standard.

**W3C (World Wide Web Consortium):**

W3C is an organization engaged in the standardization of information technology for the World Wide Web. It was founded in 1994 at the MIT Computer Science Laboratory by TimBemers-Lee, the father of the World Wide Web. The World Wide Web Consortium has developed a series of specifications, among which HTML, CSS, XML Schema, RDF, and SVG have been published with a wide range of influences.
The Basic GeoRSS specification developed by the W3C is still in use, albeit slightly outdated.

## Use of Open Specifications

Here are two types of open specifications.

(1) Open data format

If a data format has a complete description document, it can be read and written by various GIS software, and the inventor of the format does not claim any royalty rights, then the data format is open.

Open data formats in text format include KML (Keyhole Markup Language, Keyhole Markup Language), GeoJSON and TopoJSON, etc. JPEG and PNG are open data formats in raster.

ESRI Shapefile, referred to as Shapefile, is an open format for spatial data developed by the Environmental Systems Research Institute (ESRI).

Currently, the file format has become an open standard in the geographic information software community, demonstrating the importance of ESRI in the global geographic information system market.

Shapefiles are also an important interchange format that enables data interoperability between ESRI and other companies' products.

In contrast to this is ESRI's File Geodatabase, which is a closed format, it cannot be opened and created with any software other than ESRI's tools.

(2)Open specification

The most important open specifications in the GIS industry are a series of specifications formulated by OGC. International Organization for Standardization (ISO) Technical Committee 211 (TC211) is also one of the most important spatial information standards organizations.
At present, ISO/TC 211 has completed or is developing more than 40 international standards for geographic information, including "Geographic Information Reference Model", "Geographic Information Concept Model Language" and "Geographic Information Terminology".

In addition, ESRI, developed in collaboration with several other organizations, which is driving the use of the open GeoServices REST specification. This specification provides a standard method for Web clients to communicate with GIS servers using REST technology. Web services published through ArcGIS for Server adhere to this specification. This means that non-ESRI developers are free to create applications to publish and access Web services that conform to the standard. Although GeoServices REST was not adopted by the OGC, it is a prime example of a voluntary disclosure specification for commercial software.

OGC map service standard introduction
=======================================================

OGC1999 began WMT1 (Web Map Tested) and WMT2 interoperability project. Among them, the famous GML comes from the results of WMT1.

In WMT2, OGC defines three geographic reference information models: Web Map Server (WMS), Web Feature Server (WFS), Web Coverage Server (WCS).

- WMT1: http://www.opengeospatial.org/projects/initiatives/wmt1
- WMT2: http://www.opengeospatial.org/projects/initiatives/wmt2

Cyberspace data service is the most important functional service provided by the data layer to the outside world. In order to realize spatial data sharing and interoperability, the data layer will provide an international standard access interface that conforms to the OGC specification,adopt OWS service model to realize W*S service.
Each service type will conform to the latest protocols and specifications, enabling visual access to map data.

OGC map service protocols, including WMS, WFS, WCS, WMTS, WPS. One of the more important standards that are now used more are GML, WMS and WFS.

Web Map Service (WMS)
--------------------------------------------------------

Web Map Service (WMS) can return corresponding maps
(including raster forms such as PNG, GIF, JPEG,
or vector forms such as SVG and WEB CGM) according to the user's request.

WMS supports the network protocol HTTP,
and the supported operations are defined by URLs.
　
Here are three important operations ``GetCapabilities``, ``GetMap``, ``GetFeatureinfo``.

- ``GetCapabilities`` returns service-level metadata.
- ``GetMap`` returns a map image. 
- ``GetFeatureinfo`` returns information about some special features displayed on the map.

Also some other operations such as ``DescribeLayer``, ``GetLegendGraphic``, ``GetStyles``, ``SetSytles``.

In fact, with the traditional point of view, what ``GetMap`` gets is the result drawn on the control in the desktop program, which is the representation of the data.

``GetFeatureInfo`` is easier to understand, it has the same function as the ``Info`` button used in almost all desktop programs. It is used to obtain information about the screen coordinates. The parameters in ``GetFeatureInfo`` are Screen coordinates, current view range, etc., also facilitate the writing of the client to a certain extent.

``GetFeatureInfo`` can return feature information in multiple layers at the same time, which is the same as the operation in GIS desktop applications. WMS also includes some ``GetLegend`` and other requests to return legend information, which are also completely defined according to the existing standards of the desktop.

The full name of WMS is "Web Map Service". The standard mainly defines three operations for creating and displaying map images: ``GetCapabilities`` (getting service capabilities), ``GetMap`` (getting maps), and ``GetFeatureInfo`` (getting object information).  ``GetMap`` is a common operation, which results in an image of a map.

WFS is an online service standard for geographic elements based on Web service technology. It has two functions.

One is to realize the Web service of geographic data. The data service department has established a geospatial database system to provide online services, and users can obtain the geospatial data they need through this standard. 

The second is the specification for interoperability of heterogeneous systems. Two different geographic information systems can realize the interoperability of heterogeneous data, including data query, browsing, extraction, modification, update and other operations. It can realize remote interoperability based on Web technology.

Web Mapping Services (WMS) make maps from data with geospatial location information. A map is defined as a visual representation of geographic data. it can return the corresponding map (including PNG, GIF, JPEG and other raster forms or SVG and WEB CGM and other vector forms) according to the user's request. WMS supports the network protocol HTTP, and the supported operations are defined by URLs.

WMS provides the following operations:

 - GetCapabitities: Returns service-level metadata, which is a description of service information content and required parameters.
 - GetMap: Returns a map image whose geospatial reference and size parameters are well-defined.
 - GetFeatureInfo: Returns information about some special features displayed on the map.
 - GetLegendGraphic: Returns the legend information of the map.

Web Map Server (WMS) can return corresponding maps (including PNG, GIF, raster such as JPEG or vector such as SVG and WEB CGM). WMS supports the network protocol HTTP, and the supported operations are defined by URLs. There are three important operations ``GetCapabilities``, ``GetMap``, ``GetFeatureinfo``.

- GetCapabilities returns service-level metadata. 
- GetMap returns a map image. 
- GetFeatureinfo returns information about some special features displayed on the map.

Other operations like `DescribeLayer`, `GetLegendGraphic`, `GetStyles`, `SetSytles`.

In fact, to explain with the traditional point of view, what GetMap obtains is the result drawn on the control in the desktop program, which is the performance of the data. GetFeatureInfo is easier to understand. It has the same function as the Info button used in almost all desktop programs, it is used to obtain information about the coordinates of the screen somewhere.

- The parameters in `GetFeatureInfo` are screen coordinates, current view range, etc., which also facilitates the writing of the client to a certain extent. 
- `GetFeatureInfo` can return feature information in multiple layers at the same time, which is the same as ArcGIS Desktop.

WMS also includes some requests to return legend information such as GetLegend, which are also completely defined according to the existing standards of the desktop.

Web Map Service (WMS)
--------------------------------------------------

Make maps from data with geospatial location information. A map is defined as a visual representation of geographic data. The specification defines three operations:

- GetCapabitities returns service-level metadata, which is a description of service information content and required parameters;
- GetMap returns a map image whose geospatial reference and size parameters are well-defined; 
- GetFeatureInfo (optional) returns information about some special features displayed on the map.


Web Feature Service (WFS)
------------------------------------------------------

Web Feature Services (WFS) supports insert, update, delete, retrieve,
and discover services for geographic features.
The service returns GML data based on HTTP client requests.

Its basic connection is: GetCapabilities, DescribeFeatureType,
GetFeature GetCapabilities as above.
DescribeFeatureType returns the feature structure for client queries and other operations. GetFeature can return a GML-compliant data document according to the query requirements. GetFeature is the most important interface. Other interfaces such as Transaction can not only provide element reading, but also support element online editing and transaction processing.

WFS corresponds to the conditional query function in common desktop programs. WFS constructs query conditions through OGC Filter, supports query based on spatial geometric relationship, query based on attribute domain, and of course, includes common query based on spatial relationship and attribute domain. On the Web, WFS requests are not implemented in SQL, but through Filter XML, which is more scalable. What WFS returns is the result set of the query, to a certain extent, it is different from the "data representation" of WMS, The result set of WFS is a result set defined and constrained by a complete Schema, with GML as the carrier. This result set is similar to the data table of the query results of the desktop program.

The function of WFS includes 5 operations: 

- `GetCapabilities` (get service capabilities)
- `DescribeFeatureType` (feature type feature description) 
- `GetFeature` (get object) 
- `Transaction` (transaction processing includes adding, deleting, and modifying elements) 
- `LockFeature` (lock feature)

The first three operations are required operations, which can obtain geographic elements; the latter two are optional operations, which are mainly used for adding, deleting, and modifying geographic elements.

Web Feature Service (WFS) supports users to insert, update, delete, retrieve and discover geographic features through HTTP in a distributed environment. The service returns feature-level GML (Geography Markup Language, Geographic Markup Language) data according to HTTP client requests, and provides transaction operations such as adding, modifying, and deleting features, which is a further development of Web map services. 
WFS constructs query conditions through OGC Filter, supports query based on spatial geometric relationship, query based on attribute domain, and of course also includes common query based on spatial relationship and attribute domain. WFS provides the following operations:

- GetCapabitities: Returns service-level metadata, which is a description of service information content and required parameters. 
- DescribeFeatureType: Generate a Schema to describe the feature types that the WFS implementation can provide.  The Schema description defines how the WFS implementation encodes a feature instance on input and generates a feature instance on output. 
- GetFeature: A data document that conforms to the GML specification can be returned according to the query requirements.
- LockFeature: When the user requests through Transaction, in order to ensure the consistency of the feature information, That is, when a transaction accesses a data item, other transactions cannot modify the data item and add element locks to the element data.
- Transaction: Interaction with feature instances.  This operation can not only provide feature reading, but also support feature online editing and transaction processing. The Transaction operation is optional, and the server chooses whether to support this operation according to the nature of the data.
 
Web Feature Services (WFS) supports insert, update, delete, retrieve, and discover services for geographic features. The service returns GML data based on HTTP client requests.Its basic interfaces are: ``GetCapabilities``, ``DescribeFeatureType``, ``GetFeature``.

- ``GetCapabilities`` as above. 
- ``DescribeFeatureType`` returns the feature structure for client queries and other operations. 
- ``GetFeature`` can return a GML-compliant data document according to the query requirements. GetFeature is the most important interface.

Other interfaces such as Transaction can not only provide element reading, but also support element online editing and transaction processing. WFS corresponds to the conditional query function in common desktop programs. 
WFS constructs query conditions through OGC Filter, supports query based on spatial geometric relationship, query based on attribute domain, and of course, includes common query based on spatial relationship and attribute domain.

On the Web, WFS requests are not implemented in SQL, but through Filter XML, which is more scalable. 

.. ToDo: A bit of a problem. More than just queries. And processing. This is only explained from the operation, not comprehensive. 

What WFS returns is the result set of the query, to a certain extent, it is different from the "data representation" of WMS, The result set of WFS is a result set defined and constrained by a complete Schema, with GML as the carrier. This result set is similar to the data table of the query results of the desktop program.

Web Feature Services (WFS)
------------------------------------------

Web map service returns map-level map images, and Web Feature Service (WFS) returns feature-level GML codes, and provides transaction operations such as adding, modifying, and deleting features, which is a further in-depth development of Web map services. The OGC Web Feature Service allows clients to retrieve geospatial data encoded in the Geographic Markup Language (GML) from multiple Web feature services. The Far East defines five operations:

- GetCapabilites returns Web feature service capability description documents (described in XML); 
- DescribeFeatureType returns an XML document describing the structure of any feature that can be served; 
- GetFeature serves a request to get a feature instance; 
- Transaction provides services for transaction requests; 
- LockFeature handles requests to lock one or more feature type instances during a transaction.

Network Coverage Service (WCS)
-------------------------------------------

Web Geographic Coverage Service (WCS): Provides a spatial raster layer containing geographic information or attributes, instead of static map access. Send corresponding data according to HTTP client request, including imagery, multispectral imagery and other scientific data. Two important operations GetCapabilities, GetCoverage GetCapabilities returns a description of the service and an XML document from which to obtain a collection of covered data. GetCoverage is executed after GetCapabilities determines the query scheme and the data to be acquired, and returns the coverage data. There is also the optional operation DescribeCoverageType.

WCS corresponds to the functions based on raster data, and corresponds to the characteristics of WMS based on vector data. The network coverage service is oriented to spatial image data. It exchanges geospatial data containing geographic location as "COverage" on the Internet, such as raster data such as satellite imagery and digital elevation data. WCS provides the following operations:

- GetCapabitities: Returns service-level metadata, which is a description of service information content and required parameters. 
- DescribeCoverage: Allows users to obtain detailed description documents of one or more coverages from a specific WCS server. 
- GetCoverage: Returns a response document containing or referencing the requested coverage data according to the query request.

Web Geographic Coverage Service (WCS): Provides access to spatial raster layers containing geographic information or attributes rather than static maps. Send corresponding data according to HTTP client request, including imagery, multispectral imagery and other scientific data. Two important operations are ``GetCapabilities``, ``GetCoverage``. 

- ``GetCapabilities`` returns a description of the service and an XML document from which to get a collection of covered data.
- ``GetCoverage`` is executed after GetCapabilities determines the query scheme and the data to be acquired, and returns the coverage data. 

Also an optional action is ``DescribeCoverageType``. WCS corresponds to the functions based on raster data, and corresponds to the characteristics of WMS based on vector data.

The Web Overlay Service (WCS) is oriented towards spatial imagery data, which exchanges geospatial data containing geographic location values with each other on the Internet as "COverage". The network coverage service consists of three operations: GetCapabilities, GetCoverage and DescribeCoverageType. The GetCapabilities operation returns an XML document describing the service and dataset. The GetCoverage operation in the network coverage service is performed after GetCapabilities determines what kind of query can be executed and what kind of data can be obtained. It returns the value or attribute of the geographic location using a common overlay format. The DescribeCoverageType operation allows clients to request a full description of any coverage provided by a specific WCS server.

The above three specifications can not only be used as the spatial data service specification of Web services, but also can be used as the interoperability of spatial data to realize the Far East. 
As long as a certain GIS software supports this interface and is deployed on the local server, other GIS software can obtain the required data through this interface. 
From the perspective of technical implementation, a Web service can be understood as an application program that exposes an interface that can be invoked through the Web to the outside world, allowing it to be invoked by programs written in any platform, any system, and in any language. This application can be implemented in a variety of existing programming languages.
The biggest feature of web services is that they can achieve cross-platform, cross-language, and cross-hardware interoperability. It is SOAP, WSDL and UDDI in web services that ensure the cross-platform interoperability of web services. Therefore, how to use SOAP, WSDL Deploying, describing, transporting and registering a Web service with UDDI is the key to implementing Web services. 
Since SOAP, WSDL and UDDI are a set of standards, different manufacturers can have different products that implement these standards, such as the Web service toolkit based on the JAVA platform launched by companies such as SUN, APACHE, IBM, and Borland, and the .NET proposed by Microsoft. Platform, etc. These tools provide convenient tools for the development, deployment and description of Web services, which greatly reduces the complexity of developing Web services.

Tile Map Service (TMS)
----------------------------------------------------

The Tile Map Service (TMS) defines operations that allow users to access tile maps. WMTS may be OGC's first service standard to support RESTful access.


WPS
---------------------------------------------------------

These specifications are basically supported in major mainstream GIS platforms and open source GIS software. Intergraph has long released the WFS server and interop development kit. ESRI has developed related components in ArcIms to support WMS, WFS and other specifications. 

Another: Web Processing Server (WPS) is a newly introduced standard, and its functions are actually familiar to us. Processing is GeoProcessing in ArcView, such as Union, Intersect and other methods. What WPS needs to do is to expose the URL-based interface to implement the client's invocation of such methods through WebService and return data. These specifications are basically supported in major mainstream GIS platforms and open source GIS software.

MapInfo8.5 has also added the ability to access WMS and WFS services, as well as the interface function of reading GML data. 

GeoServer, MapServer map server plays the role of providing map services to clients in the network. This type of map server can receive unified standard WMS and WFS requests (requests) and return data in multiple formats. This process is strictly regulated by the WMS/WFS specification, so it doesn't really matter to the client what the implementation of its map server is. Such a specification creates the possibility for a public, federated map service.

Client software such as OpenLayers/MapBuilder, uDig, and QGIS are divided into browser and desktop client programs. The B/S system client represented by OpenLayers is now very powerful. It can encapsulate the WMS request and implement the map tile loading function on the browser. In addition, the functions of dragging and zooming are also very perfect, which can realize cross-browser operation. Recent OpenLayers versions also support vector editing, which can be submitted via WFS-t. The traditional desktop client program is more powerful, supporting a variety of data sources including WMS and WFS, in addition, the editing function and operability are also stronger than those in the browser.
