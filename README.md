# Server Web-Image-Management

The aim of this image management tool is to provide a server side service, which scans media albums by cron job or directory change events.

# Album
The image data is organized in albums. Each album is stored in a SQLite database and defined by a name, an optional description and an absolute path to its root, the absolute path to the thumbnail directory. In addition a thesaurus for the mapping of keywords is selected.

## Scanner
The primary operation is scanning the images in an album. It can be started at album root with recursion, but also from a subdirectory with a selected recursion depth. The result is stored in a SQLite Database. Supported image formats are JPG, PNG, GIT and TIF. The basic informations about image resolution, creation and change date are resolved, as well as IPTC tags. The tags are stored in a keyword list inside the album database.

An image is updated, if there are changes in the image name, the extension, media type and modification time. Only in the case of an update the media data is read, which speeds up a rescan. 

###
From the commandline the scanner is started by:
```
usage: scan.py [-h] [-v [VERBOSE]] [-r [RECURSE]] [-d DEPTH] -a ALBUM
               [--album-root ALBUMROOT] [-s SCANSTART] [--db-path DATAPATH]

Server Side Image Management

optional arguments:
  -h, --help            	show this help message and exit
  -v [VERBOSE]          	print details
  -r [RECURSE]          	scan recursive
  -d DEPTH, --depth DEPTH  	depth of recursive scan
  -a ALBUM, --album ALBUM	album name
  --album-root ALBUMROOT	set album root path
  -s SCANSTART, --start 	SCANSTART
                        	scan start path in album root
  --db-path DATAPATH    	set database path; default=data/

```

To create a new album -a and --album-root has to be defined. For the database and thumbnails default values (data, thumb) are used. For different paths the --db-path and --thumb-path have to be defined. After creating the database the scan is started in the root directory.

TODO
* -t              create thumbnails
* --thumb-path    root path for thumbnails (is saved in the album database)
* --thumb-size    size for the bigger resolution of thumbnails

TODO
## Thumbnailer
The thumbnail service creates thumbnails from the already scanned images. The thumbnails are stored in the directory defined in the corresponding entry of the album database. If the scanner is called with the -t parameter, thumbnailing is done while scanning. In the image database the creation datetime of the thumbnail is stored. During a rescan with the -t parameter, only the thumbnails with different datetimes are recreated.

## Thesaurus
In contrast to the keyword list of the album, which is a flat list without any hierarchy, the thesaurus offers different types of links between terms. The advantage is, that a search can get results also following the links. There can be used hierarchical, equivalent and related links as well as synonyms. So the thesaurus is a static structure of related (linked) terms, while the keywords of the album can change with the import of new images.

### Mapping
The map routine creates connections between the keywords of an album and the terms of a thesaurus. If the term does not exist in the thesaurus, it will be created with the status 'candidate'. There can be many thesauri, but each album can only be matched to one thesaurus. By remapping to another thesaurue, the mapping date in the album will be overwritten. A thesaurus can be used for many albums for the mapping is unidirectional from the album to the thesaurus.

```
usage: map.py [-h] [-v [VERBOSE]] [-r [RECURSE]] -a ALBUM -t THESAURUS
              [--db-path DATAPATH]

Server Side Image Management

optional arguments:
  -h, --help            	show this help message and exit
  -v [VERBOSE]          	print details
  -r [RECURSE]          	scan recursive
  -a ALBUM, --album ALBUM 	album name
  -t THESAURUS, --thesaurus THESAURUS
                        	thesaurus name
  --db-path DATAPATH    	set database path; default=data/
```

## Management Web Interface
