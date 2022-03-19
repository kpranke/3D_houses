# Import libraries:
import rasterio
import pandas as pd

# Create a list ranging from 01 to 43:
list_43 = list(range(1,44))
updated_list = []
for i in list_43:
    i = str(i)
    i = i.zfill(2)
    updated_list.append(i)

# Create a list of dictionaries with the following info: DTM file URL, DSM file URL, bounds - left, bounds - right, bounds - top, bounds - bottom:
DTM_bounds = []

for i in updated_list:
    url_dtm = f'zip+https://downloadagiv.blob.core.windows.net/dhm-vlaanderen-ii-dtm-raster-1m/DHMVIIDTMRAS1m_k{i}.zip!/GeoTIFF/DHMVIIDTMRAS1m_k{i}.tif'
    url_dsm = f'zip+https://downloadagiv.blob.core.windows.net/dhm-vlaanderen-ii-dsm-raster-1m/DHMVIIDSMRAS1m_k{i}.zip!/GeoTIFF/DHMVIIDSMRAS1m_k{i}.tif'
    print(f"Accesssing {i}")
    
    DTM_file = rasterio.open(url_dtm)
    print(f"Opened DTM file {i}")
       
    DTM_bounds.append({
        'url_dtm': url_dtm,
        'url_dsm' : url_dsm,
        'left' : DTM_file.bounds.left,
        'right' : DTM_file.bounds.right,
        'top' : DTM_file.bounds.top,
        'bottom' : DTM_file.bounds.bottom
    })
    print(f"Added bounds of DTM file {i}")

#Create a data frame from dictionary:
DTM_bounds_df = pd.DataFrame.from_dict(DTM_bounds)

# Save the data frame as .csv: 
DTM_bounds_df.to_csv('DTM_bounds.csv', encoding='utf-8', index=False)    
