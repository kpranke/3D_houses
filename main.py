import pandas as pd
import numpy as np
import rasterio
import requests
#import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import shapefile
import fiona
from rasterio.mask import mask
import plotly.graph_objects as go

# Input a valid address in Flanders:
#address = input('Provide a valid address in Flanders: ')

address = 'Epicealaan 28, 2910 Essen'
print(f'Searching info for: {address}')
# Get a polygoon based on address in Flanders:

def get_coordinates(address: str):
    req = requests.get(f"https://loc.geopunt.be/v4/Location?q={address}").json()
    info = {'address' : address, 
                'x_value' : req['LocationResult'][0]['Location']['X_Lambert72'],
                'y_value' : req['LocationResult'][0]['Location']['Y_Lambert72'],
                'street' : req['LocationResult'][0]['Thoroughfarename'],
                'house_number' : req['LocationResult'][0]['Housenumber'], 
                'postcode': req['LocationResult'][0]['Zipcode'], 
                'municipality' : req['LocationResult'][0]['Municipality']}
    
    detail = requests.get("https://api.basisregisters.vlaanderen.be/v1/adresmatch", 
                          params={"postcode": info['postcode'], 
                                  "straatnaam": info['street'],
                                  "huisnummer": info['house_number']}).json()
    building = requests.get(detail['adresMatches'][0]['adresseerbareObjecten'][0]['detail']).json()
    build = requests.get(building['gebouw']['detail']).json()
    info['polygon'] = [build['geometriePolygoon']['polygon']]
    return info['polygon'][0]['coordinates'][0] 

print(f'Retrieved coordinates for: {address}')
 # Store polygon in a variable:

polygon = get_coordinates(address)

x_polygon = [i[0] for i in polygon]   
y_polygon = [i[1] for i in polygon]

print('Created a polygon of the building')
# Calculate bounds of a rectangle that contains the polygon:

left = min(x_polygon)
right = max(x_polygon)
top = max(y_polygon)
bottom = min(y_polygon)

print('Calculated the bounds of the building')
# Create a rectangle which contains the polygoon (left,bottom, right, top):

polygon_bounds = [[left,bottom, right, top]]

# Find to which file belong polygon_bounds - loop over the the DTM_bounds.csv:

df = pd.read_csv('DTM_bounds.csv')

for index, row in df.iterrows():
    if left >= row.left and right <= row.right and top <= row.top and bottom >= row.bottom:
        right_dtm_url = row.url_dtm
        right_dsm_url = row.url_dsm

print('Found the correct DTM and DSM files')

# Convert polygon to a Shapely format:

polygon_shapely = Polygon(polygon)

# Save a polygon to a .shp file:

w = shapefile.Writer('polygon')
w.field('name', 'C')

w.poly([polygon])
w.record('polygon1')

w.close()

polygon_path = 'polygon.shp'

# Clip DSM and DTM files with rasterio:

def clip_geotiff(file):
    with fiona.open("C:/Users/kasia/pyproj/3D_houses/shapefiles/polygon.shp", "r") as shapefile:
        shapes = [feature["geometry"] for feature in shapefile]

    with rasterio.open(file) as src:
        return rasterio.mask.mask(src, shapes, crop=True)


dsm_clip = clip_geotiff(right_dsm_url)
print('Clipped the DSM file')
dtm_clip = clip_geotiff(right_dtm_url)
print('Clipped the DTM file')

#Calculate Canopy Height Model: 

chm = dsm_clip[0][0] - dtm_clip[0][0]

print('Calculated the Canopy Height Model')

# Plot the 3D house with Plotly:

z = chm
x, y = np.arange(chm.shape[1]),np.arange(chm.shape[0])
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title= f'3D House Model: {address}', autosize=False)
fig.show()

print('The 3D house model is ready')