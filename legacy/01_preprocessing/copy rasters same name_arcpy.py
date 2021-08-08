import os, shutil, arcpy

rgb_path = 'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\1989\\0_25\\east\\PAN\\'
gt_path = 'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\1989\\0_25\\train\\GT\\'
out_path = 'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\1989\\0_25\\train\\PAN\\'

arcpy.env.workspace = rgb_path
rgb_list = arcpy.ListRasters()
print(len(rgb_list))

arcpy.env.workspace = gt_path
gt_list = arcpy.ListRasters()
print(len(gt_list))

print(rgb_path)
counter = 0
for i in rgb_list:
    for j in gt_list:
        if i[-12:] in j:
            arcpy.CopyRaster_management(rgb_path + i, out_path + 'e_' + i)
            counter += 1
        else:
            pass

print('Copied %s rasters' % (counter))
