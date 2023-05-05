import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#read dataset
data = pd.read_csv("world-happiness-report-2021.csv")

#check for missing value
print(data.insull().sum())