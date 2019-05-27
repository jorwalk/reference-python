- https://pypi.org/project/GDAL/
- https://gis.stackexchange.com/questions/116319/plotting-elevation-maps-and-shaded-relief-images-from-latitude-longitude-and-e
- https://rasterio.readthedocs.io/en/latest/topics/plotting.html
- https://geohackweek.github.io/raster/04-workingwithrasters/
- https://www.google.com/imgres?imgurl=https%3A%2F%2Fgeohackweek.github.io%2Fraster%2F05-pygeotools_rainier%2F19700901_ned1_2003_adj_warp_fig.png&imgrefurl=https%3A%2F%2Fgeohackweek.github.io%2Fraster%2F05-pygeotools_rainier%2F&docid=kE_SN26NZFFJpM&tbnid=8xu4flnIjyKcjM%3A&vet=10ahUKEwj36cnQv9XhAhUIPa0KHXuZB6wQMwh_KDMwMw..i&w=730&h=602&bih=916&biw=1291&q=python%20plot%20elevation%20map&ved=0ahUKEwj36cnQv9XhAhUIPa0KHXuZB6wQMwh_KDMwMw&iact=mrc&uact=8#h=602&imgdii=8xu4flnIjyKcjM:&vet=10ahUKEwj36cnQv9XhAhUIPa0KHXuZB6wQMwh_KDMwMw..i&w=730
- https://www.earthdatascience.org/tutorials/visualize-digital-elevation-model-contours-matplotlib/
- https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.earthdatascience.org%2Fimages%2Fvisualize-digital-elevation-model-contours-matplotlib_files%2Fvisualize-digital-elevation-model-contours-matplotlib_9_0.png&imgrefurl=https%3A%2F%2Fwww.earthdatascience.org%2Ftutorials%2Fvisualize-digital-elevation-model-contours-matplotlib%2F&docid=wHgArdHCgQ6RGM&tbnid=8MMgpzfcdzuRgM%3A&vet=10ahUKEwj36cnQv9XhAhUIPa0KHXuZB6wQMwhDKAQwBA..i&w=664&h=470&bih=916&biw=1291&q=python%20plot%20elevation%20map&ved=0ahUKEwj36cnQv9XhAhUIPa0KHXuZB6wQMwhDKAQwBA&iact=mrc&uact=8

- https://www.google.com/search?biw=1291&bih=916&tbm=isch&sa=1&ei=8UC2XOnVDsmD5wKQg4zACQ&q=python+plot+elevation+map&oq=python+plot+elevation+map&gs_l=img.3..0i24.22916.26233..26518...3.0..1.82.1256.21......1....1..gws-wiz-img.......0j0i67j0i8i30.XlEiB7sULMI

- https://jsfiddle.net/jonataswalker/079xha47/

- https://developer.here.com/api-explorer/maps-js/v3.0

-https://automating-gis-processes.github.io/CSC18/index.html

-https://github.com/sacridini/Awesome-Geospatial

- http://www.data-analysis-in-python.org/t_gis.html

- http://kapadia.github.io/usgs/

- https://github.com/DiegoVicen/som-tsp

- https://github.com/giswqs/lidar

- https://github.com/loicdtx/landsat-extract-gee

- http://www.loicdutrieux.net/landsat-extract-gee/examples.html

- https://rasterio.readthedocs.io/en/stable/topics/plotting.html

- https://wiki.earthdata.nasa.gov/display/GIBS/GIBS+Available+Imagery+Products#expand-CorrectedReflectance16Products

- https://lance-modis.eosdis.nasa.gov/imagery/firemaps/

- https://rabernat.github.io/research_computing_2018/maps-with-cartopy.html
- http://www.net-analysis.com/blog/cartopylayout.html

docker run --rm -it --name osmnx -p 8888:8888 -v "$PWD":/home/jovyan/work gboeing/osmnx

docker run -ti --name nb --rm -v $(pwd)/notebooks:/notebooks -p 8888:8888 quay.io/occ_data/jupyter-geo
docker run -p 8888:8888 quay.io/occ_data/jupyter-geo

docker run -it edce81c52e9f --rm -v "$PWD"/notebooks:/notebooks -p 8888:8888

```
I was inspired today by a NatGeo World Map hanging on a wall.

Using NASA satellite imagery of global active fire detections from MODIS and VIIRS, I created this animation in python showing world fires between 2015 and 2017.


#hackersgonnahack #python #nasa #map 
```