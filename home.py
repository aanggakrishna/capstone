import streamlit as st
import pandas as pd
import altair as alt
import matplotlib
matplotlib.use('Agg')
import numpy as np

import matplotlib.pyplot as plt
from scipy import stats
from PIL import Image

#content-start
st.set_page_config(layout="wide")
st.title('Daya Saing Export Udang Beku Indonesia dengan Negara Lain')
st.write('_Product: 030617 Frozen shrimps and prawns_')
st.write('oleh : **I Putu A. Angga Krishna**')
st.write('Seafood adalah makanan yang tinggi protein dan mudah untuk didapatkan di Indonesia karena wilayah perairan indonesia lebih luas ketimbang daratannya. Selain di Indonesia, hampir sebagian besar negara memiliki olehan seafood tersendiri. Salah satu bahan makanan yang hampir selalu ada saat membeli olahan seafood adalah **udang**.')
image = Image.open('udang.JPG')

st.image(image, caption='makanan berbahan udang')
st.write('Selain memproduksi sendiri, untuk memenuhi kebutuan pasar di setiap negara, sebagian besar negara juga tergantung dari ekspor negara lain')
st.write('berikut ini adalah daftar **5** Negara **pengekspor udang beku** (_Product: 030617 Frozen shrimps and prawns_) terbesar didunia')
data = pd.read_csv('5exportall.csv')
data = data.set_index('country').stack().reset_index()
data.columns=['country', 'year', 'total']
data_all = data
data_indonesia = data_all.loc[data_all['country'] == 'Indonesia']
data_indonesia = data_indonesia.set_index('country')
tahun =list(set(data['year']))






     
udang_indonesia_ke_all = pd.read_csv('indonesia_export_udang_ke_all.csv')
udang_indonesia_ke_all_world = udang_indonesia_ke_all.iloc[0:1 , :]
udang_indonesia_ke_all = udang_indonesia_ke_all.iloc[1: , :]
#udang_indonesia_ke_all = udang_indonesia_ke_all.head(5)
#st.write(udang_indonesia_ke_all)
#st.write(udang_indonesia_ke_all_world.head(5))
data_5_all = udang_indonesia_ke_all.set_index('country').stack().reset_index()
data_5_all.columns=['country', 'year', 'total']

# sidebar-start
with st.sidebar:
    st.title('Tahun dari 2017-2021')
    
    # option_tahun = st.selectbox(
    #     'Tahun ?',
    #     tahun)

    # st.write('Select:', option_tahun)
    start_tahun, end_tahun = st.select_slider(
     'Select a range of color wavelength',options=['2017', '2018', '2019', '2020', '2021']
     ,
     value=('2017', '2021'))
    st.write('Kamu Memilih tahun', start_tahun, 'dan', end_tahun)
    
    option = st.selectbox(
        'Negara Diluar 5 Besar?',
        data_5_all['country'].unique())

    st.write('Select:', option)
# sidebar-end
data_5_all = data_5_all.loc[(data_5_all['year']<=end_tahun) & (data_5_all['year']>=start_tahun)]

with st.container():
    st.title('TOP 5 Negara Export Udang Beku')
    st.write('_nilai per ribu USD_')
    jumlah = (int(end_tahun)-int(start_tahun)+1)*5
    data_top_all = data.loc[(data['year']<=end_tahun) & (data['year']>=start_tahun)]
    
    
    c = alt.Chart(data_top_all.head(jumlah)).mark_line().encode(
        x='year', y='total', color='country',tooltip=['year', 'total', 'country'])

    st.altair_chart(c, use_container_width=True)
    st.write('Untuk tahun **2021** saja dari grafik diatas dapat dilihat bahwa **India** berada pada tingkat pengekspor udang **terbesar** didunia yaitu **5,148,765 USD**,diikuti oleh **Equador, Vietnam, Indonesia (1,530,310.000 USD), dan Argentina**')
    st.markdown('')
    with st.expander("Lihat Data Tabel"):
        table = pd.pivot_table(data_top_all.head(jumlah), values='year', index=['country'],
                        columns=['year'])
        st.table(table)
        st.write("""
            Sumber https://trademap.org""")
   
