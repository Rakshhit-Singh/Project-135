import pandas as pd
import plotly.express as px

df  = pd.read_csv("habitable.csv")
star_name_list = df["Star Name"]
mass_list = df["Mass"]
radius_list = df["Radius"]
distance_list = df["Distance"]
gravity_list = df["Gravity"]

fig1 = px.bar(x=star_name_list, y=radius_list) 
fig1.show()
fig2 = px.bar(x=star_name_list, y=mass_list) 
fig2.show()
fig3 = px.bar(x=star_name_list, y=distance_list) 
fig3.show()
fig4 = px.bar(x=star_name_list, y=gravity_list) 
fig4.show()
