import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State, ALL

# https://www.bootstrapcdn.com/bootswatch/
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}], use_pages=True)

# TODO Home is active when Results is selected 
navbar = dbc.Navbar(
    color="dark",
    dark=True,
    children=[
        html.Div(
            className="container-fluid",
            children=[
                html.A("Meet Me", href="/", className="navbar-brand", style={"font-size": "x-large"}),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    style={"font-size": "large"},
                    id="navbar-collapse",
                    navbar=True,
                    children=[
                        dbc.Nav(
                            className="ms-auto",
                            children=[
                                dbc.NavItem(
                                    dbc.NavLink("Projects", href="/projects")
                                ),
                                dbc.NavItem(
                                    dbc.NavLink("Publications", href="/publications")
                                ),
                                dbc.NavItem(
                                    dbc.NavLink("Awards", href="/awards")
                                ),
                                dbc.NavItem(
                                    dbc.NavLink("Resume", href="/results")
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )
    ],
)

app.layout = html.Div([
    dcc.Location(id="url"),
    navbar,
    dash.page_container
])

# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    Output({"type":"link-navbar", "index":ALL}, "class_name"), 
    Input("url", "pathname"),
    Input({"type":"link-navbar", "index":ALL}, "id"),
    Input("navbar-toggler", "n_clicks"),
    State("navbar-collapse", "is_open")
)
def callback_func(pathname, link_elements, n, is_open):
    if n:
        val = not is_open
    else:
        val = is_open
    class_name = ["active" if val["index"] == pathname else "not-active" for val in link_elements]
    return val, class_name


if __name__=='__main__':
    app.run_server(debug=True, port=8000)