with st.container():
    image = Image.open('berita.JPG')

    st.image(image, caption='berita export udang')
    st.title('Hasil Ekspor Indonesia per tahun')
    st.write('_2017-2021_')
    st.write('_per ribu USD_')
    data_indonesia_ori = data_indonesia
    data_indonesia = data_indonesia.loc[(data_indonesia['year']<=end_tahun) & (data_indonesia['year']>=start_tahun)]

    col1, col2, col3,col4 = st.columns(4)
    with col1:
        nilai = data_indonesia_ori.loc[data_indonesia_ori['year'] == '2018']
        nilai_sebelumnya = data_indonesia_ori.loc[data_indonesia_ori['year'] == '2017']
        delta = (nilai['total']-nilai_sebelumnya['total'])/nilai['total']*100
        st.metric('2018',nilai['total'],'{} %'.format(round(delta.iloc[0],2)))

    with col2:
        nilai = data_indonesia_ori.loc[data_indonesia_ori['year'] == '2019']
        nilai_sebelumnya = data_indonesia_ori.loc[data_indonesia_ori['year'] == '2018']
        delta = (nilai['total']-nilai_sebelumnya['total'])/nilai['total']*100
        st.metric('2019',nilai['total'],'{} %'.format(round(delta.iloc[0],2)))

    with col3:
        nilai = data_indonesia_ori.loc[data_indonesia_ori['year'] == '2020']
        nilai_sebelumnya = data_indonesia_ori.loc[data_indonesia_ori['year'] == '2019']
        delta = (nilai['total']-nilai_sebelumnya['total'])/nilai['total']*100
        st.metric('2020',nilai['total'],'{} %'.format(round(delta.iloc[0],2)))

    with col4:
        nilai = data_indonesia_ori.loc[data_indonesia_ori['year'] == '2021']
        nilai_sebelumnya = data_indonesia_ori.loc[data_indonesia_ori['year'] == '2019']
        delta = (nilai['total']-nilai_sebelumnya['total'])/nilai['total']*100
        st.metric('2021',nilai['total'],'{} %'.format(round(delta.iloc[0],2)))
    bar_chart_indonesia = alt.Chart(data_indonesia).mark_line().encode(
        y='total:Q',
        x='year:O',
        tooltip=['year', 'total']
    )
    st.write('Untuk tahun **2017 - 2019** ekspor Indonesia untuk udang beku mengalami **penurunan** hingga **6%**. Tetapi setelahnya **2019-2021** terdapat **peningkatan** ekspor yang mencapai **17%** pada tahun **2021**')
    st.altair_chart(bar_chart_indonesia, use_container_width=True)
    st.write('melansir dari detik finance  **Penurunan** nilai ekspor udang pada tahun **2019** ini terjadi akibat **turunnya harga ekspor udang dari Indonesia**, yakni menjadi **USD 8,26/kg** pada kuartal I 2019 dari sebelumnya **USD 9,35/kg**. dikarenakan beberapa produsen utama dunia seperti **India, Argentina, dan Meksiko** pasokannya meningkat di pasar-pasar tersebut dengan harga yang relatif rendah.')
    with st.expander('sumber berita'):
        st.write("finance.detik.com/berita-ekonomi-bisnis/d-4592433/penjelasan-lengkap-kkp-soal-ekspor-produk-perikanan-turun")
    with st.expander("Lihat Data Tabel"):

        st.table(data_indonesia.sort_values('total',ascending=False))
        st.write("""
            Sumber trademap.org""")



    

with st.container():
    st.title('TOP 5 Negara Tujuan Export Udang Beku Indonesia')
    
    data_5_all = data_5_all.loc[(data_5_all['year']<=end_tahun) & (data_5_all['year']>=start_tahun)]
    data_5_all_negara = data_5_all.head(25)
    c = alt.Chart(data_5_all_negara).mark_bar(interpolate='basis').encode(
        x='country:O', y='total:Q', column='year:N', color='country:N',tooltip=['year', 'total', 'country'])

    st.altair_chart(c)
    st.write('Untuk pasar **China** dari tahun 2020 terjadi **penurunan** sampai tahun 2021. Hal ini dikarenakan **COVID 19** yang terjadi pada awalnya di Cina sehingga menyebabkan export ke negara Cina tidak dapat dilakukan')
    
    st.write('**United States of America** adalah negara dengan importir udang beku **terbanyak dari indonesia**. walaupun nilai dari tahun 2017-2019 terjadi penurunan, tetapi untuk tahun berikutnya terlah terjadi lonjakan ekspor yang meningkat bahkan melewati nilai ekspor 5 tahun terakhir. Sedangkan untuk pasar **Jepang** ekspor Indonesia terlihat **stabil** dengan naik turun yang tidak begitu banyak.')
    with st.expander('sumber berita:'):
        st.write('https://lokadata.id/artikel/ekspor-udang-masih-bisa-tumbuh-lebih-tinggi')
        st.write('Pendiri PT Dewi Laut Aquaculture Rizal Mallarangeng mengatakan, harga udang di pasar internasional bagus karena sejumlah negara, seperti Amerika Serikat, memang tidak terlalu ketat menerapkan pembatasan. **Walmart, misalnya, buka seperti biasa**. Pandemi seperti tak berpengaruh, katanya.')
    
    with st.expander("Lihat Data Tabel"):
        table = pd.pivot_table(data_5_all_negara, values='total', index=['country'],
                        columns=['year'])
        st.table(table)
        st.write("""
            Sumber trademap.org""")

