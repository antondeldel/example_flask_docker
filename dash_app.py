# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

colors = {"background": "#111111", "text": "#7FDBFF"}

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig2 = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig2.update_layout(
    plot_bgcolor=colors["background"],
    paper_bgcolor=colors["background"],
    font_color=colors["text"],
)


df = pd.read_csv(
    "https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv"
)

fig3 = px.scatter(
    df,
    x="gdp per capita",
    y="life expectancy",
    size="population",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

app.layout = html.Div(
    [
        html.Div(
            children=[
                html.H1(children="Hello Dash"),
                html.Div(
                    children="\nDash: A web application framework for your data.\n"
                ),
                dcc.Graph(id="example-graph", figure=fig),
            ]
        ),
        html.Div(
            style={"backgroundColor": colors["background"]},
            children=[
                html.H1(
                    children="Hello Dash",
                    style={"textAlign": "center", "color": colors["text"]},
                ),
                html.Div(
                    children="Dash: A web application framework for your data.",
                    style={"textAlign": "center", "color": colors["text"]},
                ),
                dcc.Graph(id="example-graph-2", figure=fig2),
            ],
        ),
        html.Div([dcc.Graph(id="life-exp-vs-gdp", figure=fig3)]),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, port=9000)
