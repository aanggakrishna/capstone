import streamlit as st
import pandas as pd
import altair as alt
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from scipy import stats


#content-start

st.title('Daya Saing Udang Beku Indonesia')
st.write('Product: 030617 Frozen shrimps and prawns')
data = pd.read_csv('5exportall.csv')
data = data.set_index('country').stack().reset_index()
data.columns=['country', 'year', 'total']
data_all = data.head(25)
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
    st.write('hello')
    c = alt.Chart(data_all).mark_line().encode(
        x='year', y='total', color='country',tooltip=['year', 'total', 'country'])

    st.altair_chart(c, use_container_width=True)
    with st.expander("See data"):
        table = pd.pivot_table(data_all, values='total', index=['country'],
                        columns=['year'])
        st.table(table)
        st.write("""
            Sumber trademap.org""")
with st.container():
    st.title('lalal')
    st.write('hello')
    st.write('/USD Dollar thousand')
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
    bar_chart_indonesia = alt.Chart(data_indonesia).mark_bar().encode(
        y='total:Q',
        x='year:O',
        tooltip=['year', 'total']
    )
    st.altair_chart(bar_chart_indonesia, use_container_width=True)
    with st.expander("See data"):

        st.table(data_indonesia.sort_values('total',ascending=False))
        st.write("""
            Sumber trademap.org""")



    

with st.container():
    st.title('TOP 5 Negara Tujuan Export Udang Beku Indonesia')
    st.write('#TOP 5 Negara Tujuan Export Udang Indonesia')
    data_5_all = data_5_all.loc[(data_5_all['year']<=end_tahun) & (data_5_all['year']>=start_tahun)]
    data_5_all_negara = data_5_all.head(25)
    c = alt.Chart(data_5_all_negara).mark_bar(interpolate='basis').encode(
        x='country:O', y='total:Q', column='year:N', color='country:N',tooltip=['year', 'total', 'country'])

    st.altair_chart(c)
    with st.expander("See data"):
        table = pd.pivot_table(data_5_all_negara, values='total', index=['country'],
                        columns=['year'])
        st.table(table)
        st.write("""
            Sumber trademap.org""")

with st.container():
    st.title('Daya Saing Indonesia dari Negara Lain untuk')
    st.write('--')

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
with st.expander("See data"):
    st.write(data_join_top_5)







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
    
    fig = plt.figure(figsize=(5, 2))
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
col1,col2,col3 = st.columns(3)
with col1:
    st.write('Nilai RCA')
    histogram()
    
with col2:
    st.write('Jumlah Ekspor')
    histogram_total()
with col3:
    st.write('Hubungan Jumlah Export -> RCA')  
    regresi()




#caridata
cari = option
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
with st.expander("See data"):
    st.write(data_join[['country','year','RCA']])