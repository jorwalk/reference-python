# Conda in Docker

Start the docker container
```
docker run -i -t -p 8888:8888 continuumio/miniconda3 /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && mkdir /opt/notebooks && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip=0.0.0.0 --port=8888 --no-browser --allow-root"
```

Install Geospatial libraries
```
# Install a conda package in the current Jupyter kernel
import sys
```

```
!conda install --yes --prefix {sys.prefix} numpy

!conda install --yes --prefix {sys.prefix} pandas

!conda install --yes --prefix {sys.prefix} scipy

!conda install --yes --prefix {sys.prefix} matplotlib

!conda install --yes --prefix {sys.prefix} scikit-learn

!conda install --yes --prefix {sys.prefix} networkx

!conda install --yes --prefix {sys.prefix} bokeh

!conda install --yes --prefix {sys.prefix} beautifulsoup4

!conda install --yes --prefix {sys.prefix} statsmodels

!conda install --yes --prefix {sys.prefix} pyspark

!conda install --yes --prefix {sys.prefix} geopandas

!conda install --yes --prefix {sys.prefix} cartopy

pip install geoplot


conda install -c conda-forge osmnx


conda install -c conda-forge folium
conda install -c conda-forge rasterio
conda install -c conda-forge rasterstats

# Install Dash using Pip
pip install dash==0.19.0  # The core dash backend
pip install dash-renderer==0.11.1  # The dash front-end
pip install dash-html-components==0.8.0  # HTML components
pip install dash-core-components==0.14.0  # Supercharged components
pip install plotly --upgrade  # Plotly graphing library

# Install PyCRS (v. 1.3) using Pip (a fixed version from mullenkamp)
pip install https://github.com/mullenkamp/PyCRS/archive/master.zip
```

## Firemaps
```
https://lance-modis.eosdis.nasa.gov/imagery/firemaps/
```

## Cartopy
```
%matplotlib inline
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_extent([-20, 60, -40, 45], crs=ccrs.PlateCarree())

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS)

plt.show()
```

```
import datetime
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.feature.nightshade import Nightshade


fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

date = datetime.datetime(1999, 12, 31, 12)

ax.set_title('Night time shading for {}'.format(date))
ax.stock_img()
ax.add_feature(Nightshade(date, alpha=0.2))
plt.show()
```


```
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
from owslib.wmts import WebMapTileService

import cartopy.crs as ccrs


# URL of NASA GIBS
URL = 'http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi'
wmts = WebMapTileService(URL)

# Layers for MODIS true color and snow RGB
layers = ['MODIS_Terra_SurfaceReflectance_Bands143',
          'MODIS_Terra_CorrectedReflectance_Bands367']

date_str = '2016-02-05'


plot_CRS = ccrs.Mercator()
geodetic_CRS = ccrs.Geodetic()
x0, y0 = plot_CRS.transform_point(4.6, 43.1, geodetic_CRS)
x1, y1 = plot_CRS.transform_point(11.0, 47.4, geodetic_CRS)

print(x0, y0)
print('-----')
print(x1, y1)

# x0, y0 = (910489.26751227, 6629139.86591456)
# x1, y1 = (2318643.78340736, 7571512.68867450)

ysize = 8
xsize = 2 * ysize * (x1 - x0) / (y1 - y0)

print('-----')
print(xsize)

fig = plt.figure(figsize=(xsize, ysize), dpi=100)

for layer, offset in zip(layers, [0, 0.5]):
    ax = fig.add_axes([offset, 0, 0.5, 1], projection=plot_CRS)
    ax.set_xlim((x0, x1))
    ax.set_ylim((y0, y1))
    ax.add_wmts(wmts, layer, wmts_kwargs={'time': date_str})
    txt = ax.text(4.7, 43.2, wmts[layer].title, fontsize=18, color='wheat',
                  transform=geodetic_CRS)
    txt.set_path_effects([PathEffects.withStroke(linewidth=5,
                                                 foreground='black')])
plt.show()
```

```
import cartopy.feature as cfeature
import numpy as np

central_lat = 37.5
central_lon = -96
extent = [-120, -70, 24, 50.5]
central_lon = np.mean(extent[:2])
central_lat = np.mean(extent[2:])

plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.AlbersEqualArea(central_lon, central_lat))
ax.set_extent(extent)

ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.LAND, edgecolor='black')
ax.add_feature(cartopy.feature.LAKES, edgecolor='black')
ax.add_feature(cartopy.feature.RIVERS)
ax.gridlines()
```

```
rivers_50m = cfeature.NaturalEarthFeature('physical', 'rivers_lake_centerlines', '50m')

plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.AlbersEqualArea(central_lon, central_lat))
ax.set_extent(extent)

ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.LAND, edgecolor='black')
ax.add_feature(rivers_50m, facecolor='None', edgecolor='b')
ax.gridlines()
```


```
! wget https://lance-modis.eosdis.nasa.gov/imagery/gallery/2012270-0926/Miriam.A2012270.2050.2km.jpg
```


```
fig = plt.figure(figsize=(8, 12))

# this is from the cartopy docs
fname = 'Miriam.A2012270.2050.2km.jpg'
img_extent = (-120.67660000000001, -106.32104523100001, 13.2301484511245, 30.766899999999502)
img = plt.imread(fname)

ax = plt.axes(projection=ccrs.PlateCarree())

# set a margin around the data
ax.set_xmargin(0.05)
ax.set_ymargin(0.10)

# add the image. Because this image was a tif, the "origin" of the image is in the
# upper left corner
ax.imshow(img, origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
ax.coastlines(resolution='50m', color='black', linewidth=1)

# mark a known place to help us geo-locate ourselves
ax.plot(-117.1625, 32.715, 'bo', markersize=7, transform=ccrs.Geodetic())
ax.text(-117, 33, 'San Diego', transform=ccrs.Geodetic())
```

## Make animated gif

```
import os,sys
import datetime
import imageio
from pprint import pprint
import time
import datetime
e=sys.exit
 
 
def create_gif(filenames, duration):
	images = []
	for filename in filenames:
		images.append(imageio.imread(filename))
	output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
	imageio.mimsave(output_file, images, duration=duration)
 
 
if __name__ == "__main__":
	script = sys.argv.pop(0)
	duration = 0.2 
	filenames = sorted(filter(os.path.isfile, [x for x in os.listdir() if x.endswith(".jpg")]), key=lambda p: os.path.exists(p) and os.stat(p).st_mtime or time.mktime(datetime.now().timetuple()))
 
	create_gif(filenames, duration)
```
```	
## Make movie	
fileList = []
for file in os.listdir(path):
    if file.startswith(name):
        complete_path = path + file
        fileList.append(complete_path)

writer = imageio.get_writer('test.mp4', fps=20)

for im in fileList:
    writer.append_data(imageio.imread(im))
writer.close()
```

