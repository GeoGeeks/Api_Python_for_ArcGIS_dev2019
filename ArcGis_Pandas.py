# -*- coding: utf-8 -*-
"""
ArcGis for python 
"""
from arcgis import GIS
import pandas as pd
from arcgis.features import SpatialDataFrame
import matplotlib as plt
import numpy as np

#conectar a cuenta arcgis online (No es obligatorio)
gis=GIS("https://www.arcgis.com","dparra_geek","Esrico123*")


# Importa contenido de arcgis online con el id
item = GIS().content.get("5479b54bd1544e3a9553f40f219da67b")

#Toma la primera capa del contenido
flayer = item.layers[0]
#Convierte los datos a un dataFrame de pandas
sdf = pd.DataFrame.spatial.from_layer(flayer)
#Visualiza la cabeza del dataframe
sdf.head()


#Filtra por localidad y total
sdf3=pd.DataFrame(sdf.groupby(['LOCALIDAD','TOTAL']).agg(['count']))
#
sdf3=sdf.sum(axis = 3, skipna = True)
 
#Agrupar hurtos por localidad 
sdf3=pd.DataFrame(sdf.groupby(['LOCALIDAD'])['TOTAL'].sum())
#Grafica de barras para cantidad de hurtos por localidad
sdf3['TOTAL'].plot(kind='bar')

#Agrupa por tipo de hurtos
sdf4=pd.DataFrame(sdf.groupby(['FECHA_HECHO'])['TOTAL'].sum())
#Grafica de barras por tipo de hurto
sdf4['TOTAL'].plot(kind='line')

##


from bokeh.plotting import figure, output_file, show
# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

y=np.random.randint(10, size=10)
x=np.random.randint(15, size=10)


output_file("lines.html")


# add a line renderer with legend and line thickness
p.line(y, x, legend="Temp.", line_width=2)

# show the results
show(p)