with st.container():
    st.title('Pengaruh Daya Saing (RCA) terhadap Ekspor Udang Indonesia')
    st.write('_ke negara top 5 importir (Canada, China, Jepang, US, Taipe_)')
#persiapan RCA    
# st.table(data_5_all)
data_5_country= data_5_all['country'].unique()
#data indonesia export udang ke negara tujuan
data_5_all.columns=['country', 'year', 'total_menerima_export_udang_dari_indonesia']
#data indonesia export semua komuditas ke negara tujuan
export_total_indo_all = pd.read_csv('export_total_negara_indo_ke_all.csv')
export_total_indo_all_world = export_total_indo_all.iloc[0:1 , :]
export_total_indo_all = export_total_indo_all.iloc[1: , :]
#export_total_indo_all = export_total_indo_all.head(5)
export_total_indo_all=export_total_indo_all.set_index('country').stack().reset_index()
export_total_indo_all.columns=['country', 'year', 'total_menerima_export_all_produk']
export_total_indo_all = export_total_indo_all.loc[(export_total_indo_all['year']<=end_tahun) & (export_total_indo_all['year']>=start_tahun)]
#st.write(export_total_indo_all)
# st.write(data_5_country[0])
#st.write(data_5_all.loc[data_5_all['country']==data_5_country[0]])
# st.write(export_total_indo_all.loc[export_total_indo_all['country']==data_5_country[0]])



export_udang_dunia_all = pd.read_csv('export_udang_dunia_ke_all.csv')
export_udang_dunia_all_world = export_udang_dunia_all.iloc[0:1 , :]
export_udang_dunia_all = export_udang_dunia_all.iloc[1: , :]
export_udang_dunia_all = export_udang_dunia_all.set_index('country').stack().reset_index()
export_udang_dunia_all.columns=['country', 'year', 'export_udang_dunia']
export_udang_dunia_all = export_udang_dunia_all.loc[(export_udang_dunia_all['year']<=end_tahun) & (export_udang_dunia_all['year']>=start_tahun)]
# st.write(export_udang_dunia_all.loc[export_udang_dunia_all['country']==data_5_country[0]])



export_total_dunia_all = pd.read_csv('export_total_dunia_ke_all.csv')
export_total_dunia_all_world = export_total_dunia_all.iloc[0:1 , :]
export_total_dunia_all = export_total_dunia_all.iloc[1: , :]
export_total_dunia_all = export_total_dunia_all.set_index('country').stack().reset_index()
export_total_dunia_all.columns=['country', 'year', 'export_total_dunia']
export_total_dunia_all = export_total_dunia_all.loc[(export_total_dunia_all['year']<=end_tahun) & (export_total_dunia_all['year']>=start_tahun)]

# st.write(export_total_dunia_all.loc[export_total_dunia_all['country']==data_5_country[0]])
##gabungan data 1,2,3,4 mencari rca us
data1=data_5_all.loc[data_5_all['country']==data_5_country[0]]
data2 = export_total_indo_all.loc[export_total_indo_all['country']==data_5_country[0]]
data2 = data2['total_menerima_export_all_produk'].reset_index(drop=True)
data3 = export_udang_dunia_all.loc[export_udang_dunia_all['country']==data_5_country[0]]
data3 = data3['export_udang_dunia'].reset_index(drop=True)
data4 = export_total_dunia_all.loc[export_total_dunia_all['country']==data_5_country[0]]
data4 = data4['export_total_dunia'].reset_index(drop=True)
# gabungkan data 1,2,3,4
data_join = pd.concat([data1, data2,data3,data4], axis=1)
#st.write(data_join)
#mencari nilai rca
data_join['RCA1']=data_join['total_menerima_export_udang_dari_indonesia']/data_join['total_menerima_export_all_produk']
data_join['RCA2']=data_join['export_udang_dunia']/data_join['export_total_dunia']
data_join['RCA'] = data_join['RCA1']/data_join['RCA2']
data_join_1 = data_join[['country','year','RCA']]



#untuk jepang
data1=data_5_all.loc[data_5_all['country']==data_5_country[1]].reset_index(drop=True)
data2 = export_total_indo_all.loc[export_total_indo_all['country']==data_5_country[1]]
data2 = data2['total_menerima_export_all_produk'].reset_index(drop=True)
data3 = export_udang_dunia_all.loc[export_udang_dunia_all['country']==data_5_country[1]]
data3 = data3['export_udang_dunia'].reset_index(drop=True)
data4 = export_total_dunia_all.loc[export_total_dunia_all['country']==data_5_country[1]]
data4 = data4['export_total_dunia'].reset_index(drop=True)
# gabungkan data 1,2,3,4
data_join = pd.concat([data1, data2,data3,data4], axis=1)
#st.write(data_join)
#mencari nilai rca
data_join['RCA1']=data_join['total_menerima_export_udang_dari_indonesia']/data_join['total_menerima_export_all_produk']
data_join['RCA2']=data_join['export_udang_dunia']/data_join['export_total_dunia']
data_join['RCA'] = data_join['RCA1']/data_join['RCA2']
data_join_2 = data_join[['country','year','RCA']]


