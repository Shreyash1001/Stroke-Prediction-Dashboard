import streamlit as st
import pandas as pd
from matplotlib import image
import plotly.express as px
import plotly.graph_objects as go
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR,"resources")

DATA_PATH = os.path.join(dir_of_interest, "data","data.csv")

st.title("Stroke Prediction Dashboard")

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

st.markdown("The dashboard will help a researcher to get to know \
more about the given datasets and it's output")
st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Charts/Plots accordingly:")


chart_visual = st.sidebar.selectbox('Select Charts/Plot type',
									('Line Chart', 'Bar Chart', 'Bubble Chart'))

st.sidebar.checkbox("Show Analysis by Smoking Status", True, key = 1)
selected_status = st.sidebar.selectbox('Select Smoking Status',
									options = ['Formerly_Smoked',
												'Smoked', 'Never_Smoked',
												'Unknown'])

fig = go.Figure()

if chart_visual == 'Line Chart':
	if selected_status == 'Formerly_Smoked':
		fig.add_trace(go.Scatter(x = df.Country, y = df.formerly_smoked,
								mode = 'lines',
								name = 'Formerly_Smoked'))
	if selected_status == 'Smoked':
		fig.add_trace(go.Scatter(x = df.Country, y = df.Smokes,
								mode = 'lines', name = 'Smoked'))
	if selected_status == 'Never_Smoked':
		fig.add_trace(go.Scatter(x = df.Country, y = df.Never_Smoked,
								mode = 'lines',
								name = 'Never_Smoked'))
	if selected_status == 'Unknown':
		fig.add_trace(go.Scatter(x=df.Country, y=df.Unknown,
								mode='lines',
								name="Unknown"))

elif chart_visual == 'Bar Chart':
	if selected_status == 'Formerly_Smoked':
		fig.add_trace(go.Bar(x=df.Country, y=df.formerly_smoked,
							name='Formerly_Smoked'))
	if selected_status == 'Smoked':
		fig.add_trace(go.Bar(x=df.Country, y=df.Smokes,
							name='Smoked'))
	if selected_status == 'Never_Smoked':
		fig.add_trace(go.Bar(x=df.Country, y=df.Never_Smoked,
							name='Never_Smoked'))
	if selected_status == 'Unknown':
		fig.add_trace(go.Bar(x=df.Country, y=df.Unknown,
							name="Unknown"))

elif chart_visual == 'Bubble Chart':
	if selected_status == 'Formerly_Smoked':
		fig.add_trace(go.Scatter(x=df.Country,
								y=df.formerly_smoked,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name='Formerly_Smoked'))
		
	if selected_status == 'Smoked':
		fig.add_trace(go.Scatter(x=df.Country, y=df.Smokes,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name='Smoked'))
		
	if selected_status == 'Never_Smoked':
		fig.add_trace(go.Scatter(x=df.Country,
								y=df.Never_Smoked,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name = 'Never_Smoked'))
	if selected_status == 'Unknown':
		fig.add_trace(go.Scatter(x=df.Country,
								y=df.Unknown,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50],
								name="Unknown"))

st.plotly_chart(fig, use_container_width=True)
