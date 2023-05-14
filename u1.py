import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd

# Create pandas dataframes with location coordinates and categories
dff=pd.read_excel('final_zom_swiggy.xlsx')
locations1=dff[dff['Presence']=='zomato'][['name','latitude','longitude']]

locations2 = dff[dff['Presence']=='Not in zomato']

# Create a folium map object
m = folium.Map( location=[30.7514,76.7731],zoom_start=13)

# Add markers for each location in the dataframes
for i, row in locations1.iterrows():
    folium.Marker(location=[row['latitude'], row['longitude']],
                  tooltip=row['name'],
                  icon=folium.Icon(color='red')).add_to(m)
    
map_container = st.container()
with map_container:
    # Add a title to the container
    st.write('# Zomato vs Not in zomato')
    # Render the map in a custom-sized container
    folium_static(m, width=500, height=300)


df=locations2

df.insert(1,'rating_cat','ii')
la = list(df['rating'])
las = list(df['rating_cat'])




for i in range(len(la)):
    if(la[i]==' -- '):
        las[i]='No Ratings'
    elif(la[i]==' NEW '):
        las[i]='Newly added restaurants'
    elif(la[i]>=4):
         las[i]='4-5 rating'
    elif(la[i]<3):
        las[i]='Less than 3'
    else:
        las[i]='3-4 rating'

        
df['rating_cat'] = las

st.subheader('Filtering Restaurants based on Rating')        
sb = st.radio('**Select the rating**',('Select the Rating','Newly added restaurants','No Ratings','4-5 rating','3-4 rating','Less than 3'))
if(sb=='Select The Rating'):
    pass
if(sb=='Newly added restaurants'):
    df_4_5=df[df['rating_cat']==sb][['name','latitude', 'longitude','fssai','rating','address']]
    df['fssai']=df['fssai'].astype('int64')
    st.dataframe(df_4_5[['name','fssai']])
    st.write('Number of Restaurants:',len(df_4_5))
    df45=df_4_5[['name','fssai','rating','address']]
    m = folium.Map( location=[30.7514,76.7731],zoom_start=12,)

    # Add markers for each location in the dataframes
    for i, row in df_4_5.iterrows():
        folium.Marker(location=[row['latitude'], row['longitude']],
                      tooltip=row['name'],
                      icon=folium.Icon(color='orange')).add_to(m)
    map_container = st.container()
    with map_container:
        folium_static(m, width=500, height=300)
      
    st.subheader('Download the above data')
    rad=st.radio('**Export Forecasted Production**',['.csv','.xlsx'])
    if(st.button('Submit')):
        if rad=='.csv':
            df45.to_csv(str(sb)+'_restaurant_data.csv',index=False)
        if rad=='.xlsx':
            df45.to_excel(str(sb)+'_restaurant_data.xlsx',index=False)
            
if(sb=='No Ratings'):
    df_4_5=df[df['rating_cat']==sb][['name','latitude', 'longitude','fssai','rating','address']]
    df['fssai']=df['fssai'].astype('int64')
    st.dataframe(df_4_5[['name','fssai']])
    st.write('Number of Restaurants:',len(df_4_5))
    df45=df_4_5[['name','fssai','rating','address']]
    m = folium.Map( location=[30.7514,76.7731],zoom_start=12,)

    # Add markers for each location in the dataframes
    for i, row in df_4_5.iterrows():
        folium.Marker(location=[row['latitude'], row['longitude']],
                      tooltip=row['name'],
                      icon=folium.Icon(color='orange')).add_to(m)
    map_container = st.container()
    with map_container:
        folium_static(m, width=500, height=300)
      
    st.subheader('Download the above data')
    rad=st.radio('**Export Forecasted Production**',['.csv','.xlsx'])
    if(st.button('Submit')):
        if rad=='.csv':
            df45.to_csv(str(sb)+'_restaurant_data.csv',index=False)
        if rad=='.xlsx':
            df45.to_excel(str(sb)+'_restaurant_data.xlsx',index=False)
    
if(sb=='4-5 rating'):
    df_4_5=df[df['rating_cat']==sb][['name','latitude', 'longitude','fssai','rating','address']]
    st.dataframe(df_4_5[['name','fssai']])
    st.write('Number of Restaurants:',len(df_4_5))
    df45=df_4_5[['name','fssai','rating','address']]
    m = folium.Map( location=[30.7514,76.7731],zoom_start=12,)

    # Add markers for each location in the dataframes
    for i, row in df_4_5.iterrows():
        folium.Marker(location=[row['latitude'], row['longitude']],
                      tooltip=row['name'],
                      icon=folium.Icon(color='orange')).add_to(m)
    map_container = st.container()
    with map_container:
        folium_static(m, width=500, height=300)
      
    st.subheader('Download the above data')
    rad=st.radio('**Export Forecasted Production**',['.csv','.xlsx'])
    if(st.button('Submit')):
        if rad=='.csv':
            df45.to_csv(str(sb)+'_restaurant_data.csv',index=False)
        if rad=='.xlsx':
            df45.to_excel(str(sb)+'_restaurant_data.xlsx',index=False)
            
if(sb=='3-4 rating'):
    df_3_4=df[df['Rating_Cat']==sb][['name','latitude', 'longitude','fssai','rating','address']]
    st.dataframe(df_3_4[['name','fssai']])
    st.write('Number of Restaurants:',len(df_3_4))
    df34=df_3_4[['name','fssai','rating','address']]
    
    m = folium.Map( location=[30.7514,76.7731],zoom_start=12,)
    
    for i, row in df_3_4.iterrows():
        folium.Marker(location=[row['latitude'], row['longitude']],
                      tooltip=row['name'],
                      icon=folium.Icon(color='orange')).add_to(m)
    map_container = st.container()
    with map_container:
        folium_static(m, width=500, height=300)
        
    st.subheader('Download the above data')
    rad=st.radio('**Export Forecasted Production**',['.csv','.xlsx'])
    if(st.button('Submit')):
        if rad=='.csv':
            df34.to_csv(str(sb)+'_restaurant_data.csv',index=False)
        if rad=='.xlsx':
            df34.to_excel(str(sb)+'_restaurant_data.xlsx',index=False)
    
if(sb=='Less than 3'):
    df_less3=df[df['Rating_Cat']==sb][['name','latitude', 'longitude','fssai','rating','address']]
    st.dataframe(df_less3[['name','fssai']])
    st.write('Number of Restaurants:',len(df_less3))
    dfless3=df_less3[['name','fssai','rating','address']]
    #dfless3=dfless3.reset_index(drop=True)
    m = folium.Map( location=[30.7514,76.7731],zoom_start=12,)
    
    for i, row in df_less3.iterrows():
        folium.Marker(location=[row['latitude'], row['longitude']],
                      tooltip=row['name'],
                      icon=folium.Icon(color='orange')).add_to(m)
    map_container = st.container()
    with map_container:
        folium_static(m, width=500, height=300)
        
        
    st.subheader('Download the above data')
    rad=st.radio('**Export Forecasted Production**',['.csv','.xlsx'])
    if(st.button('Submit')):
        if rad=='.csv':
            dfless3.to_csv(str(sb)+'_restaurant_data.csv',index=False)
        if rad=='.xlsx':
            dfless3.to_excel(str(sb)+'_restaurant_data.xlsx',index=False)
    




































