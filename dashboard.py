import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import folium
# from folium.plugins import HeatMap
from wordcloud import WordCloud 

def create_cust_state_sp (df):
    cust_state_sp = df['customer_city'].value_counts()
    return cust_state_sp

with st.sidebar:
    st.header("Dashboard")
    st.image('assets/pp.png')
    st.write('Zulfi Fadilah Azhar')
    st.write('zulfi.fazhar12@gmail.com')

cust_city_sp = pd.read_csv('assets/cust_city_sp.csv')
state_count = pd.read_csv('assets/state_count.csv')
top5_cust_city = pd.read_csv('assets/top5_cust_city_sp.csv')

cust_city = create_cust_state_sp(cust_city_sp)

st.header('E-Commerce Public Dataset Visualization 📊')

st.subheader('Data Overview')
fig, ax = plt.subplots(figsize=(12, 8))
sns.barplot(x='count', y='state', data=state_count, palette='viridis', hue='state', legend=False)
ax.set_xlabel('Jumlah Transaksi')
ax.set_ylabel('State')
ax.set_title('Aktivitas transaksi di Berbagai States')
st.pyplot(fig)

st.subheader('Peta Sebaran Transaksi di State of São Paulo')

tab1, tab2 = st.tabs(["Map São Paulo", "Heatmap São Paulo"])

with tab1 :
    map_center = [-23.5600152049106, -46.639313644184575]
    m = folium.Map(location=map_center, zoom_start=8)
    html_map = m.get_root().render()
    st.components.v1.html(html_map, height=600, width=800, scrolling=True)

with tab2 :
    # map_center = [-23.5600152049106, -46.639313644184575]
    # m = folium.Map(location=map_center, zoom_start=8)
    # HeatMap(data_heatmap).add_to(m)
    # html_map = m.get_root().render()
    # st.components.v1.html(html_map, height=600, width=800, scrolling=True)
    st.write("Note : asumsi saya streamlit cloud terjadi error karena terlalu berat menampilkan heatmap. Jadi, saya melampirkan hasil screnshot heatmap yang sudah saya visualisasikan sebelumnya.")
    st.image("assets/SP-Heatmap.jpeg")

st.subheader('Wordcloud kota-kota dari State of São Paulo')
customer_wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(cust_city)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(customer_wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

st.subheader('Distribusi Transaksi di 5 Kota Teratas dari State of São Paulo')
plt.figure(figsize=(8, 8))
colors = ['#21a585', '#3cc29b', '#57dfb1', '#72fccc', '#8dffdd']
plt.title('Distribusi Transaksi di 5 Kota Teratas dari State of São Paulo')
plt.pie(
    top5_cust_city['count'],
    labels=top5_cust_city['customer_city'],
    autopct='%1.1f%%',
    explode=(0.1, 0, 0, 0, 0),
    shadow=True,
    colors=colors,
    startangle=90
)
st.pyplot(plt.gcf())

st.caption('Copyright (c) Zulfi Fadilah Azhar 2023')