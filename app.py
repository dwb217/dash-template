import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd

########### Define a few variables ######

tabtitle = 'Dash Template'
sourceurl = 'https://plot.ly/python/choropleth-maps/'
githublink = 'https://github.com/austinlasseter/dash-template'

### read in Data
df = pd.read_pickle('virginia_total.pkl')
print(df['jurisdiction'].value_counts().sort_index().index)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Layout

app.layout = html.Div(children=[
    html.H1('This is the title'),
    html.Div(children=[
        dcc.Dropdown(
            id-'my-dropdown',
            options=[{'label':i, 'value':i} for i in options_list}],
            value='FAIRFAX CITY',
        ),
    html.Br(),
    dcc.Graph(id='output_div', children=''),
    html.Br(),

    ]),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

@app.callback(Output('output-div', 'figure'),
                [Input('my-dropdown', 'value')])
def county_picker(arg1):
    juris_df=df[df['jurisdiction']==arg1]
            mydata1 = go.Bar(x=list(accomack['precinct'].value_counts().index),
                     y=list(accomack['votes']['Donald Trump']),
                     marker=dict(color='#122A7F'),
                     name='Trump')
            mydata2 = go.Bar(x=list(accomack['precinct'].value_counts().index),
                     y=list(accomack['votes']['Hillary Clinton']),
                     marker=dict(color='#008080'),
                     name='Clinton')
            mydata3 = go.Bar(x=list(accomack['precinct'].value_counts().index),
                     y=list(accomack['votes']['Other']),
                     marker=dict(color='#92A5E8'),
                     name='Other')

            mylayout = go.Layout(
                    title='Grouped bar chart',
                    xaxis=dict(title='Candidates'),
                    yaxis=dict(title='Number of Votes')    
                    )
fig = go.Figure(data=[mydata1, mydata2, mydata3], layout=mylayout)
return fig




############ Callbacks



############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
