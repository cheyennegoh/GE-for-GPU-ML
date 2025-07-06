# datasets.py

from PIL import Image
import math
import numpy as np
import kagglehub
import os

def spiral():
    '''
        Generates training data for a network with 2 inputs and 1 output.

        Adapted from mkspiral.c by Alexis P. Wieland of the MITRE Corporation.
    '''
    ds = []

    for i in range(96 + 1):
        angle = i * math.pi / 16
        radius = 6.5 * (104 - i) / 104

        x = radius * math.sin(angle)
        y = radius * math.cos(angle)

        ds.append([x, y, 1])
        ds.append([-x, -y, 0])
    
    return np.array(ds)


def drive():
    handle = 'andrewmvd/drive-digital-retinal-images-for-vessel-extraction'
    drive_path = os.path.join(kagglehub.dataset_download(handle), 'DRIVE', 'training')

    ds = []

    for n in range(21, 40 + 1):
        image_path = os.path.join(drive_path, 'images', f'{n}_training.tif')
        with Image.open(image_path) as im:
            image = np.array(im.convert('L'))

        manual_path = os.path.join(drive_path, '1st_manual', f'{n}_manual1.gif')
        with Image.open(manual_path) as im:
            manual = np.array(im)

        mask_path = os.path.join(drive_path, 'mask', f'{n}_training_mask.gif')
        with Image.open(mask_path) as im:
            mask = np.array(im)

        image = np.lib.stride_tricks.sliding_window_view(image, (3, 3))
        manual = manual[1:-1, 1:-1] // 255
        mask = mask[1:-1, 1:-1].astype(bool)

        ds.append(np.dstack((image.reshape(*image.shape[:-2], -1), manual))[mask])
            
    return np.vstack(ds)
