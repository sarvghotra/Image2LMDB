from __future__ import print_function
import os
import numpy as np
import torch
import cv2
import imageio
import random
from scipy import signal
from subprocess import check_output
import pathlib

from math import ceil, floor

###################### get image path list ######################
IMG_EXTENSIONS = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP']


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)


def get_paths_from_images(path, p_get_img_files=True):
    '''get image path list from image folder'''
    assert os.path.isdir(path), '{:s} is not a valid directory'.format(path)

    images = []
    list_dir = str(pathlib.Path(__file__).parent.absolute()) + '/listdir'
    file_names = check_output([list_dir, path])
    fnames = file_names.decode().strip().split('\n')

    for fname in sorted(fnames):
        # get all the files
        if not p_get_img_files:
            img_path = os.path.join(path, fname)
            images.append(img_path)
        # just image type files
        elif is_image_file(fname):
            img_path = os.path.join(path, fname)
            images.append(img_path)
    assert images, '{:s} has no valid image file'.format(path)
    return images