#untuk china
data1=data_5_all.loc[data_5_all['country']==data_5_country[2]].reset_index(drop=True)
data2 = export_total_indo_all.loc[export_total_indo_all['country']==data_5_country[2]]
data2 = data2['total_menerima_export_all_produk'].reset_index(drop=True)
data3 = export_udang_dunia_all.loc[export_udang_dunia_all['country']==data_5_country[2]]
data3 = data3['export_udang_dunia'].reset_index(drop=True)
data4 = export_total_dunia_all.loc[export_total_dunia_all['country']==data_5_country[2]]
data4 = data4['export_total_dunia'].reset_index(drop=True)
# gabungkan data 1,2,3,4
data_join = pd.concat([data1, data2,data3,data4], axis=1)
#st.write(data_join)
#mencari nilai rca
data_join['RCA1']=data_join['total_menerima_export_udang_dari_indonesia']/data_join['total_menerima_export_all_produk']
data_join['RCA2']=data_join['export_udang_dunia']/data_join['export_total_dunia']
data_join['RCA'] = data_join['RCA1']/data_join['RCA2']
data_join_3 = data_join[['country','year','RCA']]


#untuk kanada
data1=data_5_all.loc[data_5_all['country']==data_5_country[3]].reset_index(drop=True)
data2 = export_total_indo_all.loc[export_total_indo_all['country']==data_5_country[3]]
data2 = data2['total_menerima_export_all_produk'].reset_index(drop=True)
data3 = export_udang_dunia_all.loc[export_udang_dunia_all['country']==data_5_country[3]]
data3 = data3['export_udang_dunia'].reset_index(drop=True)
data4 = export_total_dunia_all.loc[export_total_dunia_all['country']==data_5_country[3]]
data4 = data4['export_total_dunia'].reset_index(drop=True)
# gabungkan data 1,2,3,4
data_join = pd.concat([data1, data2,data3,data4], axis=1)
#st.write(data_join)
#mencari nilai rca
data_join['RCA1']=data_join['total_menerima_export_udang_dari_indonesia']/data_join['total_menerima_export_all_produk']
data_join['RCA2']=data_join['export_udang_dunia']/data_join['export_total_dunia']
data_join['RCA'] = data_join['RCA1']/data_join['RCA2']
data_join_4 = data_join[['country','year','RCA']]


#untuk taipe
data1=data_5_all.loc[data_5_all['country']==data_5_country[4]].reset_index(drop=True)
data2 = export_total_indo_all.loc[export_total_indo_all['country']==data_5_country[4]]
data2 = data2['total_menerima_export_all_produk'].reset_index(drop=True)
data3 = export_udang_dunia_all.loc[export_udang_dunia_all['country']==data_5_country[4]]
data3 = data3['export_udang_dunia'].reset_index(drop=True)
data4 = export_total_dunia_all.loc[export_total_dunia_all['country']==data_5_country[4]]
data4 = data4['export_total_dunia'].reset_index(drop=True)
# gabungkan data 1,2,3,4
data_join = pd.concat([data1, data2,data3,data4], axis=1)
#st.write(data_join)
#mencari nilai rca
data_join['RCA1']=data_join['total_menerima_export_udang_dari_indonesia']/data_join['total_menerima_export_all_produk']
data_join['RCA2']=data_join['export_udang_dunia']/data_join['export_total_dunia']
data_join['RCA'] = data_join['RCA1']/data_join['RCA2']
data_join_5 = data_join[['country','year','RCA']]

#gabungan data 12345
data_join_top_5 = pd.concat([data_join_1,data_join_2,data_join_3,data_join_4,data_join_5],ignore_index = True)
c5 = alt.Chart(data_join_top_5).mark_line().encode(
        x='year', y='RCA', color='country',tooltip=['year', 'RCA', 'country'])

