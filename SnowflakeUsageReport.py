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

dbConn = st.connection("snowflake")
###############################################################################
#Function Definitions
###############################################################################
@st.cache_data
def get_information_schema(databaseName):
    session = dbConn.session()
    retVal = session.sql("SELECT TABLE_SCHEMA, TABLE_NAME FROM " + databaseName + ".information_schema.tables ").to_pandas()
    
    return retVal
###############################################################################
#Start building Streamlit App
###############################################################################
thePassPhrase = st.secrets["thePassPhrase"]
dbName = 'ACUS_DATA'

with st.sidebar:
    st.markdown('![alt text](https://raw.githubusercontent.com/paulledin/data/master/ACUS.jpg)')
    passphrase = st.text_input("### Please enter the passphrase:")

if (passphrase != thePassPhrase):
    if len(passphrase) > 0:
        st.markdown('# Passphrase not correct....')
        st.markdown('### Please try again or contact: pledin@americascreditunions.org for assistance.')
else:
    information_schema = get_information_schema(dbName)

    st.write('### Contents of Database: ' + dbName)
    
    #st.write(information_schema)
    
     



    
