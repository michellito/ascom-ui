import streamlit as st
import time
import numpy as np
from alpaca.telescope import *      # Multiple Classes including Enumerations
from alpaca.exceptions import *     # Or just the exceptions you want to catch
import streamlit as st

st.set_page_config(page_title="Telescope App", page_icon="🔭")

st.title("🔭 Telescope App")

st.sidebar.header("TXT File / Launch")


uploaded_file = st.file_uploader("Select txt file", type=["txt"], accept_multiple_files=False)
if uploaded_file is not None:
  for i in range(len(uploaded_file)):
      head, sep, tail = str(uploaded_file[i].name).partition(".")
      st.write("file name："+str(head))
      st.write("file type："+str(tail))
      st.write(uploaded_file)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
    if st.button('Launch'):
        st.write('Launching!')


T = Telescope('host.docker.internal:80', 0) # Local Omni Simulator

try:
    T.Connected = True
    print(f'Connected to {T.Name}')
    print(T.Description)
    T.Tracking = True               # Needed for slewing (see below)
    print('Starting slew...')
    T.SlewToCoordinatesAsync(T.SiderealTime + 2, 50)    # 2 hrs east of meridian
    while(T.Slewing):
        time.sleep(5)               # What do a few seconds matter?
    print('... slew completed successfully.')
    print(f'RA={T.RightAscension} DE={T.Declination}')
    print('Turning off tracking then attempting to slew...')
    T.Tracking = False
    T.SlewToCoordinatesAsync(T.SiderealTime + 2, 55)    # 5 deg slew N
    # This will fail for tracking being off
    print("... you won't get here!")
except Exception as e:              # Should catch specific InvalidOperationException
    print(f'Slew failed: {str(e)}')
finally:                            # Assure that you disconnect
    print("Disconnecting...")
    T.Connected = False
