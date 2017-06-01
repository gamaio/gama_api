GAMA API
========

This is the core of the GAMA API. 
It is a django project that defines the core db components and routing.
Different hooks for the API will be written and integrated as seperate "Apps",

Currently Planned:
GPS_API - A service that will provide GPS support for devices such as asset trackers
LOB_API - An update to the lob.li service, moving away from the aging PHP5 code for the API (chrome extension and site itself. Site will be a seperate django project not related to the API)