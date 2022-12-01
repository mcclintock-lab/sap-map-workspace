# prints bounding box of shapes to be rasterized
import geopandas as gpd

shps = gpd.read_file('/Users/petermenzies/SeaSketch/azores/azo-ous/outputs/phase-3/shapefiles/shapes_cropped.shp')
island = 'saojorge'
shps = shps[shps['island']==island]

bounds = str(shps.total_bounds).replace('  ', ' ').replace(' ', ', ')
print(bounds)