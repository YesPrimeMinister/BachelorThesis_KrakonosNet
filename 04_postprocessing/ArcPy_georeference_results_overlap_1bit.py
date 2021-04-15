import arcpy
import os
from time import time as time

# created for Python 2.7 (ArcMap for Desktop 10.6)
# ref_path and pred_path need to be set to point into correct folders
reference_path =  '..\\data\\jeseniky\\blackandwhite\\_FULL_size\\' # path to the input tiles, their spatial reference is used for georeferencing
prediction_path = reference_path + 'results\\' # path to the classified tiles without spatial reference
folder = 'krakonosnet_jes_spectarea_1e-4_reclassed_tree90percent'
spatial_res = 0.58

def georeference_folder(ref_path, pred_path):
    list_ref_files = os.listdir(ref_path)
    list_pred_files = os.listdir(pred_path)

    new_path = pred_path + 'georeferenced\\' # path to temp files, they are not deleted automatically
    os.mkdir(new_path)

    out_filename = 'classified_' + folder + '.tif' # Filename of the final merged raster

    i = 0
    for filename in list_pred_files:
        pred_raster = arcpy.Raster(pred_path + filename)
        arr = arcpy.RasterToNumPyArray(pred_raster)

        # clip to the central 256x256 pixels
        array = arr[128:384,128:384]

        ref_raster = arcpy.Raster(ref_path + list_ref_files[i])
        i+=1
    
        arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(5514) #ref_raster.spatialReference
        arcpy.env.snapRaster = ref_raster

        new_file_path = new_path + filename
        # move the lower left point closer to the middle
        ref_lower_left = ref_raster.extent.lowerLeft
        new_lower_left = arcpy.Point(ref_lower_left.X+ 128*spatial_res, ref_lower_left.Y+ 128*spatial_res)

        result_raster = arcpy.NumPyArrayToRaster(array,new_lower_left,ref_raster.meanCellWidth, ref_raster.meanCellHeight)
        result_raster.save(new_file_path)
        del result_raster

    print('Combining rasters')
    out_dataset = arcpy.CreateRasterDataset_management(reference_path + 'complete\\', out_filename, pixel_type='1_BIT', number_of_bands=1, pyramids= 'NONE', raster_spatial_reference=arcpy.SpatialReference(5514))
    arcpy.WorkspaceToRasterDataset_management(new_path, out_dataset)
    arcpy.Delete_management(new_path)

a = time()

georeference_folder(reference_path + "PAN\\", prediction_path)
print('Folder ' + folder + ' finished.')
b = time()
print('Total time elapsed is ' + str((b-a)/60/60) + ' h')

