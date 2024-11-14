# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:34:26 2024

@author: PLedin
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

conn = st.connection("snowflake")
###############################################################################
#Function Definitions
###############################################################################
@st.cache_data
def get_report_periods_fromDB():
    session = conn.session()
    retVal = session.sql("SELECT substr(TABLE_NAME, 21, 26) as \"period\" FROM monthly_report.information_schema.tables WHERE table_schema = 'BOTH' and TABLE_NAME like 'AFL_TABLE_1_BYSTATE_%' ").to_pandas()
    
    return retVal

#report_periods = get_report_periods_fromDB()
#st.write(report_periods)



def format_number(amount):
    return '{:,.0f}'.format(amount)

###############################################################################
#Start building Streamlit App
###############################################################################
thePassPhrase = 'PeopleNotProfit$'

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
    column_configuration = {
        "State": st.column_config.TextColumn(
            "State", max_chars=50
            ),
        "Affiliated CUs": st.column_config.NumberColumn(
            "Affiliated CUs",
            min_value=0,
            max_value=10000,
            ),
        "Non Affiliated CUs": st.column_config.NumberColumn(
            "Non Affiliated CUs",
            min_value=0,
            max_value=10000,
            ),
        "State Chartered": st.column_config.NumberColumn(
            "State Chartered",
            min_value=0,
            max_value=10000,
            ),
        "Fed Chartered": st.column_config.NumberColumn(
            "Fed Chartered",
            min_value=0,
            max_value=10000,
            ),
        "Total CUs": st.column_config.NumberColumn(
        "Total CUs",
        min_value=0,
        max_value=10000,
        ),
    "Affiliated Memberships": st.column_config.NumberColumn(
        "Affiliated Memberships",
        min_value=0,
        max_value=10000,
        ),
    "Affiliated Assets": st.column_config.NumberColumn(
        "Affiliated Assets",
        min_value=0,
        max_value=10000,
        ),
    "Total Assets": st.column_config.NumberColumn(
        "Total Assets",
        min_value=0,
        max_value=10000,
        ),
    "% CUs Affiliated": st.column_config.NumberColumn(
        "% CUs Affiliated",
        min_value=0,
        max_value=10000,
        format="%.1f"
        ),
    "% Memberships Affiliated": st.column_config.NumberColumn(
        "% Memberships Affiliated",
        min_value=0,
        max_value=10000,
        format="%.1f"
        ),
    "% Assets Affiliated": st.column_config.NumberColumn(
        "% Assets Affiliated",
        min_value=0,
        max_value=10000,
        format="%.1f"
        ),
    }
     



    
