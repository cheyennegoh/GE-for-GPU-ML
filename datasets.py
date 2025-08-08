# datasets.py

from PIL import Image
import math
import numpy as np
import kagglehub
import os

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler

def spiral(n_samples=None, test_size=0.2, random_seed=42):
    X, y = spiral_generate()

    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        test_size=test_size, 
                                                        random_state=random_seed,
                                                        stratify=y)

    X_train, y_train = shuffle(X_train, y_train, random_state=random_seed, n_samples=n_samples)

    return X_train, X_test, y_train, y_test


def spiral_generate():
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

    data = np.array(ds)

    X = data[:,:-1]
    y = data[:,-1]

    return X, y


def drive(n_samples=None, test_size=0.2, random_seed=42):
    image_ids = range(21, 40 + 1)
    image_ids_train, image_ids_test = train_test_split(image_ids,
                                                       test_size=test_size, 
                                                       random_state=random_seed)
    
    X_train, y_train = drive_preprocessing(image_ids_train)
    X_test, y_test = drive_preprocessing(image_ids_test)

    X_train, y_train = RandomUnderSampler(random_state=random_seed).fit_resample(X_train, y_train)
    X_train, y_train = shuffle(X_train, y_train, random_state=random_seed, n_samples=n_samples)

    return X_train, X_test, y_train, y_test


def drive_preprocessing(image_ids, window_size=5):
    handle = 'andrewmvd/drive-digital-retinal-images-for-vessel-extraction'
    drive_path = os.path.join(kagglehub.dataset_download(handle), 'DRIVE', 'training')

    ds = []
    for image_id in image_ids:
        image, manual, mask = drive_load_image(drive_path, image_id)

        image = np.lib.stride_tricks.sliding_window_view(image, 
                                                         (window_size, window_size), 
                                                         axis=(0, 1)) / 255
        
        trim = (window_size - 1) // 2

        manual = manual[trim:-trim, trim:-trim] / 255
        mask = mask[trim:-trim, trim:-trim].astype(bool)

        ds.append(np.dstack((image.reshape(*image.shape[:2], -1), manual))[mask])

    data = np.vstack(ds)
    
    X = data[:,:-1]
    y = data[:,-1]

    return X, y


def drive_load_image(drive_path, image_id, greyscale=True):
    image_path = os.path.join(drive_path, 'images', f'{image_id}_training.tif')
    with Image.open(image_path) as im:
        if greyscale:
            im = im.convert('L')
        image = np.array(im)

    manual_path = os.path.join(drive_path, '1st_manual', f'{image_id}_manual1.gif')
    with Image.open(manual_path) as im:
        manual = np.array(im)

    mask_path = os.path.join(drive_path, 'mask', f'{image_id}_training_mask.gif')
    with Image.open(mask_path) as im:
        mask = np.array(im)

    return image, manual, mask


def drive_get_sample_image(test_size=0.2, random_seed=42):
    handle = 'andrewmvd/drive-digital-retinal-images-for-vessel-extraction'
    drive_path = os.path.join(kagglehub.dataset_download(handle), 'DRIVE', 'training')

    image_ids = range(21, 40 + 1)
    image_ids_test = train_test_split(image_ids,
                                      test_size=test_size, 
                                      random_state=random_seed)[1]
    
    image_id = image_ids_test[0]
    
    image, manual, mask = drive_load_image(drive_path, image_id)

    X_sample, _ = drive_preprocessing([image_id])

    return image, manual, mask, X_sample


def drive_annotate_sample_image(mask, y_sample):
    annotation = mask.copy()
    y_sample_iter = iter(y_sample)

    for i in range(annotation.shape[0]):
        for j in range(annotation.shape[1]):
            if annotation[i, j]:
                annotation[i, j] = 255 * next(y_sample_iter)
    
    return annotation