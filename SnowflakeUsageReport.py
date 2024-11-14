# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:34:26 2024

@author: PLedin
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(
    page_title="America's Credit Unions",
    layout="wide",
    initial_sidebar_state="expanded")

conn = st.connection("snowflake")
###############################################################################
#Function Definitions
###############################################################################
@st.cache_data
def get_information_schema(databaseName):
    session = conn.session()
    retVal = session.sql("SELECT substr(TABLE_NAME, 21, 26) as \"period\" FROM monthly_report.information_schema.tables WHERE table_schema = 'BOTH' and TABLE_NAME like 'AFL_TABLE_1_BYSTATE_%' ").to_pandas()
    
    return retVal
###############################################################################
#Start building Streamlit App
###############################################################################
thePassPhrase = st.secrets["thePassPhrase"]


with st.sidebar:
    st.markdown('![alt text](https://raw.githubusercontent.com/paulledin/data/master/ACUS.jpg)')
    passphrase = st.text_input("### Please enter the passphrase:")

if (passphrase != thePassPhrase):
    if len(passphrase) > 0:
        st.markdown('# Passphrase not correct....')
        st.markdown('### Please try again or contact: pledin@americascreditunions.org for assistance.')
else:
    report_periods = get_information_schema('ACUS_DATA')
    st.write(report_periods)
    
     



    