st.altair_chart(c5, use_container_width=True)
st.write('**Revealed Comparative Advantage (RCA) digunakan menentukan keunggulan daya saing.**')
st.write('_Jika nilai **RCA** > **1** maka berdaya saing **KUAT** sedangkan_')
st.write('_Jika nilai **RCA** < **1** maka berdaya saing **LEMAH**_')
st.write('Dalam data diatas daya saing **LEMAH** hanya terdapat pada **CHINA** di tahun **2021** yaitu sebesar **0.38** selainnya bernilai **KUAT** hal ini disebabkan karena export yang masuk ke negara tersebut **tidak bisa** dilakukan karena **COVID 19** yang baru melanda **China**')
st.write('Itu berarti daya saing Udang Beku **Indonesia dapat bersaing** dengan exportir dari **negara lain** tetapi untuk negara **China** masih **perlu adanya peningkatan** daya saing agar China kembali melakukan export ke Indonesia apalagi dengan COVID 19 yang sudah mebaik kedepannya')
with st.expander("Lihat Data Tabel"):
    st.write('sumber rumus : https://www.kemendag.go.id/addon/rca/')
    st.write(data_join_top_5.dropna(subset=['country', 'year']))








#data_join_top_5
# st.write(data_5_all.head(25))
data_top_5 = data_5_all.head(25)
data_top_5_rca = pd.concat([data_top_5,data_join_top_5['RCA'].reset_index(drop=True)],axis = 1)
# st.write(data_top_5_rca.loc[data_top_5_rca['year']=='2017'])

def regresi():
    # if start_tahun <=2017 & end_tahun>=2017
    # data1 = data_top_5_rca.loc[data_top_5_rca['year']=='2017']
    data1 = data_top_5_rca
    x1 = data1['total_menerima_export_udang_dari_indonesia']
   
    y1 = data1['RCA']
    # data2 = data_top_5_rca.loc[data_top_5_rca['year']=='2018']
    # x2 = data2['total_menerima_export_udang_dari_indonesia']
   
    # y2 = data2['RCA']
    # data3 = data_top_5_rca.loc[data_top_5_rca['year']=='2019']
    # x3 = data3['total_menerima_export_udang_dari_indonesia']
   
    # y3 = data3['RCA']
    # data4 = data_top_5_rca.loc[data_top_5_rca['year']=='2020']
    # x4 = data4['total_menerima_export_udang_dari_indonesia']
   
    # y4 = data4['RCA']
    # data5 = data_top_5_rca.loc[data_top_5_rca['year']=='2021']
    # x5 = data5['total_menerima_export_udang_dari_indonesia']
   
    # y5 = data5['RCA']
    #x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    #y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
    slope, intercept, r, p, std_err = stats.linregress(x1, y1)

    def myfunc(x):
        return slope * x + intercept

    mymodel1 = list(map(myfunc, x1))
    # mymodel2 = list(map(myfunc, x2))
    # mymodel3 = list(map(myfunc, x3))
    # mymodel4 = list(map(myfunc, x4))
    # mymodel5 = list(map(myfunc, x5))
   
    plt.plot(x1, mymodel1)
    # plt.plot(x2, mymodel2)
    # plt.plot(x3, mymodel3)
    # plt.plot(x4, mymodel4)
    # plt.plot(x5, mymodel5)
    # plt.show()
    
    fig = plt.figure(figsize=(3, 2))
    # plt.scatter(x1, y1, color = 'green')
    # plt.scatter(x2, y2, color = 'blue')
    # plt.scatter(x3, y3, color = 'yellow')
    # plt.scatter(x4, y4, color = 'red')
    # plt.scatter(x5, y5, color = 'black')

    plt.scatter(x1, y1, color = 'blue')
    # plt.scatter(x2, y2, color = 'blue')
    # plt.scatter(x3, y3, color = 'blue')
    # plt.scatter(x4, y4, color = 'blue')
    # plt.scatter(x5, y5, color = 'blue')
   
        
    st.pyplot(fig)

def histogram():
    data = data_top_5_rca
    x = data['RCA']
    #x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

    fig = plt.figure(figsize=(5, 2))
    plt.hist(x)

    st.pyplot(fig)
def histogram_total():
    data = data_top_5_rca
    x = data['total_menerima_export_udang_dari_indonesia']
    #x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

    fig = plt.figure(figsize=(5, 2))
    plt.hist(x)

    st.pyplot(fig)
# col1,col2,col3 = st.columns(3)
# with col1:
#     st.write('Nilai RCA')
#     histogram()
    
# with col2:
#     st.write('Jumlah Ekspor')
#     histogram_total()
# with col3:
#     st.write('Hubungan Jumlah Export -> RCA')  
#     regresi()




