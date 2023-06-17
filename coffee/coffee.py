import pandas as pd
import geopandas as gpd
import folium
import webbrowser


df = pd.read_csv('Shops.csv', encoding='utf-8')

gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.X, df.Y), crs="EPSG:4326"
)

gdf.to_file("shops.geojson", driver='GeoJSON')

"""
m = gdf.explore(
    popup=True,  # show all values in popup (on click)
    tiles="CartoDB voyager",  # use "CartoDB positron" tiles
    marker_type="marker"
)

bgy = folium.features.GeoJson('barangay.geojson')
bgy.add_to(m)

folium.LayerControl().add_to(m)  
m.save("map.html")
webbrowser.open("map.html")
"""