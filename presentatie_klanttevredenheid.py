#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st


# In[2]:


data = pd.read_csv('Invistico_Airline.csv')
gem_voor_vertrek = pd.read_csv('gem_voor_vertrek.csv')
gem_tijdens_vlucht = pd.read_csv('gem_tijdens_vlucht.csv')
onderwerp_score = pd.read_csv('onderwerp_score.csv')
dis_m_voor = pd.read_csv('dis_m_voor.csv')
dis_m_tijdens = pd.read_csv('dis_m_tijdens.csv')
gem_sat_voor = pd.read_csv('gem_sat_voor.csv')
gem_niet_voor = pd.read_csv('gem_niet_voor.csv')
gem_sat_tijdens = pd.read_csv('gem_sat_tijdens.csv')
gem_niet_tijdens = pd.read_csv('gem_niet_tijdens.csv')


# In[4]:


st.set_page_config(page_title="tevredenheid van een luchtmaatschappij", layout="wide")

row1_spacer1, row1_1, row1_spacer1 = st.columns((0.1, 3.2, 0.1))

with row1_1:
    st.title("Passagierstevredenheid")
    st.write("""
    Welom! Deze presentatie gaat over de passagierstevredenheid. Ik ben op het idee gekomen naar het lezen van een 
    artikel over hoe vliegtuigmaatschappij en luchthavens hun klanttevredenheid kunnen beïnvloeden. Het artikel:
    https://www.travelnext.nl/hoe-kunnen-luchtvaartmaatschappijen-en-vliegvelden-de-klanttevredenheid-verhogen-via-mobile/. 
    In het artikel hebben zij het ook over dat Inflight Entertainment beter moet zijn bij langere vluchten. Hier wil ik dan
    ook naar kijken. 
    
    Mijn dashboard gaat verder in op:
    - Hoe score de onderwerpen en moet er nog wat verbeterd worden.
    - Heeft de lengte van de vlucht invloed op het entertaiment cijfer?
    - Op welke passagiersgroep kunnen zij zich het best focussen?
    
    Voor de data heb ik gebruik gemaakt van een dataset van Kaggle: https://www.kaggle.com/datasets/sjleshrac/airlines-customer-satisfaction.
    """)
    
row2_space1, row2_1, row2_space2, row2_2, row2_space3 = st.columns((0.1, 1, 0.1, 1, 0.1))

