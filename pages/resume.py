import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, "/resume", title="resume")


layout = html.Div(
    [
        html.Iframe(src='./assets/files/Ahmed-Muntasir-Hossain-Resume.pdf', style={"height": "1067px", "width": "100%"})
    ])