import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Telescope App", page_icon="🔭", layout="wide")

st.title("TLE File / Settings")
st.sidebar.header("TLE File / Settings")

uploaded_file = st.file_uploader("Select TLE file", type=["tle"], accept_multiple_files=False)
if uploaded_file is not None:
  for i in range(len(uploaded_file)):
      head, sep, tail = str(uploaded_file[i].name).partition(".")
      st.write("file name："+str(head))
      st.write("file type："+str(tail))
      st.write(uploaded_file)

c1, c2, c3 = st.columns(3)

with c1:
    num_images = st.number_input('Number of images', min_value = 1, max_value=None, value=1, key = 1)

    expose_time = st.number_input('Expose time', min_value = 0.0, max_value=None, value=1.0, key = 2)

    max_visits_per_field = st.number_input('Max visits per field', min_value = 1, max_value=None, value=5, key = 3)

    st.write('')
    st.write('Shutdown time')

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
    hour = st.number_input('Hour (0-23)', min_value = 0, max_value=23, value=19, key = 4)

with col2:
    minute = st.number_input('Minute (0-59)', min_value = 0, max_value=59, value=35, key = 5)


st.write('Current number of images:', num_images)
st.write('Current expose time:', expose_time, 'seconds')
st.write('Current max visits per field:', max_visits_per_field)
st.write('Current hour:', hour)
st.write('Current minute:', minute)