with row2_1:
    st.subheader("score per onderwerp")
    dropdown_buttons = [{'label':'Seat comfort', 'method': 'update', 
                     'args':[{'visible': [True, False, False, False, False, False, False, False, False, False, False, False, False, False]},
                            {'title': 'Seat comfort'}]},
                   {'label':'Departure/Arrival time convenient', 'method': 'update', 
                     'args':[{'visible': [False, True, False, False, False, False, False, False, False, False, False, False, False, False]},
                            {'title': 'Departure/Arrival time convenient'}]},
                   {'label':'Food and drink', 'method': 'update', 
                     'args':[{'visible': [False, False, True, False, False, False, False, False, False, False, False, False, False, False]},
                            {'title': 'Food and drink'}]},
                    {'label':'Gate location', 'method': 'update', 
                     'args':[{'visible': [False, False, False, True, False, False, False, False, False, False, False, False, False, False]},
                            {'title': 'Gate location'}]},
                    {'label':'Inflight wifi service', 'method': 'update', 
                     'args':[{'visible': [False, False, False, False, True, False, False, False, False, False, False, False, False, False]},
                            {'title': 'Inflight wifi service'}]},
                    {'label':'Inflight entertainment', 'method': 'update', 
                     'args':[{'visible': [False, False, False, False, False, True, False, False, False, False, False, False, False, False]},
                            {'title': 'Inflight entertainment'}]},
                    {'label':'Online support', 'method': 'update', 
                     'args':[{'visible': [False, False, False, False, False, False, True, False, False, False, False, False, False, False]},
                            {'title': 'Online support'}]},
                    {'label':'Ease of Online booking', 'method': 'update', 
                     'args':[{'visible': [False, False, False, False, False, False, False, True, False, False, False, False, False, False]},
                            {'title': 'Ease of Online booking'}]},
                    {'label':'On-board service', 'method': 'update', 
                     'args':[{'visible': [False, False, False, False, False, False, False, False, True, False, False, False, False, False]},
                            {'title': 'On-board service'}]},
                    {'label':'Leg room service', 'method': 'update', 
                     'args':[{'visible': [False, False, False, False, False, False, False, False, False, True, False, False, False, False]},
                            {'title': 'Leg room service'}]},
                    {'label':'Baggage handling', 'method': 'update', 
                     'args':[{'visible': [False, False, False, False, False, False, False, False, False, False, True, False, False, False]},
                            {'title': 'Baggage handling'}]},
                    {'label':'Checkin service', 'method': 'update', 
                     'args':[{'visible': [False, False, False, False, False, False, False, False, False, False, False, True, False, False]},
                            {'title': 'Checkin service'}]},
                    {'label':'Cleanliness', 'method': 'update', 
                     'args':[{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, True, False]},
                            {'title': 'Cleanliness'}]},
                    {'label':'Online boarding', 'method': 'update', 
                     'args':[{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, True]},
                            {'title': 'Online boarding'}]}
                   ]
    fig = px.histogram(data, x=['Seat comfort', 'Departure/Arrival time convenient', 'Food and drink', 'Gate location',
       'Inflight wifi service', 'Inflight entertainment', 'Online support',
       'Ease of Online booking', 'On-board service', 'Leg room service',
       'Baggage handling', 'Checkin service', 'Cleanliness', 'Online boarding'], 
                   barmode='group', histnorm='percent')
    fig.update_layout({'updatemenus':[{'type': "dropdown",
                                  'x': 1.3,
                                  'y': 1.2,
                                  'showactive': True,
                                  'active': 0,
                                  'buttons': dropdown_buttons}]})
    fig.update_layout(bargap=0.3,
                 xaxis_title_text='Waarde',
                 yaxis_title_text='Percentage')
    fig.add_annotation(x=1.35, y=0.5,
                  text='0 - Niet van toepassing <br>1 - slecht <br> 3 - neutraal <br>5 - goed',
                  showarrow=False,
                  xref='paper',
                  yref='paper',
                  bordercolor='black',
                  borderwidth=1)
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)
    
with row2_2:
    st.subheader("Gemiddelde score per onderwerp")
    fig = make_subplots(rows=1, cols=2, shared_yaxes=True,
                   subplot_titles=('Alle passagiers voor de vlucht', 
                                   'Alle passagiers Tijdens de vlucht'))
    fig.add_trace(go.Bar(x=gem_voor_vertrek['index'], y=gem_voor_vertrek['gem_voor'],
                    marker=dict(color=gem_voor_vertrek['gem_voor'], coloraxis='coloraxis'),
                    text=round(gem_voor_vertrek['gem_voor'],3), textposition='auto'),
             row=1, col=1)
    fig.add_trace(go.Bar(x=gem_tijdens_vlucht['index'], y=gem_tijdens_vlucht['gem_tijdens'],
                     marker=dict(color=gem_tijdens_vlucht['gem_tijdens'], coloraxis='coloraxis'),
                    text=round(gem_tijdens_vlucht['gem_tijdens'],3), textposition='auto'),
             row=1, col=2)
    fig.update_layout(coloraxis=dict(colorscale='rdylgn'), showlegend=False)
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)
    
row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns((0.1, 1, 0.1, 1, 0.1))

with row3_1:
    st.subheader("Flight Distance en Inflight entertainment")
    fig = px.box(onderwerp_score, x='Inflight entertainment', y='Flight Distance', color='satisfaction')
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

