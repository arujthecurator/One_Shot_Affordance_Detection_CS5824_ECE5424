# -*- coding: utf-8 -*-

import os
import cv2
from tqdm import tqdm
from PIL import Image
from metrics import *
import numpy as np
from skimage import io
import scipy.misc
import imageio

_EPS = 1e-16
_TYPE = np.float64

FM = Fmeasure()
EM = Emeasure()
MAE = MAE()
IoU = IoU()
CC = CC()


data_root="/content/gdrive/MyDrive/OSAD_Net/OSAD/save_models"
mask_root = "/content/gdrive/MyDrive/OSAD_Net/datasets/PAD/divide_1/test/masks"
# These paths are valid if you upload your project in google colab. Otherwise, change these paths accordingly.
map_files=os.listdir(data_root)

for map_file in map_files:
    if map_file[-3:]=="pth":
        continue
    pred_root=os.path.join(data_root,map_file)
    print(pred_root)
   
    EM.adaptive_ems=[]
    EM.changeable_ems=[]
    MAE.maes=[]
    IoU.IoUs=[]
    CC.CCs=[]
    FM.precisions = []
    FM.recalls = []
    FM.adaptive_fms = []
    FM.changeable_fms = []

    mask_name_list = sorted(os.listdir(mask_root))
    for mask_name in tqdm(mask_name_list, total=len(mask_name_list)):
        mask_file = os.path.join(mask_root, mask_name)
        mask_images = os.listdir(mask_file)

        for mask_image in mask_images:
          mask_path = os.path.join(mask_root, mask_name, mask_image)
          pred_path = os.path.join(pred_root, mask_name)
          mask_image_nos=os.listdir(mask_path)
          for mask_image_no in mask_image_nos:
            mask_image=os.path.join(mask_path, mask_image_no)
            pred_image=os.path.join(pred_path, mask_image_no)
            if 2>1:   
              mask = cv2.imread(mask_image, cv2.IMREAD_GRAYSCALE)

              pred = cv2.imread(pred_image, cv2.IMREAD_GRAYSCALE)
              
              if pred.shape != mask.shape:
                  pred = cv2.resize(pred, (mask.shape[1], mask.shape[0]))
              EM.step(pred=pred, gt=mask)
              FM.step(pred=pred, gt=mask)

              MAE.step(pred=pred, gt=mask)
              IoU.step(pred=pred, gt=mask)
              CC.step(pred=pred, gt=mask)
    em = EM.get_results()["em"]
    mae = MAE.get_results()["mae"]
    iou = IoU.get_results()['iou']
    cc = CC.get_results()['cc']
    fm = FM.get_results()["fm"]

    results = {

      "MAE": mae,
      "adpEm": em["adp"],
      "meanEm": em["curve"].mean(),
      "maxEm": em["curve"].max(),
      "meanFm": fm["curve"].mean(),
      'IoU': iou,
      'CC': cc,
    }

    print(results)
    str_1 = ""
    for key in results:
        str_1 += key + " " + str(results[key]) + "\n"
        # print(os.path.join(pred_root, 'results.txt'))
    if os.path.exists(os.path.join(pred_root, 'results_3.txt')):
        os.unlink(os.path.join(pred_root, 'results_3.txt'))
    with open(os.path.join(pred_root, 'results_3.txt'), 'a') as f:
        f.write(str_1)


