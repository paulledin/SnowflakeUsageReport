# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:32:27 2024

@author: PLedin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 13:40:15 2024

@author: Paul Ledin
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

###############################################################################
#Function Definitions
###############################################################################



###############################################################################
#Start building Streamlit App
###############################################################################
thePassPhrase = st.secrets["thePassPhrase"]

st.set_page_config(
    page_title="America's Credit Unions",
    layout="wide",
    initial_sidebar_state="expanded")

with st.sidebar:
    st.markdown('![alt text](https://raw.githubusercontent.com/paulledin/data/master/ACUS.jpg)')
    passphrase = st.text_input("### Please enter the passphrase:")

if (passphrase != thePassPhrase):
    if len(passphrase) > 0:
        st.markdown('# Passphrase not correct....')
        st.markdown('### Please try again or contact: pledin@americascreditunions.org for assistance.')
else:
    with st.sidebar:
        st.title('Snowflake Usage Report')
    
 
