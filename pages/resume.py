import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, "/publications-projects", title="Meet Me")

# Job Experience 1
job1_date = "June 2023 - Present"
job1_description = [
    "Led and executed an initiative to implement a failover mechanism in stores, ensuring uninterrupted functionality",
    "Developed a utility application in .NET (C#) to streamline local testing of the POS, resulting in a reduced development time of 20%",
    "Refactored and documented legacy code in C/C++ to improve maintainability, robustness, and scalability",
    "Created clear, concise, and complete documentation for 3 initiatives",
    "Led 20+ Agile ceremonies, including daily standup, sprint planning, retrospectives, and backlog refinement"
]

# Job Experience 2
job2_date = "Jun 2022 - Aug 2022"
job2_description = [
    "Worked in an Agile environment with a team of 5 software engineers on the Point-of-Sale (POS)",
    "Wrote test scripts as part of Test-Driven Development using OpenTest",
    "Profiled the POS Startup process using ReSharper dotTrace to identify bottlenecks",
    "Documented and created a function map detailing all the functions being called during startup",
    "Optimized the source code and reduced startup time by 15.2%"
]

# Job Experience 3
job3_date = "May 2021 - Aug 2021"
job3_description = [
    "Worked with 5 engineers as part of the team to build 2 Mega-Watt hydrogen generators",
    "Integrated a centralized remote monitoring solution for hydrogen generators resulting in an 80% decrease in troubleshooting time",
    "Developed a dashboard in Grafana using complex SQL queries to organize and display collected data for stakeholders including customers, engineers, and sales personnel increasing their performance by 50%",
    "Tested software and verified results after configuration in collaboration with the principal electrical engineer"
]

# Job Experience 4
job4_date = "Nov 2020 - Jan 2021"
job4_description = [
    "Developed the website for NLSM, a sports consulting agency, using WordPress and CSS",
    "Designed mobile and desktop responsive web interfaces that allowed over 30 players to join our program",
    "Managed development projects for multiple teams of the startup including web development, operations, & marketing resulting in a 25% increase in revenue"
]

# Research Publication 1
rp1_date = "Aug 2022 - May 2023"
rp1_desc = ["Poster Presentation in 2023 Consortium for Computing Sciences in Colleges Northeastern Conference (CCSCNE)",
            "Proposed, designed, developed, integrated, and evaluated a conversational agent prototype to serve as a smart electronic liaison for international students and service offices at the University of New Haven.",
            "Worked closely with the University Immigration Services and Center for Learning Resources at the University of New Haven to analyze requirements, design the software, develop the software, collect data, and train the chatbot."]

