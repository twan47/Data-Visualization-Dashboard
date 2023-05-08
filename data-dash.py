import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

#read dataset notes
data = pd.read_csv("world-happiness-report-2021.csv")

#check for missing value
print(data.insull().sum())

#generate descriptive statistics
print(data.describe())

#check the correlation between variables
print(data.corr())

# Scatter plot
fig1 = px.scatter(data, x="Logged GDP per capita", y="Ladder score", hover_name="Country name", title="GDP per capita vs. Happiness Score")

# Bar chart
fig2 = px.bar(data.nlargest(10, "Ladder score"), x="Country name", y="Ladder score", title="Top 10 Happiest Countries")

#initialize dash app
app=dash.Dash(__name__)

#define app layout
app.layout = html.Div([
    html.H1("World Happiness Dashboard"),
    dcc.Graph(id="scatter-plot", figure=fig1),
    dcc.Graph(id="bar-chart", figure=fig2),
])

#run dash app
if __name__ == "__main__":
    app.run_server(debug=True)