#caridata
cari = option
st.write('**Pilih data dari dropdown di sidebar untuk melihat nilai RCA**')
st.write(cari)
data1=data_5_all.loc[data_5_all['country']==cari].reset_index(drop=True)
data2 = export_total_indo_all.loc[export_total_indo_all['country']==cari]
data2 = data2['total_menerima_export_all_produk'].reset_index(drop=True)
data3 = export_udang_dunia_all.loc[export_udang_dunia_all['country']==cari]
data3 = data3['export_udang_dunia'].reset_index(drop=True)
data4 = export_total_dunia_all.loc[export_total_dunia_all['country']==cari]
data4 = data4['export_total_dunia'].reset_index(drop=True)
# gabungkan data 1,2,3,4
data_join = pd.concat([data1, data2,data3,data4], axis=1)
#st.write(data_join)
#mencari nilai rca
data_join['RCA1']=data_join['total_menerima_export_udang_dari_indonesia']/data_join['total_menerima_export_all_produk']
data_join['RCA2']=data_join['export_udang_dunia']/data_join['export_total_dunia']
data_join['RCA'] = data_join['RCA1']/data_join['RCA2']
bar_chart = alt.Chart(data_join).mark_line().encode(
        y='RCA:Q',
        x='year:O',
        tooltip=['year', 'RCA']
    )
st.altair_chart(bar_chart, use_container_width=True)

with st.expander("Lihat Data Tabel"):
    st.write(data_join[['country','year','RCA']])


# st.write(udang_indonesia_ke_all[['country','2021']])
# st.write(export_udang_dunia_all.loc(export_udang_dunia_all['year']=='2021'))

indo_ke_all = udang_indonesia_ke_all[['country','2021']]
all_ke_all = export_udang_dunia_all.loc[export_udang_dunia_all['year']=='2021']
negara_tidak_indonesia = pd.merge(indo_ke_all,all_ke_all, on='country',how='right')
negara_tidak_indonesia = negara_tidak_indonesia.loc[negara_tidak_indonesia['2021'].isnull()]
negara_tidak_indonesia = negara_tidak_indonesia[['country','export_udang_dunia']]
negara_tidak_indonesia.drop(negara_tidak_indonesia.loc[negara_tidak_indonesia['country']=='Indonesia'].index, inplace=True)
# st.write(indo_ke_all)
# st.write(all_ke_all)


latlong = pd.read_csv('latlong.csv')

negara_latlong = pd.merge(negara_tidak_indonesia,latlong, on='country')

negara_latlong['lat'].astype(int)
negara_latlong['lon'].astype(int)