# Research Publication 2
rp2_date = "May 2022 - May 2023"
rp2_desc = ["Poster Presentation in 2023 IEEE High Performance Extreme Computing Virtual Conference (HPEC)",
            "Poster Presentation in 2023 Consortium for Computing Sciences in Colleges Northeastern Conference (CCSCNE)",
            "Designed, developed, and integrated an open-source, multi-channel, multi-engine sentiment analysis software for social media and digital reputation management purposes",
            "Conducted a case study focusing on three major information technology companies: Google, Amazon, and Microsoft, to explore how social media content about major information technology companies vary depending on various factors including geo-political, socio-economic, and environmental awareness."]

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
    dbc.Row([
        dbc.Col([
            html.H1("Hello, I am Muntasir Hossain"),
            html.P("A software engineer based in Chicago, IL. I'm interested in Software Engineering, Natural Language Processing (AI), Mobile/Web Application Development, and Mathematics.", style={"color": "white", "font-size": "large"}),
            html.Ul([
                html.Li(
                    html.A(
                        "Email",
                        href="mailto:ahoss1@unh.newhaven.edu",
                        style={"color": "white", "font-size": "large"}
                    ),
                ),
                html.Li(
                    html.A(
                        "GitHub",
                        href="https://github.com/muntasir-hossain314159",
                        style={"color": "white", "font-size": "large"}
                    ),
                ),
                html.Li(
                    html.A(
                        "LinkedIn",
                        href="https://www.linkedin.com/in/muntasirhossain314/",
                        style={"color": "white", "font-size": "large"}
                    ),
                ),
            ])
        ], lg={'size': 6}, align="center", className="mb-4"),
        dbc.Col(
            html.Img(src="./assets/profile.PNG", height="300px", style={"border-radius": "25px"}),
            lg={'size': 6},
            className="d-flex justify-content-center"),
    ], className='mt-5'),
    dbc.Row([
        dbc.Col([
            html.H2('About Me'),
            html.Div([
                html.P("I am currently working as a Software Development Engineer at McDonald's Corporate under the POS team. My passion for technology and problem-solving led me to pursue a major in Computer Science and a minor in Mathematics at the University of New Haven, where I graduated with a Bachelor's degree in May 2023.", style={"color": "white"}),
                html.P("Working in such an exciting and fast-paced environment has allowed me to enhance my skills and knowledge, and I'm excited to continue exploring new opportunities and challenges in the field of technology. In my free time, I enjoy reading about the latest advancements in technology, as well as hiking and exploring the outdoors.", style={"color": "white"}),
            ])],
            lg={'size': 6}
        ),
        dbc.Col([
            html.H2('Summary of Qualifications'),
            html.P("During my time in college and industry, I developed a deep understanding of programming languages and software development methodologies:", style={"color": "white"}),
            html.Ul([
                html.Li(html.Div([html.B("Skills: "), "Software Development, QE Testing, Performance Profile Analysis, Agile Methodologies, Mobile Application Development, Web Development, RESTful API Design, Database Management Systems, Machine Learning, Data Analysis, Scientific Research, Communication, Project Management"], style={"color": "white"})),
                html.Li(html.Div([html.B("Programming Languages/Library: "), "C, C++, C#, .NET Core, Java, Python, SQL, HTML, CSS, JavaScript, Swift"], style={"color": "white"})),
                html.Li(html.Div([html.B("Software/Framework: "), "Git, ReSharper, EJS, Bootstrap, jQuery, Express, Node.js, MongoDB, Microsoft Azure, Docker"], style={"color": "white"})),
            ])],
            lg={'size': 6}
        )
    ], className='mt-5'),
    dbc.Row(html.H2('Professional Experience'), className='mt-4'),
    dbc.Row([
        dbc.Col([
             html.Div([
                html.B("Software Development Engineer I at McDonald's Corporation", style={"font-size": "large"}),
                html.P(job1_date, style={"color": "white"}),
                html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in job1_description]),
                html.B("Software Engineering Intern at McDonald's Corporation", style={"font-size": "large"}),
                html.P(job2_date, style={"color": "white"}),
                html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in job2_description]),
            ], className='experience-section')
        ], lg={'size': 6}),
        dbc.Col([
             html.Div([
                 html.B("Controls and Software Intern at Nel Hydrogen", style={"font-size": "large"}),
                html.P(job3_date, style={"color": "white"}),
                html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in job3_description]),
                html.B("Software Engineering Intern at Next Level Sports Management", style={"font-size": "large"}),
                html.P(job4_date, style={"color": "white"}),
                html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in job4_description])
            ], className='experience-section')
        ], lg={'size': 6})
    ]),
    dbc.Row(html.H2('Poster Presentation & Publications'), className='mt-4'),
    dbc.Row([
        dbc.Col([
             html.Div([
                html.A(
                    html.B("A Novel Smart Electronic Liaison to Support International Students"),
                    href="https://www.youtube.com/watch?v=ReZLdYSXtk0",
                    style={"font-size": "large"}
                ),
                html.P(rp1_date, style={"color": "white"}),
                html.Ul([
                    html.Li(
                        html.Div(
                            html.A(desc, href="https://ccscne.org/2023/CCSCNE%202023%20Student%20Posters.pdf", style={"color": "white"}) if i == 0
                            else desc, style={"color": "white"})
                    ) for i, desc in enumerate(rp1_desc)]),
                html.A(
                    html.B("Application of Natural Language Processing Techniques for Sentiment Analysis of Social Media Content"),
                    href="https://vimeo.com/815209925?share=copy",
                    style={"font-size": "large"}
                ),
                html.P(rp2_date, style={"color": "white"}),
                html.Ul([
                    html.Li(
                        html.Div(
                            html.A(desc, href="https://ieee-hpec.org/wp-content/uploads/2023/09/40.pdf", style={"color": "white"}) if i == 0
                            else html.A(desc, href="https://ccscne.org/2023/CCSCNE%202023%20Student%20Posters.pdf", style={"color": "white"}) if i == 1
                            else desc, style={"color": "white"})
                    ) for i, desc in enumerate(rp2_desc)]),
            ], className='experience-section')
        ], lg={'size': 6}),
        dbc.Col([
             html.Div([
                html.A(
                    html.B("Online Social Network Interactions (OSNI): A Novel Online Reputation Management Solution"),
                    href="https://ieeexplore.ieee.org/document/9659615",
                    style={"font-size": "large"}
                ),
                html.P(rp3_date, style={"color": "white"}),
                html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in rp3_desc]),
                html.A(
                    html.B("Integrating Makerspaces into the Curriculum - Faculty Development Efforts"),
                    href="https://ieeexplore.ieee.org/document/9637230",
                    style={"font-size": "large"}
                ),
                html.P(rp4_date, style={"color": "white"}),
                html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in rp4_desc]),
            ], className='experience-section')
        ], lg={'size': 6})
    ]),
    dbc.Row(html.H2('Personal Projects'), className='mt-4'),
    dbc.Row([
        dbc.Col([
             html.Div([
                html.B("iOS Mobile Application Development", style={"font-size": "large"}),
                html.P("Jan 2022 - May 2022", style={"color": "white"}),
                html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in pp1_desc]),
                html.B("Full Stack Developer - Book your Books", style={"font-size": "large"}),
                html.P("Aug 2021 - Dec 2021", style={"color": "white"}),
                html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in pp2_desc]),
            ], className='experience-section')
        ], lg={'size': 6}),
        dbc.Col([
             html.Div([
                html.B("Android Mobile Application Developer - Memo'PI'ze", style={"font-size": "large"}),
                html.P("May 2021 - Jul 2021", style={"color": "white"}),
                html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in pp3_desc])
            ], className='experience-section')
        ], lg={'size': 6})
    ]),
    dbc.Row(html.H2('Awards'), className='mt-4'),
    dbc.Row([
        dbc.Col([
             html.Div([
                html.B("Finalist at Hackillinois 2024", style={"font-size": "large"}),
                html.P("Feb 2024", style={"color": "white"}),
                html.B("2nd Place at the Capstone Design Pitch Competition", style={"font-size": "large"}),
                html.P("May 2023", style={"color": "white"}),
                html.B("Honors Program", style={"font-size": "large"}),
                html.P("May 2023", style={"color": "white"}),
            ], className='experience-section')
        ], lg={'size': 6}),
        dbc.Col([
             html.Div([
                html.B("Outstanding Undergraduate Student Tutor Award", style={"font-size": "large"}),
                html.P("April 2023", style={"color": "white"}),
                html.B("Outstanding Undergraduate Student in Computer Science Award", style={"font-size": "large"}),
                html.P("April 2023", style={"color": "white"}),
                html.B("Summer Undergraduate Research Fellow", style={"font-size": "large"}),
                html.P("August 2020", style={"color": "white"}),
            ], className='experience-section')
        ], lg={'size': 6})
    ]),
])