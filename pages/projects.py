import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, "/projects", title="Projects")

# Personal Project 1
pp1_desc = ['Developed an application Travelers using Swift where users can provide reviews of different locations',
            'Developed the game 3072 where the user combines numbers to reach the 3072 tile']

# Personal Project 2
pp2_desc = ['Developed a website for students to sell their old coursebooks online - jQuery, Express, Node.js, MongoDB',
            'Incorporated jQuery for RESTful API requests improving the speed of the application by 30% ']

# Personal Project 3
pp3_desc = ['Developed an open-source Android application in Java using Android Studio to help PI enthusiasts memorize 101, 1001, and 10001 digits of PI through auditory and visual learning',
            'Published the app in Google Play Store with 8 installations across the world']

layout = dbc.Container([
    dbc.Row(html.H2('Personal Projects'), className='mt-4 mb-4 text-center'),
    dbc.Row([
        html.B("iOS Mobile Application Development", style={"font-size": "large"}),
        html.P("Jan 2022 - May 2022", style={"color": "white"}),
        html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in pp1_desc]),
    ]),
    dbc.Row([
        html.B("Full Stack Developer - Book your Books", style={"font-size": "large"}),
        html.P("Aug 2021 - Dec 2021", style={"color": "white"}),
        html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in pp2_desc]),
    ]),
    dbc.Row([
        html.B("Android Mobile Application Developer - Memo'PI'ze", style={"font-size": "large"}),
        html.P("May 2021 - Jul 2021", style={"color": "white"}),
        html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in pp3_desc])
    ])
])