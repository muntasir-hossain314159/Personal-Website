import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, "/", title="Meet Me")

# Job Experience 1
job1_date = "June 2023 - Present"
job1_description = [
    "Implemented a failover mechanism for crucial plugins running in stores, reducing customer wait time by 12%",
    "Developed a utility application in .NET to streamline local testing of the POS, reducing development time by 20%",
    "Refactored legacy code in C/C++ to improve maintainability, robustness, and scalability",
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
            html.Img(src="./assets/images/profile.PNG", height="300px", style={"border-radius": "25px"}),
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
                html.Li(html.Div([html.B("Programming Languages/Library: "), "C, C++, C#, Java, Python, HTML, CSS, JavaScript, TypeScript, SQL"], style={"color": "white"})),
                html.Li(html.Div([html.B("Software/Framework: "), "Git, ReSharper, React, Next.js, EJS, Bootstrap, jQuery, Express, Node.js, MongoDB, Docker, Microsoft Azure"], style={"color": "white"})),
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
    ], className="mb-5")
])