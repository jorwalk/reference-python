import os, sys
import datetime
import imageio
from pprint import pprint
import time
import glob
import datetime

e = sys.exit


def create_gif(filenames, duration):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
    imageio.mimsave(output_file, images, duration=duration)


if __name__ == "__main__":
    duration = 0.2
    path = '/Users/jordanwalker/Downloads/lance-modis/'
    filelist = glob.glob(os.path.join(path, '*.jpg'))
    filenames = sorted(x for x in filelist)
    # pprint(filenames)

    create_gif(filenames, duration)
