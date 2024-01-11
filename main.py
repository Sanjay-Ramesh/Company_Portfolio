import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.title("The Best Company")

content = """Innovating the future with cutting-edge technology, our company is a dynamic force driving progress in diverse industries. We prioritize creativity and excellence, delivering solutions that redefine standards."""

st.write(content)

st.title("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data (3).csv",sep = ",")

with col1:
    for index, row in df[:4].iterrows():
        st.header(row["first name"] +" "+ row["last name"])
        st.write(row["role"])
        st.image("images (3)\\"+row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(row["first name"] +" "+ row["last name"])
        st.write(row["role"])
        st.image("images (3)\\"+row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(row["first name"] +" "+ row["last name"])
        st.write(row["role"])
        st.image("images (3)\\"+row["image"])