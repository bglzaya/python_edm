import plotly.graph_objects as go
import pandas as pd
import numpy as np
import geopandas as gpd
import plotly.express as px
import json

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


geodf = gpd.read_file("data/map/Adminstrative_shape_file/Sum.shp")
geodf = geodf.to_crs("WGS84").set_index("AS_code")
print(geodf.columns)


df_mine = pd.read_stata("data/viz/mineral_lic.dta")
print(df_mine.columns)

df_bio = pd.read_excel("data/viz/biomass_long.xlsx")
df_bio['biomass'] = df_bio['biomass'].fillna(0)
df_bio['biomass'] = df_bio['biomass'].astype('float16')
df_bio['AS_code'] = df_bio['aimagcode']*100+df_bio['soumcode']
print(df_bio.columns)

# fig = px.choropleth_mapbox(df_bio,
#                            geojson=geodf.geometry,
#                            locations='AS_code',
#                            center={"lat": 47.20900020640241, "lon": 102.8187267977119},
#                            color='biomass', mapbox_style="carto-positron",
#                            color_continuous_scale="greens", color_discrete_sequence=["fuchsia"],
#                            zoom=5.2, animation_frame="year")
#
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, transition = {'duration': 5000})
# fig.show()


df_mine = df_mine.sort_values(by='year')
print(df_mine["year"])
df_mine = df_mine.loc[(df_mine["year"]>=2007) & (df_mine["year"]<=2020)].reset_index(drop=True)


fig = px.choropleth_mapbox(df_mine,
                           geojson=geodf.geometry,
                           locations='AS_code',
                           center={"lat": 47.20900020640241, "lon": 102.8187267977119},
                           color='AREA_M2', mapbox_style="open-street-map",
                           color_continuous_scale="brwnyl", color_discrete_sequence=["fuchsia"],
                           zoom=5.2, animation_frame="year")

fig2 = px.scatter_geo(df_bio, lat="latitude", lon="longitude",
                      size="biomass",
                      hover_name="plotname_mng",
                      color_continuous_scale="Cividis",
                      animation_frame='year',
                      opacity = 0.8,
                      labels={'soumname_mng':'Soum name'},
                      color="biomass"
                    )

fig.add_trace(fig2.data[0])
for i, frame in enumerate(fig.frames):
    fig.frames[i].data += (fig2.frames[i].data[0],)
fig.show()

# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, transition = {'duration': 1000})
# fig.show()






