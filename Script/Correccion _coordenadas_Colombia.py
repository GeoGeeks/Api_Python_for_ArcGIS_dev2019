#B  -  M   - C  -  R
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
def limpiarCoord(df,columnax):
    lonlat=(df
               .apply(lambda row: row[columnax],axis=1)
               .apply(lambda word: word.replace('POINT (',''))
               .apply(lambda body: list(body))
               .apply(lambda letters: list(map(lambda letter:letter.replace(")",''),letters)))
               .apply(lambda letters: ''.join(letters))
                  )            
    df['lat long']=lonlat
    latlon_df = df['lat long'].apply(lambda x: pd.Series(x.split(' ')))
    df['latt']=latlon_df[0]
    df['lonn']=latlon_df[1]
    df=df.dropna(axis=0, subset=['latt'])
    df=df.dropna(axis=0, subset=['lonn'])
    return df
def correccion(entrada,latitud,longitud,salida):
    df = pd.read_csv(entrada,dtype={latitud:'str',longitud:'str'}) # Lee los campos como texto para manipularlos
    df=df.dropna(axis=0, subset=[latitud])#borra las filas vacias
    df=df.dropna(axis=0, subset=[longitud])
    #correccion longitud en la tercera posicion pone una coma teniendo en cuenta el menos 
    long=df[longitud]
    df['long']=0
    for i in range(len(df)):
         df['long'].iloc[i]=(long.iloc[i])[0:3]+'.'+(long.iloc[i])[3:]
    #Corrección latitud teniendo en cuenta cual es el primer digito
    lat=df[latitud]
    df['lat']=0
    for i in range(len(df)):
        if (lat.iloc[i])[0]=='1':
            df['lat'].iloc[i]=(lat.iloc[i])[0:2]+'.'+(lat.iloc[i])[2:]
        elif (lat.iloc[i])[0]=='-':
            df['lat'].iloc[i]=(lat.iloc[i])[1:2]+'.'+(lat.iloc[i])[2:]
        elif (lat.iloc[i])[0]=='0':
            df['lat'].iloc[i]=(lat.iloc[i])[0:1]+'.'+(lat.iloc[i])[2:]
        else:
            df['lat'].iloc[i]=(lat.iloc[i])[0:1]+'.'+(lat.iloc[i])[1:]        
    df[['long','lat']] = df[['long','lat']].apply(pd.to_numeric)
    df= df.drop(columns=[latitud, longitud], axis=1)
    df.to_csv(salida, sep=',', encoding='utf-8')
if __name__=='__main__':
    entrada0= input('Ingrese el nombre del archivo sin la extension:  ')
    entrada=entrada0+'.csv'
    latitud= input('Ingrese el nombre de la columna de latitud:  ')
    longitud= input('Ingrese el nombre de la columna de longitud:  ')
    salida0= input('Ingrese el nombre del archivo de salida sin la extension:  ')
    salida=salida0+'.csv'
    correccion(entrada,latitud,longitud,salida)