# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:25:17 2023

@author: pdnguyen
"""

import subprocess
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Calculator App"),
    html.Button("Open Calculator", id="open-button"),
    html.Div(id="output")
])

@app.callback(
    Output('output', 'children'),
    [Input('open-button', 'n_clicks')]
    )

def open_calculator(n_clicks):
    if n_clicks is not None:
        subprocess.Popen('calc.exe')
        return 'Calculator app opened!'
    
if __name__ == "__main__":
    app.run_server(debug=True)