import arcpy
import os

# created for Python 2.7 (ArcMap for Desktop 10.6)
# ref_path and pred_path need to be set to point into correct folders
ref_path =  '..\\data\\2012\\western\\1\\CIR\\' # path to the input tiles, their spatial reference is used for georeferencing
pred_path = '..\\data\\2012\\western\\results\\1\\' # path to the classified tiles without spatial reference

list_ref_files = os.listdir(ref_path)
list_pred_files = os.listdir(pred_path)

new_path = pred_path + 'georeferenced\\' # path to temp files, they are not deleted automatically
os.mkdir(new_path)

out_filename = 'classified.tif' # Filename of the final merged raster

i = 0
for filename in list_pred_files:
    pred_raster = arcpy.Raster(pred_path + filename)
    arr = arcpy.RasterToNumPyArray(pred_raster)

    ref_raster = arcpy.Raster(ref_path + list_ref_files[i])
    i+=1
    
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(102065) #ref_raster.spatialReference
    arcpy.env.snapRaster = ref_raster

    new_file_path = new_path + filename
    result_raster = arcpy.NumPyArrayToRaster(arr,ref_raster.extent.lowerLeft,ref_raster.meanCellWidth, ref_raster.meanCellHeight)
    result_raster.save(new_file_path)
    del result_raster

out_dataset = arcpy.CreateRasterDataset_management(pred_path, out_filename, pixel_type='2_BIT', number_of_bands=1, pyramids= 'NONE')
arcpy.WorkspaceToRasterDataset_management(new_path, out_dataset)
