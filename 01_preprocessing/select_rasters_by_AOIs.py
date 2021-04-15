import os, sys, arcpy

arcpy.env.workspace = 'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\vector\\transekty\\projected_buffers_5513\\' # the area of interest to find the rasters for
AOI_root = arcpy.env.workspace
AOIs    = arcpy.ListFeatureClasses()
rFolder = 'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\2001\\east\\results\\'           # the folder containing the rasters to search from
oFolder = 'c:\\Users\\Admin\\Dokumenty\\Dvorak_BP\\___data_and_code\\data\\2001\\subset\\east\\GT\\'   # the folder to copy to

print(rFolder)
print(len(AOIs))
count = 0
for AOI in AOIs:
    print('processing %s' % (AOI))
    desc = arcpy.Describe(AOI_root + '\\' + AOI) # get the extent of the AOI
    sExt = desc.extent

    arcpy.env.workspace = rFolder

    for ThisRas in arcpy.ListRasters():
        rDesc = arcpy.Describe(ThisRas)
        rExt  = rDesc.extent
        # check if this extent is related spatially
        # by using not disjoint
        arcpy.env.workspace = oFolder
        if sExt.disjoint(rExt):
            pass
        elif ThisRas not in arcpy.ListRasters():
            count += 1
            arcpy.env.workspace = rFolder
            outFile = os.path.join(oFolder, ThisRas)
            arcpy.Copy_management(ThisRas,outFile)
        arcpy.env.workspace = rFolder

print('%i rasters were copied' % (count))
