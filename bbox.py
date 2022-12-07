# prints bounding box of shapes to be rasterized
import geopandas as gpd

shps_file = '/Users/petermenzies/SeaSketch/azores/azo-ous/outputs/flores-corvo-santamaria/shapefiles/shapes_cropped.shp'
shps = gpd.read_file(shps_file)
island = 'santa maria'
shps = shps[shps['island']==island]
shps = shps.buffer(0.01)

bounds = [x for x in shps.total_bounds]
bounds = [round(x,2) for x in bounds]

print(bounds)