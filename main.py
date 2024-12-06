import pandas as pd
import streamlit as st

df = pd.read_csv('annotation.csv')

st.title('10 Рандомных книг')

if st.button('Жмай'):
    random = df[['author', 'title']].sample(n=10)
    st.write(random)


