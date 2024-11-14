# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:56:12 2024

@author: PLedin
"""

#import libs
import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime

###  Temp variables until DB connection is setup.  ###
date = "2024-05-01"
financials_period = "December 2023"
month = "November"
year = 2023
delta = -.08

#@st.cache_data
def load_data(period = '202401', afl_type = 'Combined', grouping = 'State'):
    df_afl_rpt_1 = pd.read_csv('c:\\users\\pledin\\streamlit\\' + afl_type + '\\' + grouping + '\\' + '\\MonthAFL_Rep_' + period + '.csv')
    df_afl_rpt_1['pct_cus_afl'] = round(df_afl_rpt_1['pct_cus_afl'] * 100, 1)
    df_afl_rpt_1['pct_members_afl'] = round(df_afl_rpt_1['pct_members_afl'] * 100, 1)
    df_afl_rpt_1['pct_assets_afl'] = round(df_afl_rpt_1['pct_assets_afl'] * 100, 1)
    df_afl_rpt_1.columns = ['State','Affiliated CUs','Non-Affiliated CUs','State Chartered','Fed Chartered','Total CUs','Affiliated Memberships','Affiliated Assets','Total Memberships','Total Assets','% CUs Affiliated','% Memberships Affiliated', '% Assets Affiliated']
    
    df_afl_rpt_2 = pd.read_csv('c:\\users\\pledin\\streamlit\\' + afl_type + '\\' + grouping + '\\' + '\\MonthAFL_Rep2_' + period + '.csv')
    df_afl_rpt_2['pct_cus_afl'] = round(df_afl_rpt_2['pct_cus_afl'] * 100, 1)
    df_afl_rpt_2['pct_members_afl'] = round(df_afl_rpt_2['pct_members_afl'] * 100, 1)
    df_afl_rpt_2['pct_assets_afl'] = round(df_afl_rpt_2['pct_assets_afl'] * 100, 1)
    df_afl_rpt_2.columns = ['State','Affiliated CUs','Non-Affiliated CUs','State Chartered','Fed Chartered','Total CUs','Affiliated Memberships','Affiliated Assets','Total Memberships','Total Assets','% CUs Affiliated','% Memberships Affiliated', '% Assets Affiliated']
    
    df_exec_sum = pd.read_csv('c:\\users\\pledin\\streamlit\\' + afl_type + '\\' + grouping + '\\' + '\\Exec_Summary_' + period + '.csv')
    df_exec_sum.columns = ['', month + ' ' + str(year), 'YTD - ' + str(year), 'YTD - ' + str(year - 1)]
    
    df_exec_sum2 = pd.read_csv('c:\\users\\pledin\\streamlit\\' + afl_type + '\\' + grouping + '\\' + '\\Exec_Summary2_' + period + '.csv')
    df_exec_sum2.at[3, 'current_month'] = round(df_exec_sum2.at[3, 'current_month'] * 100, 1)
    df_exec_sum2.at[3, 'prev_yr_month'] = round(df_exec_sum2.at[3, 'prev_yr_month'] * 100, 1)
    df_exec_sum2.at[3, 'prev_2yr_month'] = round(df_exec_sum2.at[3, 'prev_2yr_month'] * 100, 1)
    df_exec_sum2.at[4, 'current_month'] = round(df_exec_sum2.at[4, 'current_month'] * 100, 1)
    df_exec_sum2.at[4, 'prev_yr_month'] = round(df_exec_sum2.at[4, 'prev_yr_month'] * 100, 1)
    df_exec_sum2.at[4, 'prev_2yr_month'] = round(df_exec_sum2.at[4, 'prev_2yr_month'] * 100, 1)
    df_exec_sum2.at[5, 'current_month'] = round(df_exec_sum2.at[5, 'current_month'] * 100, 1)
    df_exec_sum2.at[5, 'prev_yr_month'] = round(df_exec_sum2.at[5, 'prev_yr_month'] * 100, 1)
    df_exec_sum2.at[5, 'prev_2yr_month'] = round(df_exec_sum2.at[5, 'prev_2yr_month'] * 100, 1)
    df_exec_sum2.columns = ['', month + ' ' + str(year), month + ' ' + str(year - 1), month + ' ' + str(year - 2)]
    
    return df_afl_rpt_1, df_afl_rpt_2, df_exec_sum, df_exec_sum2

#create dataframes from the function 
df_afl_rpt_1, df_afl_rpt_2, df_exec_sum, df_exec_sum2  = load_data(period = '202311', afl_type = 'LegacyCUNA', grouping = 'State')

df_afl_rpt_1.set_index("State", inplace = True)
df_exec_sum.set_index("", inplace = True)
df_exec_sum2.set_index("", inplace = True)

totals = df_afl_rpt_1.loc["Totals:"]
totals['Total Assets'] = totals['Total Assets'] / 1000000000
totals['Affiliated Assets'] = totals['Affiliated Assets'] / 1000000000
totals['Total Memberships'] = totals['Total Memberships'] / 1000000
totals['Affiliated Memberships'] = totals['Affiliated Memberships'] / 1000000


###############################################################################
#Start building Streamlit App
###############################################################################
add_sidebar_section = st.sidebar.selectbox('Report Section', ('Executive Summary','Affiliation Report', 'Cover Memo', 'Affiliation Chart', 'Status Change List', 
                                                                     'Affiliation Change List', 'Name Change List', 'New Credit Unions', 'Address Change List', 'Misc'))
add_sidebar_month = st.sidebar.selectbox('Month', ('May 2024','April 2024', 'March 2024'))


st.title("America's Credit Unions")
st.header("Monthly Report")

if add_sidebar_section == 'Executive Summary':
    st.write("Executive Summary")
    st.write("DATE: ", date)
    st.write("NOTE: The information below reports changes to America's Credit Unions' records over the last month. Members and Assets are taken ",
             "from the most recent NCUA call report data (", financials_period, ").")
    add_month = st.selectbox('Affiliation Type:', ('Combined', 'Legacy CUNA Only', 'Legacy NAFCU Only'))
    st.write("----------------------------------------------------------")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    
    with columns[0]:
        st.metric(label= "Total Active CUs", value = "{:,.0f}".format(totals['Affiliated CUs'] + totals['Non-Affiliated CUs']))
        st.metric(label= "Assets ($B)", value = "{:,.1f}".format(totals['Total Assets']))
        st.metric(label= "Members (M)", value = "{:,.1f}".format(totals['Total Memberships']))
            
    with columns[1]:
        st.metric(label= "Affiliated CUs", value = "{:,.0f}".format(totals['Affiliated CUs']))
        st.metric(label= "Affiliated Assets ($B)", value = "{:,.1f}".format(totals['Affiliated Assets']))
        st.metric(label= "Affiliated Mems (M)", value = "{:,.1f}".format(totals['Affiliated Memberships']))
            
    with columns[2]:
        st.metric(label= "Non Affiliated CUs", value = "{:,.0f}".format(totals['Non-Affiliated CUs']))
        st.metric(label= "Non-Afl Assets ($B)", value = "{:,.1f}".format(totals['Total Assets'] - totals['Affiliated Assets']))
        st.metric(label= "Non-Afl Mems (M)", value = "{:,.1f}".format(totals['Total Memberships'] - totals['Affiliated Memberships']))
        
    with columns[4]:
        st.metric(label= "% Affiliated CUs", value = "{:,.1%}".format(totals['Affiliated CUs'] / (totals['Affiliated CUs'] + totals['Non-Affiliated CUs'])))
        st.metric(label= "% Affiliated Assets", value = "{:,.1%}".format(totals['Affiliated Assets'] / totals['Total Assets']))
        st.metric(label= "% Affiliated Mems", value = "{:,.1%}".format(totals['Affiliated Memberships'] / totals['Total Memberships']))
    st.write("----------------------------------------------------------")        
    
    st.dataframe(df_exec_sum)
    st.write("----------------------------------------------------------")
    
    st.dataframe(df_exec_sum2)
    st.write("----------------------------------------------------------")
          
    
    
if add_sidebar_section == 'Affiliation Report':
    st.write("Affiliation Report")
    st.write(add_sidebar_month)
    st.write("Financial Data As Of -> ", financials_period)
    add_month = st.selectbox('Affiliation Type:', ('Combined', 'Legacy CUNA Only', 'Legacy NAFCU Only'))
    add_month = st.selectbox('Group By:', ('State', 'League', 'Asset Class (1)', 'Asset Class (2)'))
    st.write("----------------------------------------------------------")
        
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    
    with columns[0]:
        st.metric(label= "Total Active CUs", value = "{:,.0f}".format(totals['Affiliated CUs'] + totals['Non-Affiliated CUs']))
        
    with columns[1]:
        st.metric(label= "Affiliated CUs", value = "{:,.0f}".format(totals['Affiliated CUs']))
        
    with columns[2]:
        st.metric(label= "% Affiliated CUs", value = "{:,.1%}".format(totals['Affiliated CUs'] / totals['Total CUs']))
        
    with columns[3]:
        st.metric(label= "% Affiliated Assets", value = "{:,.1%}".format(totals['Affiliated Assets'] / totals['Total Assets']))
        
    with columns[4]:
        st.metric(label= "% Affiliated Members", value = "{:,.1%}".format(totals['Affiliated Memberships'] / totals['Total Memberships']))
    
    st.write("----------------------------------------------------------")
    st.dataframe(df_afl_rpt_1)
    st.write("----------------------------------------------------------")
    st.dataframe(df_afl_rpt_2)
    st.write("----------------------------------------------------------")
    
                    

if add_sidebar_section == 'Cover Memo':
    st.write("Cover Memo")
    
if add_sidebar_section == 'Affiliation Chart':
    st.write("Affiliation Chart")
    
if add_sidebar_section == 'Status Change List':
    st.write("Status Change List")
    
if add_sidebar_section == 'Affiliation Change List':
    st.write("Affiliation Change List")
    
if add_sidebar_section == 'Name Change List':
    st.write("Name Change List")
    
if add_sidebar_section == 'New Credit Unions':
    st.write("New Credit Unions")
    
if add_sidebar_section == 'Address Change List':
    st.write("Address Change List")
    
if add_sidebar_section == 'Misc':
    st.write("Misc")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