with st.container():
    st.header('Export Product Dynamics ')
    st.write('Melihat tingkat kedinamisan pertumbuhan ekspor pada suatu peridoe tertentu yang nantinya akan dikelompokan menjadi 4 indikator yaitu rising star, falling star, lost opportunity dan retreat.')
    image = Image.open('matrix.JPG')
    st.image(image,'matrix EPD')
    data_import = pd.read_csv('indo_import_udang_dunia.csv')
    data_import = data_import.loc[data_import['country']=='World']
    data_export_dunia = pd.read_csv('export_dunia.csv')
    data_export_dunia = data_export_dunia.loc[data_export_dunia['country']=='World']
    data_import = data_import.set_index('country').stack().reset_index()
    data_export_dunia = data_export_dunia.set_index('country').stack().reset_index()
    data_import.columns=['country1', 'year', 'indo_import_udang']
    data_export_dunia.columns=['country2', 'year', 'export_seluruh_dunia']
    # data_import
    # data_export_dunia
    
    # data1
    udang_indonesia_ke_all = pd.read_csv('indonesia_export_udang_ke_all.csv')
    udang_indonesia_ke_all_world = udang_indonesia_ke_all.iloc[0:1 , :]
    udang_indonesia_ke_all = udang_indonesia_ke_all.iloc[1: , :]
    #udang_indonesia_ke_all = udang_indonesia_ke_all.head(5)
    #st.write(udang_indonesia_ke_all)
    #st.write(udang_indonesia_ke_all_world.head(5))
    data_5_all = udang_indonesia_ke_all.set_index('country').stack().reset_index()
    data_5_all.columns=['country', 'year', 'total']
    #data indonesia export semua komuditas ke negara tujuan
    export_total_indo_all = pd.read_csv('export_total_negara_indo_ke_all.csv')
    export_total_indo_all_world = export_total_indo_all.iloc[0:1 , :]
    export_total_indo_all = export_total_indo_all.iloc[1: , :]
    #export_total_indo_all = export_total_indo_all.head(5)
    export_total_indo_all=export_total_indo_all.set_index('country').stack().reset_index()
    export_total_indo_all.columns=['country', 'year', 'total_menerima_export_all_produk']
    
    export_udang_dunia_all = pd.read_csv('export_udang_dunia_ke_all.csv')
    export_udang_dunia_all_world = export_udang_dunia_all.iloc[0:1 , :]
    export_udang_dunia_all = export_udang_dunia_all.iloc[1: , :]
    export_udang_dunia_all = export_udang_dunia_all.set_index('country').stack().reset_index()
    export_udang_dunia_all.columns=['country', 'year', 'export_udang_dunia']
    
    export_total_dunia_all = pd.read_csv('export_total_dunia_ke_all.csv')
    export_total_dunia_all_world = export_total_dunia_all.iloc[0:1 , :]
    export_total_dunia_all = export_total_dunia_all.iloc[1: , :]
    export_total_dunia_all = export_total_dunia_all.set_index('country').stack().reset_index()
    export_total_dunia_all.columns=['country', 'year', 'export_total_dunia']
    data_5_all.columns=['country', 'year', 'total_menerima_export_udang_dari_indonesia']
    data_baru = data_5_all

    data1=data_baru.reset_index(drop=True)
    data2 = export_total_indo_all
    data2 = data2[['country','year','total_menerima_export_all_produk']].reset_index(drop=True)
    data3 = export_udang_dunia_all
    data3 = data3[['country','year','export_udang_dunia']].reset_index(drop=True)
    data4 = export_total_dunia_all
    data4 = data4[['country','year','export_total_dunia']].reset_index(drop=True)
    # data1
    # data2
    # data3
    # data4
    data_join = pd.merge(data1,data2,on=['country','year'], how='left')
    data_join = pd.merge(data_join,data3,on=['country','year'], how='left')
    data_join = pd.merge(data_join,data4,on=['country','year'], how='left')
    data_join = pd.merge(data_join,data_import,on='year', how='left')
    data_join = pd.merge(data_join,data_export_dunia,on='year', how='left')
    hasil = data_join
    hasil['atas'] = data_join['total_menerima_export_udang_dari_indonesia']/data_join['indo_import_udang']
    hasil['bawah'] = data_join['export_total_dunia']/data_join['export_seluruh_dunia']
    
    hasil_2021 = hasil.loc[hasil['year'] == '2021']
    hasil_2021 = hasil_2021[['country','atas','bawah']]
    hasil_2021.columns=['country', 'atas_2021', 'bawah_2021']

    hasil_2020 = hasil.loc[hasil['year'] == '2020']
    hasil_2020 = hasil_2020[['country','atas','bawah']]
    hasil_2020.columns=['country', 'atas_2020', 'bawah_2020']

    hasil_2019 = hasil.loc[hasil['year'] == '2019']
    hasil_2019 = hasil_2019[['country','atas','bawah']]
    hasil_2019.columns=['country', 'atas_2019', 'bawah_2019']

    hasil_2018 = hasil.loc[hasil['year'] == '2018']
    hasil_2018 = hasil_2018[['country','atas','bawah']]
    hasil_2018.columns=['country', 'atas_2018', 'bawah_2018']

    hasil_2017 = hasil.loc[hasil['year'] == '2017']
    hasil_2017 = hasil_2017[['country','atas','bawah']]
    hasil_2017.columns=['country', 'atas_2017', 'bawah_2017']

    epd = pd.merge(hasil_2021,hasil_2020,on=['country'], how='left')
    epd = pd.merge(epd,hasil_2019,on=['country'], how='left')
    epd = pd.merge(epd,hasil_2018,on=['country'], how='left')
    epd = pd.merge(epd,hasil_2017,on=['country'], how='left')
    

    epd['atas_2021'].astype(str).astype(float)
    epd['atas_2020'].astype(str).astype(float)
    epd['atas_2019'].astype(str).astype(float)
    epd['atas_2018'].astype(str).astype(float)
    epd['atas_2017'].astype(str).astype(float)
    epd['bawah_2021'].astype(str).astype(float)
    epd['bawah_2020'].astype(str).astype(float)
    epd['bawah_2019'].astype(str).astype(float)
    epd['bawah_2018'].astype(str).astype(float)
    epd['bawah_2017'].astype(str).astype(float)
    epd['hasil_atas_sesudah_covid'] = (epd['atas_2021']-epd['atas_2020'])/2
    epd['hasil_bawah_sesudah_covid'] = (epd['bawah_2021']-epd['bawah_2020'])/2
    epd['hasil_atas_sebelum_covid'] = (epd['atas_2020']-epd['atas_2019'])/2
    epd['hasil_bawah_sebelum_covid'] = (epd['bawah_2020']-epd['bawah_2019'])/2
    epd.loc[(epd['hasil_atas_sebelum_covid'] <0) & (epd['hasil_bawah_sebelum_covid']<0), 'keterangan_sebelum'] = 'Retreat'
    epd.loc[(epd['hasil_atas_sebelum_covid'] >=0) & (epd['hasil_bawah_sebelum_covid']>=0), 'keterangan_sebelum'] = 'Rising Star'
    epd.loc[(epd['hasil_atas_sebelum_covid'] >=0) & (epd['hasil_bawah_sebelum_covid']<0), 'keterangan_sebelum'] = 'Falling Star' 
    epd.loc[(epd['hasil_atas_sebelum_covid'] <0) & (epd['hasil_bawah_sebelum_covid']>=0), 'keterangan_sebelum'] = 'Lost Opportunity'   
    epd.loc[(epd['hasil_atas_sebelum_covid'] <0) & (epd['hasil_bawah_sebelum_covid']>=0), 'keterangan_sebelum'] = 'Lost Opportunity' 

    epd.loc[(epd['hasil_atas_sesudah_covid'] <0) & (epd['hasil_bawah_sesudah_covid']<0), 'keterangan_sesudah'] = 'Retreat'
    epd.loc[(epd['hasil_atas_sesudah_covid'] >=0) & (epd['hasil_bawah_sesudah_covid']>=0), 'keterangan_sesudah'] = 'Rising Star'
    epd.loc[(epd['hasil_atas_sesudah_covid'] >=0) & (epd['hasil_bawah_sesudah_covid']<0), 'keterangan_sesudah'] = 'Falling Star' 
    epd.loc[(epd['hasil_atas_sesudah_covid'] <0) & (epd['hasil_bawah_sesudah_covid']>=0), 'keterangan_sesudah'] = 'Lost Opportunity'   
    epd.loc[(epd['hasil_atas_sesudah_covid'] <0) & (epd['hasil_bawah_sesudah_covid']>=0), 'keterangan_sesudah'] = 'Lost Opportunity'     
    
    # epd
    c = alt.Chart(epd).mark_circle().encode(
     x='hasil_atas_sebelum_covid', y='hasil_bawah_sebelum_covid', color='country', tooltip=['hasil_atas_sebelum_covid', 'hasil_bawah_sebelum_covid', 'country','keterangan_sebelum'])

    st.subheader('Matrix Sebelum Covid 19')
    st.altair_chart(c, use_container_width=True)

    
  
    # epd
    d = alt.Chart(epd).mark_circle().encode(
     x='hasil_atas_sesudah_covid', y='hasil_bawah_sesudah_covid', color='country', tooltip=['hasil_atas_sesudah_covid', 'hasil_bawah_sesudah_covid', 'country','keterangan_sesudah'])
    
    epd.loc[(epd['keterangan_sesudah'] == epd['keterangan_sebelum']), 'status'] = 'Tidak Ada Perubahan'
    epd.loc[(epd['keterangan_sesudah'] != epd['keterangan_sebelum']), 'status'] = 'Ada Perubahan'
    st.subheader('Matrix Setelah Covid 19')
    st.altair_chart(d, use_container_width=True)
    st.write('Dari diagram diatas terdapat perubahan status dari sebelum terjadinya COVID 19 dengan Sesudah terjadinya Covid 19')
    st.write('dimana sebagai contoh **USA** mengalami perubahan status dari **Rising Star** menjadi **Retreat**')
    st.write('tetapi sebaliknya **Brunei Darussalam** mengalami perubahan status dari **Lost Opportunity** menjadi **Rising Star**')
    with st.expander('lihat sumber'):
        st.write('')
        st.write('sumber Estherhuizen D. 2006. Measuring and Analyzing Competitiveness in the  Agribusiness Sector: Methodological and Analytical Framework')
        st.table(epd[['country','keterangan_sebelum','keterangan_sesudah','status']])
        
