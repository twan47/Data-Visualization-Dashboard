import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# something wrong with end of code. Tried to fix in notebooks and figure problem. No effects.
data = pd.read_csv("world-happiness-report-2021.csv")
print(data.isnull().sum())
print(data.describe())
print(data.corr())
fig1 = px.scatter(data, x="Logged GDP per capita", y="Ladder score", hover_name="Country name", title="GDP per capita vs. Happiness Score")
fig2 = px.bar(data.nlargest(10, "Ladder score"), x="Country name", y="Ladder score", title="Top 10 Happiest Countries")
app=dash.Dash(__name__)
app.layout = html.Div([
    html.H1("World Happiness Dashboard"),
    dcc.Graph(id="scatter-plot", figure=fig1),
    dcc.Graph(id="bar-chart", figure=fig2),
])
if __name__ == "__main__":
    app.run_server(debug=True)
