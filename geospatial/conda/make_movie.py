import os
import imageio
import glob

## Make movie
writer = imageio.get_writer('fire_sa_10.mp4', fps=12)

path = '/Users/jordanwalker/Downloads/lance-modis-sa-name/'

filelist = glob.glob(os.path.join(path, '*.jpg'))
filenames = sorted(x for x in filelist)

for im in filenames:
    writer.append_data(imageio.imread(im))
writer.close()