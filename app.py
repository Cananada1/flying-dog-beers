import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Set up the chart
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Bud Light lol']

bitterness = go.Bar(
    x=beers,
    y=[35, 60, 85, 40],
    name='IBU',
    marker={'color':'darkgreen'}
)
alcohol = go.Bar(
    x=beers,
    y=[5.4, 7.1, 9.2, 4.2],
    name='ABV',
    marker={'color':'red'}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = 'Beer Comparison'
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('First Try at Code'),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    )]
)

if __name__ == '__main__':
    app.run_server()
