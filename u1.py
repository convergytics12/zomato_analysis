import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd
import xlsxwriter

zom = pd.read_excel('zomato and swiggy dataset.xlsx',sheet_name='zomato')
swig = pd.read_excel('zomato and swiggy dataset.xlsx',sheet_name='Swiggy')

# Create pandas dataframes with location coordinates and categories
dff=pd.read_excel('final_zom_swiggy.xlsx')
locations1=dff[dff['Presence']=='zomato'][['name','latitude','longitude']]

dfnz=pd.read_excel('Not_In_Zomato_Res_List.xlsx')
locations2 = dfnz
st.header('Zomato vs Swiggy Restaurant Base')
sb2 = st.radio('**Select the location**',['Chandigarh'])
if(sb2=='Chandigarh'):
    pass


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


st.subheader('Total Restaurants:')
sb1 = st.radio('',('Select the option','Zomato','Swiggy','Not in Zomato'))
if(sb1=='Select The option'):
    pass

if(sb1=='Zomato'):
    df_4_5=zom[['name','latitude', 'longitude','fssai','rating','address']].reset_index(drop=True)
    df_4_5['fssai']=df_4_5['fssai'].astype('str')
    for i in range(len(df_4_5)):
        df_4_5['fssai'][i]=df_4_5['fssai'][i].rstrip('.0')
    st.dataframe(df_4_5[['name','fssai','latitude','longitude']])
    st.write('Number of Restaurants:',len(df_4_5))
    df45=df_4_5[['name','fssai','rating','address']]
    m = folium.Map( location=[30.7514,76.7731],zoom_start=12,)

    # Add markers for each location in the dataframes
    for i, row in df_4_5.iterrows():
        folium.Marker(location=[row['latitude'], row['longitude']],
                      tooltip=row['name'],
                      icon=folium.Icon(color='red')).add_to(m)
    map_container = st.container()
    with map_container:
        folium_static(m, width=500, height=300)
        
    exl_button = st.button('Download as Excel',key='k1')
    if exl_button:
        writer = pd.ExcelWriter('data.xlsx', engine='openpyxl')
        df45.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()
        with open('data.xlsx', 'rb') as f:
            excel_data = f.read()
            st.download_button(label='Click here to download', data=excel_data, file_name='data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
       
if(sb1=='Swiggy'):
    df_4_5=swig[['name','latitude', 'longitude','fssai','rating','address']].reset_index(drop=True)
    df_4_5['fssai']=df_4_5['fssai'].astype('str')
    for i in range(len(df_4_5)):
        df_4_5['fssai'][i]=df_4_5['fssai'][i].rstrip('.0')
    st.dataframe(df_4_5[['name','fssai','latitude','longitude']])
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
      

        
    exl_button = st.button('Download as Excel',key='k2')
    if exl_button:
        writer = pd.ExcelWriter('data.xlsx', engine='openpyxl')
        df45.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()
        with open('data.xlsx', 'rb') as f:
            excel_data = f.read()
            st.download_button(label='Click here to download', data=excel_data, file_name='data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')            
if(sb1=='Not in Zomato'):
    df_4_5=locations2[['name','latitude', 'longitude','fssai','rating','address']].reset_index(drop=True)
    df_4_5['fssai']=df_4_5['fssai'].astype('str')
    for i in range(len(df_4_5)):
        df_4_5['fssai'][i]=df_4_5['fssai'][i].rstrip('.0')
    st.dataframe(df_4_5[['name','fssai','latitude','longitude']])
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
      

        
    exl_button = st.button('Download as Excel',key='k3')
    if exl_button:
        writer = pd.ExcelWriter('data.xlsx', engine='openpyxl')
        df45.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()
        with open('data.xlsx', 'rb') as f:
            excel_data = f.read()
            st.download_button(label='Click here to download', data=excel_data, file_name='data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')





st.subheader('Filtering Restaurants not in zomato based on Rating')        
sb = st.radio('',('Select the Rating','Newly added restaurants','No Ratings','4-5 rating','3-4 rating','Less than 3'))
if(sb=='Select The Rating'):
    pass
    
if(sb=='Newly added restaurants'):
    df_4_5=df[df['rating_cat']==sb][['name','latitude', 'longitude','fssai','rating','address']].reset_index(drop=True)
    df_4_5['fssai']=df_4_5['fssai'].astype('str')
    for i in range(len(df_4_5)):
        df_4_5['fssai'][i]=df_4_5['fssai'][i].rstrip('.0')
    st.dataframe(df_4_5[['name','fssai','latitude','longitude']])
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
      

        
    excel_button = st.button('Download as Excel',key='k4')
    if excel_button:
        writer = pd.ExcelWriter('data.xlsx', engine='openpyxl')
        df45.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()
        with open('data.xlsx', 'rb') as f:
            excel_data = f.read()
            st.download_button(label='Click here to download', data=excel_data, file_name='data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

            
if(sb=='No Ratings'):
    df_4_5=df[df['rating_cat']==sb][['name','latitude', 'longitude','fssai','rating','address']].reset_index(drop=True)
    df_4_5['fssai']=df_4_5['fssai'].astype('str')
    for i in range(len(df_4_5)):
        df_4_5['fssai'][i]=df_4_5['fssai'][i].rstrip('.0')
    st.dataframe(df_4_5[['name','fssai','latitude','longitude']])
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
      

        
    excel_button = st.button('Download as Excel',key='k5')
    if excel_button:
        writer = pd.ExcelWriter('data.xlsx', engine='openpyxl')
        df45.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()
        with open('data.xlsx', 'rb') as f:
            excel_data = f.read()
            st.download_button(label='Click here to download', data=excel_data, file_name='data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

            
    
    
if(sb=='4-5 rating'):
    df_4_5=df[df['rating_cat']==sb][['name','latitude', 'longitude','fssai','rating','address']].reset_index(drop=True)
    df_4_5['fssai']=df_4_5['fssai'].astype('str')
    for i in range(len(df_4_5)):
        df_4_5['fssai'][i]=df_4_5['fssai'][i].rstrip('.0')
    st.dataframe(df_4_5[['name','fssai','latitude','longitude']])
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
    
            

        
    excel_button = st.button('Download as Excel',key='k6')
    if excel_button:
        writer = pd.ExcelWriter('data.xlsx', engine='openpyxl')
        df45.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()
        with open('data.xlsx', 'rb') as f:
            excel_data = f.read()
            st.download_button(label='Click here to download', data=excel_data, file_name='data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

            
if(sb=='3-4 rating'):
    df_3_4=df[df['rating_cat']==sb][['name','latitude', 'longitude','fssai','rating','address']].reset_index(drop=True)
    df_3_4['fssai']=df_3_4['fssai'].astype('str')
    for i in range(len(df_3_4)):
        df_3_4['fssai'][i]=df_3_4['fssai'][i].rstrip('.0')
    st.dataframe(df_3_4[['name','fssai','latitude','longitude']])
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
    
            

        
    excel_button = st.button('Download as Excel',key='k7')
    if excel_button:
        writer = pd.ExcelWriter('data.xlsx', engine='openpyxl')
        df34.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()
        with open('data.xlsx', 'rb') as f:
            excel_data = f.read()
            st.download_button(label='Click here to download', data=excel_data, file_name='data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    
if(sb=='Less than 3'):
    df_less3=df[df['rating_cat']==sb][['name','latitude', 'longitude','fssai','rating','address']].reset_index(drop=True)
    df_less3['fssai']=df_less3['fssai'].astype('str')
    for i in range(len(df_less3)):
        df_less3['fssai'][i]=df_less3['fssai'][i].rstrip('.0')
    st.dataframe(df_less3[['name','fssai','latitude','longitude']])
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
        
        


        
    excel_button = st.button('Download as Excel',key='k8')
    if excel_button:
        writer = pd.ExcelWriter('data.xlsx', engine='openpyxl')
        dfless3.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()
        with open('data.xlsx', 'rb') as f:
            excel_data = f.read()
            st.download_button(label='Click here to download', data=excel_data, file_name='data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')



    




