with row3_2:
    fig = make_subplots(rows=1, cols=4, shared_yaxes=True,
                   subplot_titles=('Niet tevreden (voor)',
                                  '(tijdens)',
                                  'Tevreden (voor)',
                                  '(tijdens)'))
    fig.add_trace(go.Bar(x=gem_niet_voor['index'], y=gem_niet_voor['gem_niet'],
                    marker=dict(color=gem_niet_voor['gem_niet'], coloraxis='coloraxis'),
                    text=round(gem_niet_voor['gem_niet'],3), textposition='auto'),
             row=1, col=1)
    fig.add_trace(go.Bar(x=gem_niet_tijdens['index'], y=gem_niet_tijdens['gem_tijdens_niet'],
                     marker=dict(color=gem_niet_tijdens['gem_tijdens_niet'], coloraxis='coloraxis'),
                    text=round(gem_niet_tijdens['gem_tijdens_niet'],3), textposition='auto'),
             row=1, col=2)
    fig.add_trace(go.Bar(x=gem_sat_voor['index'], y=gem_sat_voor['gem_sat'],
                    marker=dict(color=gem_sat_voor['gem_sat'], coloraxis='coloraxis'),
                    text=round(gem_sat_voor['gem_sat'],3), textposition='auto'),
             row=1, col=3)
    fig.add_trace(go.Bar(x=gem_sat_tijdens['index'], y=gem_sat_tijdens['gem_tijdens_sat'],
                     marker=dict(color=gem_sat_tijdens['gem_tijdens_sat'], coloraxis='coloraxis'),
                    text=round(gem_sat_tijdens['gem_tijdens_sat'],3), textposition='auto'),
             row=1, col=4)
    fig.update_layout(coloraxis=dict(colorscale='rdylgn'), showlegend=False)
    fig.update_coloraxes(showscale=False)
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)
    
row4_spacer1, row4_1, row4_spacer1 = st.columns((0.1, 3.2, 0.1))

with row4_1:
    st.write("""
    Er kan vooral verbeterd worden op service tijdens de vlucht en dan voornamelijk op Seat Comfort
    en Food en drink. Ook is de Inflight entertainment interessant, want er zijn grote verschillen
    te zien tussen tevreden en ontevreden passagiers. Er lijk geen verband te zijn met het cijfer van
    entertainment en de lengte van de vlucht.""")
    
    
row5_space1, row5_1, row5_space2, row5_2, row5_space3 = st.columns((0.1, 1, 0.1, 1, 0.1))

with row5_1:
    st.subheader("Tevredenheid per type passagiers")
    fig, ax = plt.subplots() 
    sns.heatmap(pd.crosstab([onderwerp_score['Gender'], onderwerp_score['Type of Travel'],
                        onderwerp_score['Class']], [onderwerp_score['satisfaction']],
                       normalize=True, margins=True),
           cmap='YlGnBu', annot=True, ax=ax)
    st.pyplot(fig, theme='streamlit', use_container_width=True)
    
with row5_2:
    st.subheader("Pie chart passagiers tevredenheid")
    fig = px.sunburst(onderwerp_score, path=['satisfaction', 'Gender', 'Type of Travel', 'Class'])
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)
    
row6_spacer1, row6_1, row6_spacer2 = st.columns((0.1, 3.1, 0.1))

with row6_1:
    st.subheader("Dissatisfied Male Personal Travel Eco")
    fig = make_subplots(rows=1, cols=2, shared_yaxes=True,
                   subplot_titles=('Voor de vlucht', 'Tijdens de vlucht'))
    fig.add_trace(go.Bar(x=dis_m_voor['index'], y=dis_m_voor['voor'],
                    name='Dissatisfied Male Personal Travel Eco', 
                     marker=dict(color=dis_m_voor['voor'], coloraxis='coloraxis'),
                    text=round(dis_m_voor['voor'],3), textposition='auto'),
             row=1, col=1)
    fig.add_trace(go.Bar(x=dis_m_tijdens['index'], y=dis_m_tijdens['tijdens'],
                    name='Dissatisfied Male Personal Travel Eco', 
                     marker=dict(color=dis_m_tijdens['tijdens'], coloraxis='coloraxis'),
                    text=round(dis_m_tijdens['tijdens'],3), textposition='auto'),
             row=1, col=2)
    fig.update_layout(coloraxis=dict(colorscale='rdylgn'), showlegend=False)
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)
    
row7_spacer1, row7_1, row7_spacer1 = st.columns((0.1, 3.2, 0.1))

with row7_1:
    st.write(""" 
    De vluchtvaartmaatschappij kan het best targetten op mannen die voor persoonlijke redenen
    reizen in de eco klasse. Dit is de groep die het meest ontevreden is. Ook hier worden voornamelijk
    de Food en drink, Inflight entertainment en Seat comfort slecht beoordeeld.""")

    
    
#Deze loop is voor het indificeren van errors.     
import asyncio

def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()


# In[ ]:




