import os, shutil
import numpy as np

west_path = 'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\1989\\0_25\\west\\'
east_path = 'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\1989\\0_25\\east\\'
jeseniky_path = 'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\jeseniky\\blackandwhite\\training_only_spectrozonal_area\\'

train_path = 'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\jeseniky\\blackandwhite\\training_only_spectrozonal_area\\percentile_30\\train\\'
test_path =  'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\jeseniky\\blackandwhite\\training_only_spectrozonal_area\\percentile_30\\test\\'

probability_train  = 0.75

def rnd_raster_assignment(path, train_dir, test_dir, prob, ident):
    gt_path = path + 'GT\\'
    gt_list = os.listdir(gt_path)

    for i in gt_list:
        if np.random.random() < prob:
            shutil.copy(gt_path + i, train_dir + 'GT\\')
            os.rename(train_dir + 'GT\\' + i, train_dir + 'GT\\' + ident + i)
        else:
            shutil.copy(gt_path + i, test_dir + 'GT\\')
            os.rename(test_dir + 'GT\\' + i, test_dir + 'GT\\' + ident + i)

# rnd_raster_assignment(west_path, train_path, test_path, probability_train, '')
# rnd_raster_assignment(east_path, train_path, test_path, probability_train, '')
rnd_raster_assignment(jeseniky_path, train_path, test_path, probability_train, '')