st.map(negara_latlong[['lat','lon']])
st.write('Data sebaran diatas adalah negara-negara yang melakukan import udang beku dari **negara lain diluar Indonesia**')

st.write('Jika dilihat negara yang dekat dengan Indonesia, yaitu **Timor-Leste** saja melakukan import udang dari negara lain padalah kita adalah negara tetangga terdekatnya.')
col1,col2 = st.columns(2)

with col1:
    st.write('**Top 10 Daftar Negara Importir Udang bukan dari Indonesia**')
   

    c = alt.Chart(negara_latlong.head(10)).mark_bar(interpolate='basis').encode(
            x='export_udang_dunia', y=alt.Y('country', sort='-x'),  color='country:N',tooltip=['export_udang_dunia', 'country'])

    st.altair_chart(c)
with col2:
    st.write('**Down 10 Daftar Negara Importir Udang bukan dari Indonesia**')
    

    c = alt.Chart(negara_latlong.tail(10)).mark_bar(interpolate='basis').encode(
            x='export_udang_dunia', y=alt.Y('country', sort='x'),  color='country:N',tooltip=['export_udang_dunia', 'country'])

    st.altair_chart(c)



st.write('Negara-Negara diatas adalah negara yang melakukan import Udang Beku dari negara lain. Agar Indonesia dapat memperlebar pasar ke negara tersebut dibutuhkan peran dari pemerintah untuk mendorong kerjasama dengan negara tersebut agar export udang beku di Indonesia bisa ditingkatkan untuk meningkatkan pendapatan negara')
