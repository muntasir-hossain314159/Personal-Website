import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, "/publications", title="Publications")

# Research Publication 1
rp1_date = "Aug 2022 - May 2023"
rp1_desc = ["Poster Presentation in 2023 Consortium for Computing Sciences in Colleges Northeastern Conference (CCSCNE)",
            "Proposed, designed, developed, integrated, and evaluated a conversational agent prototype to serve as a smart electronic liaison for international students and service offices at the University of New Haven.",
            "Worked closely with the University Immigration Services and Center for Learning Resources at the University of New Haven to analyze requirements, design the software, develop the software, collect data, and train the chatbot.",
            "Video Demonstration"]

# Research Publication 2
rp2_date = "May 2022 - May 2023"
rp2_desc = ["Poster Presentation in 2023 IEEE High Performance Extreme Computing Virtual Conference (HPEC)",
            "Poster Presentation in 2023 Consortium for Computing Sciences in Colleges Northeastern Conference (CCSCNE)",
            "Designed, developed, and integrated an open-source, multi-channel, multi-engine sentiment analysis software for social media and digital reputation management purposes",
            "Conducted a case study focusing on three major information technology companies: Google, Amazon, and Microsoft, to explore how social media content about major information technology companies vary depending on various factors including geo-political, socio-economic, and environmental awareness.",
            "Video Demonstration"]

# Research Publication 3
rp3_date = "Feb 2021 - Jul 2021"
rp3_desc = ['Published in 2021 International Conference on Engineering and Emerging Technologies (ICEET)',
            'Verified and validated the design and architecture of the solution by presenting an online reputation management case study of three COVID-19 vaccines; Pfizer-BioNTech, Oxford-AstraZeneca, and Johnson & Johnson']

# Research Publication 4
rp4_date = "Mar 2020 - Apr 2020"
rp4_desc = ['Published in 2021 IEEE Frontiers in Education Conference (FIE)',
            'Analyzed pre and post-event surveys collected during several faculty training sessions on using the makerspace',
            'Reviewed post-event survey data from one of the faculty training sessions',
            'Compiled key findings related to maker ability, intended plans, and concerns',
            'Created bar charts and graphs in Excel to display certain data',
            'Implemented the qualitative data analysis technique of thematic coding to determine common themes in written free-response answers']

layout = dbc.Container([
    dbc.Row(html.H2('Poster Presentation & Publications'), className='mt-4 mb-4 text-center'),
    dbc.Row([
        html.Div([
            html.A(
                html.B("A Novel Smart Electronic Liaison to Support International Students"),
                style={"font-size": "large"}
            ),
            html.P(rp1_date, style={"color": "white"}),
            html.Ul([
                html.Li(
                    html.Div(
                        html.A(desc, href="https://ccscne.org/2023/CCSCNE%202023%20Student%20Posters.pdf", style={"color": "white"}) if i == 0
                        else html.A(desc, href="https://www.youtube.com/watch?v=ReZLdYSXtk0", style={"color": "white"}) if i == 3
                        else desc, style={"color": "white"})
                ) for i, desc in enumerate(rp1_desc)]),
            ], className='experience-section')
    ]),
    dbc.Row([
        html.Div([
            html.A(
                html.B("Application of Natural Language Processing Techniques for Sentiment Analysis of Social Media Content"),
                style={"font-size": "large"}
            ),
            html.P(rp2_date, style={"color": "white"}),
            html.Ul([
                html.Li(
                    html.Div(
                        html.A(desc, href="https://ieee-hpec.org/wp-content/uploads/2023/09/40.pdf", style={"color": "white"}) if i == 0
                        else html.A(desc, href="https://ccscne.org/2023/CCSCNE%202023%20Student%20Posters.pdf", style={"color": "white"}) if i == 1
                        else html.A(desc, href="https://vimeo.com/815209925?share=copy", style={"color": "white"}) if i == 4
                        else desc, style={"color": "white"})
                ) for i, desc in enumerate(rp2_desc)]),
            ], className='experience-section')
    ]),
    dbc.Row([
        html.Div([
            html.A(
                html.B("Online Social Network Interactions (OSNI): A Novel Online Reputation Management Solution"),
                style={"font-size": "large"}
            ),
            html.P(rp3_date, style={"color": "white"}),
            html.Ul([html.Li(html.Div(
                html.A(desc, href="https://ieeexplore.ieee.org/document/9659615", style={"color": "white"}) if i == 0
                else desc, style={"color": "white"})) for i, desc in enumerate(rp3_desc)]),
            ], className='experience-section')
    ]),
    dbc.Row([
        html.Div([
            html.A(
                html.B("Integrating Makerspaces into the Curriculum - Faculty Development Efforts"),
                style={"font-size": "large"}
            ),
            html.P(rp4_date, style={"color": "white"}),
            html.Ul([html.Li(html.Div(
                html.A(desc, href="https://ieeexplore.ieee.org/document/9637230", style={"color": "white"}) if i == 0
                else desc, style={"color": "white"})) for i, desc in enumerate(rp4_desc)]),
            ], className='experience-section')
    ])
])