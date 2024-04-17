import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, "/awards", title="Awards")

layout = dbc.Container([
    dbc.Row(html.H2('Awards'), className='mt-4 mb-4 text-center'),
    dbc.Row([
        dbc.Col([
            html.B("Finalist at Hackillinois 2024", style={"font-size": "large"}),
            html.P("Feb 2024", style={"color": "white"}),
            html.Img(src="./assets/Hackillinois_Finalist.jpg", style={"border-radius": "25px", "width": "100%"}),
        ], lg={'size': 6}),
    ], justify='center', className='mb-4'),
    dbc.Row([
        dbc.Col([
            html.B("2nd Place at the Capstone Design Pitch Competition", style={"font-size": "large"}),
            html.P("May 2023", style={"color": "white"}),
            html.Img(src="./assets/Capstone_Pitch_Competition.jpg", style={"border-radius": "25px", "width": "100%"}),
        ], lg={'size': 6}),
    ], justify='center', className='mb-4'),
    dbc.Row([
        dbc.Col([
            html.B("Honors Program Recipient", style={"font-size": "large"}),
            html.P("May 2023", style={"color": "white"}),
            html.Img(src="./assets/Honors_Program.JPG", style={"border-radius": "25px", "width": "100%"}),
        ], lg={'size': 6}),
    ], justify='center', className='mb-4'),
    dbc.Row([
        dbc.Col([
            html.B("Outstanding Undergraduate Student in Computer Science Award", style={"font-size": "large"}),
            html.P("April 2023", style={"color": "white"}),
            html.Img(src="./assets/Outstanding_Undergraduate_Student_in_Computer_Science_Award.jpg", style={"border-radius": "25px", "width": "100%"}),
        ], lg={'size': 6}), 
    ], justify='center', className='mb-4'),
    dbc.Row([
        dbc.Col([    
            html.B("Outstanding Undergraduate Student Tutor Award", style={"font-size": "large"}),
            html.P("April 2023", style={"color": "white"}),
            html.Img(src="./assets/Undergraduate_Tutor_Award.jpg", style={"border-radius": "25px", "width": "100%"}),
        ], lg={'size': 6}),
    ], justify='center', className='mb-4'),
    dbc.Row([
        dbc.Col([
            html.B("Summer Undergraduate Research Fellow", style={"font-size": "large"}),
            html.P("August 2020", style={"color": "white"}),
            html.Img(src="./assets/SURF.JPG", style={"border-radius": "25px", "width": "100%"})
        ], lg={'size': 6}), 
    ], justify='center', className='mb-4')
])


#   dbc.Row([
#         dbc.Col([
#             html.B("Finalist at Hackillinois 2024", style={"font-size": "large"}),
#             html.P("Feb 2024", style={"color": "white"}),
#             html.Img(src="./assets/Hackillinois_Finalist.jpg", style={"border-radius": "25px", "width": "100%"}),
#         ], lg={'size': 6}, className='mb-4'),

#         dbc.Col([
#             html.B("2nd Place at the Capstone Design Pitch Competition", style={"font-size": "large"}),
#             html.P("May 2023", style={"color": "white"}),
#             html.Img(src="./assets/Capstone_Pitch_Competition.jpg", style={"border-radius": "25px", "width": "100%"}),
#         ], lg={'size': 6}, className='mb-4'),
#     ]),
#     dbc.Row([
#         dbc.Col([
#             html.B("Honors Program Recipient", style={"font-size": "large"}),
#             html.P("May 2023", style={"color": "white"}),
#             html.Img(src="./assets/Honors_Program.JPG", style={"border-radius": "25px", "width": "100%"}),
#         ], lg={'size': 6}, className='mb-4'),

#         dbc.Col([
#             html.B("Outstanding Undergraduate Student in Computer Science Award", style={"font-size": "large"}),
#             html.P("April 2023", style={"color": "white"}),
#             html.Img(src="./assets/Outstanding_Undergraduate_Student_in_Computer_Science_Award.jpg", style={"border-radius": "25px", "width": "100%"}),
#         ], lg={'size': 6}, className='mb-4'), 
#     ]),
#     dbc.Row([
#         dbc.Col([    
#             html.B("Outstanding Undergraduate Student Tutor Award", style={"font-size": "large"}),
#             html.P("April 2023", style={"color": "white"}),
#             html.Img(src="./assets/Undergraduate_Tutor_Award.jpg", style={"border-radius": "25px", "width": "100%"}),
#         ], lg={'size': 6}, className='mb-4'),

#         dbc.Col([
#             html.B("Summer Undergraduate Research Fellow", style={"font-size": "large"}),
#             html.P("August 2020", style={"color": "white"}),
#             html.Img(src="./assets/SURF.JPG", style={"border-radius": "25px", "width": "100%"})
#         ], lg={'size': 6}, className='mb-4'), 
#     ])