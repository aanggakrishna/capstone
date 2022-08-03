import streamlit as st
import pandas as pd
import altair as alt
#sidebar-start
with st.sidebar:
    st.write('ini sidebar')

#sidebar-end

#content-start

st.title('TOP 5 Negara Export Udang Beku')
st.write('hello')

data = pd.read_csv('5exportall.csv')
data = data.set_index('country').stack().reset_index()
data.columns=['country', 'year', 'total']
data_all = data.head(25)
data_indonesia = data_all.loc[data_all['country'] == 'Indonesia']
data_indonesia = data_indonesia.set_index('country')
tahun =list(set(data['year']))
with st.container():
    st.write('/USD Dollar thousand')
    col1, col2, col3,col4 = st.columns(4)
    with col1:
        nilai = data_indonesia.loc[data_indonesia['year'] == '2018']
        nilai_sebelumnya = data_indonesia.loc[data_indonesia['year'] == '2017']
        delta = nilai['total']-nilai_sebelumnya['total']
        st.metric('2018',nilai['total'],delta.iloc[0])

    with col2:
        nilai = data_indonesia.loc[data_indonesia['year'] == '2019']
        nilai_sebelumnya = data_indonesia.loc[data_indonesia['year'] == '2018']
        delta = nilai['total']-nilai_sebelumnya['total']
        st.metric('2019',nilai['total'],delta.iloc[0])

    with col3:
        nilai = data_indonesia.loc[data_indonesia['year'] == '2020']
        nilai_sebelumnya = data_indonesia.loc[data_indonesia['year'] == '2019']
        delta = nilai['total']-nilai_sebelumnya['total']
        st.metric('2020',nilai['total'],delta.iloc[0])

    with col4:
        nilai = data_indonesia.loc[data_indonesia['year'] == '2021']
        nilai_sebelumnya = data_indonesia.loc[data_indonesia['year'] == '2019']
        delta = nilai['total']-nilai_sebelumnya['total']
        st.metric('2021',nilai['total'],delta.iloc[0])

with st.container():
    bar_chart_indonesia = alt.Chart(data_indonesia).mark_line().encode(
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
    c = alt.Chart(data_all).mark_line().encode(
        x='year', y='total', color='country',tooltip=['year', 'total', 'country'])

    st.altair_chart(c, use_container_width=True)
    with st.expander("See data"):
        table = pd.pivot_table(data_all, values='total', index=['country'],
                        columns=['year'])
        st.table(table.sort_values('2021',ascending=False))
        st.write("""
            Sumber trademap.org""")
     



