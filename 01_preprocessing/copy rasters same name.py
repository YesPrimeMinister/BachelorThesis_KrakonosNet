import os, shutil

east_rgb_path = 'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\1989\\0_25\\east\\PAN\\'
east_index_len = 12
west_rgb_path = 'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\jeseniky\\blackandwhite\\training_only_spectrozonal_area\\GT_3class\\'
west_index_len = 9

test_gt_path =   'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\jeseniky\\blackandwhite\\training_only_spectrozonal_area\\percentile_30\\test\\PAN\\'
test_out_path =  'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\jeseniky\\blackandwhite\\training_only_spectrozonal_area\\percentile_30\\test\\GT\\'

train_gt_path =  'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\jeseniky\\blackandwhite\\training_only_spectrozonal_area\\percentile_30\\train\\PAN\\'
train_out_path = 'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\jeseniky\\blackandwhite\\training_only_spectrozonal_area\\percentile_30\\train\\GT\\'

def copy_rasters_same_name(rgb_path, gt_path, out_path, index_len):
    rgb_list = os.listdir(rgb_path)
    gt_list = os.listdir(gt_path)

    print(gt_path)
    counter = 0
    for i in rgb_list:
        for j in gt_list:
            if i[-index_len:] in j:
                shutil.copy(rgb_path + i, out_path)
                counter += 1
            else:
                pass

    print('Copied %s rasters' % (counter))

#copy_rasters_same_name(east_rgb_path, train_gt_path, train_out_path, east_index_len)
copy_rasters_same_name(west_rgb_path, train_gt_path, train_out_path, west_index_len)
#copy_rasters_same_name(east_rgb_path, test_gt_path, test_out_path, east_index_len)
copy_rasters_same_name(west_rgb_path, test_gt_path, test_out_path, west_index_len)

