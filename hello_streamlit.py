import streamlit as st
import pandas as pd
import numpy as np

unit="#01-02 blk 113 clement west avenue 6"
st.title("Elderly Detection System ")
st.write("Unit details: "+unit)


item=["Microphone","Lidar","Pressure Sensor","Microprocessor"]
item_state=[[False,False],[True,False],[False,False],[True,False]]
detection=True
#format of item state is as follow:[Active state, transmitting state]

if detection:
    st.success("No fall detected. All is good and well but i tired as fuck")
    pass
    #SOP for fall detection
else:
    st.error("Fall detected! Contacting local caregiver")
    pass
    #SOP for all system normal
st.write("_"*20)


col1,col2,col3,col4=st.columns([50,50,50,50],gap="large")
with col1:

    st.subheader(item[0])

    if not item_state[0][0] or not item_state[0][1]:
        st.warning("Warning! Troubleshooting required.")
    st.metric("Status","Active" if item_state[0][0] else "Inactive",delta="+ Device is turned on" if item_state[0][0] else "- Device is turned off")
    st.metric("Transmission", "Active" if item_state[0][1] else "Inactive",delta="+ Device is transmitting" if item_state[0][1] else "- Device is not transmitting")
    st.button("Configure "+item[0])


with col2:
    st.subheader(item[1])
    st.metric("Status", "Active" if item_state[1][0] else "Inactive",\
              delta="+ Device is turned on" if item_state[1][0] else "- Device is turned off")
    st.metric("Transmission", "Active" if item_state[1][1] else "Inactive",\
              delta="+ Device is transmitting" if item_state[1][1] else "- Device is not transmitting")
    st.button("Configure "+item[1])


with col3:
    st.subheader(item[2])
    st.metric("Status", "Active" if item_state[2][0] else "Inactive",
              delta="+ Device is turned on" if item_state[2][0] else "- Device is turned off")
    st.metric("Transmission", "Active" if item_state[2][1] else "Inactive",
              delta="+ Device is transmitting" if item_state[2][1] else "- Device is not transmitting")
    st.button("Configure "+item[2])
with col4:
    st.subheader(item[3])
    st.metric("Status", "Active" if item_state[3][0] else "Inactive",
              delta="+ Device is turned on" if item_state[3][0] else "- Device is turned off")
    st.metric("Transmission", "Active" if item_state[3][1] else "Inactive",
              delta="+ Device is transmitting" if item_state[3][1] else "- Device is not transmitting")
    st.button("Configure "+item[3])

st.subheader("Data transmission")
tab1,tab2,tab3,tab4=st.tabs(item)
with tab3:
    subcol1,subcol2=st.columns(2)
    data=pd.DataFrame([[1,2,3],[4,5,6]])
    data.columns=["Tile 1","Tile 2","Tile 3"]
    data.index=[" Row A","Row B"]
    with subcol1:
        st.table(data)
    with subcol2:
        st.metric("test","test")
    st.metric("test", "test")
    st.metric("test", "test")
    st.metric("test", "test")