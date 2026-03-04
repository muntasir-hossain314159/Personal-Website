import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, "/", title="Meet Me")

# Job Experience 1
job1_date = "May 2021 - Aug 2021"
job1_description = [
    "Worked with 5 engineers as part of the team to build 2 Mega-Watt hydrogen generators",
    "Integrated a centralized remote monitoring solution for hydrogen generators resulting in an 30% decrease in troubleshooting time",
    "Developed a dashboard in Grafana using complex SQL queries to organize and display collected data to stakeholders including customers, engineers, and sales personnel increasing their performance by 27%",
    "Tested software and verified results after configuration in collaboration with the principal electrical engineer"
]

# Job Experience 2
job2_date = "Jun 2022 - Aug 2022"
job2_description = [
    "Refactored and optimized source code, achieving a 15% decrease in POS startup time, directly enhancing crew experience and operational efficiency",
    "Documented a detailed function map encompassing all startup calls, streamlining future debugging and feature development, and reducing onboarding time for new developers by 20%",
    "Utilized ReSharper dotTrace to profile and analyze the POS startup process, identifying and resolving critical bottlenecks",
    "Worked in an Agile environment with a team of 5 software engineers on the Point-of-Sale (POS)",
    "Wrote test scripts as part of Test-Driven Development using OpenTest"
]

# Job Experience 3
job3_date = "July 2020 - Jan 2021"
job3_description = [
    "Developed the website for NLSM, a sports consulting agency, using WordPress and CSS",
    "Designed mobile and desktop responsive web interfaces that allowed over 30 players to join our program",
    "Managed development projects for multiple teams of the startup including web development, operations, & marketing resulting in a 10% increase in revenue"
]

# Job Experience 4
job4_date = "June 2023 - June 2025"
job4_description = [
    "Decoupled a centralized logging component from a legacy monolithic .NET application and re-architected it as a standalone, production-grade microservice.",
    "Implemented a high-throughput asynchronous logging pipeline using batching, retry strategies, and non-blocking I/O, reducing request latency by 25–30% while handling sustained high write volume.",
    "Designed and automated a fault-tolerant failover mechanism for critical backend services, reducing customer-visible downtime by 10% and improving service availability.",
    "Automated testing and debugging workflows by building an internal developer tool, reducing development iteration time by 20% and improving microservice reliability.",
    "Refactored and increased code coverage in legacy C/C++ code by 35%, reducing regressions and improving release confidence.",
    "Served as a mentor for 2 new incoming engineers, providing guidance on technical skills, onboarding processes, and project best practices to help them integrate into the team effectively.",
]

job5_date = "June 2025 - Present"
job5_description = [
    "Led backend architecture for a multi-store device management platform, enabling concurrent configuration updates across thousands of stores and reducing market-level workflows from hours to minutes.",
    "Designed and developed an event-driven backend using RabbitMQ, applying idempotent consumers and retry/backoff strategies to orchestrate asynchronous workflows across multiple microservices with 99.9% processing reliability.",
    "Implemented parallel execution to process dozens of stores simultaneously, reducing end-to-end latency by 70–85% compared to the prior sequential workflow.",
    "Re-architected a core backend feature, reducing execution time from ~3 hours with heavy IT support to under 2 minutes with zero IT involvement.",
    "Performed deep production incident triage and root-cause analysis across AWS-hosted microservices, using Kubernetes CPU and memory metrics to identify over-provisioned pods and right-size resource requests, improving service stability and overall cluster efficiency.",
    "Collaborated with cross-functional engineering teams to align backend designs, rollout strategies, and operational requirements across dependent services.",
    "Mentored two junior engineers, providing guidance on backend architecture, concurrency, and production-ready coding practices.",
    "Authored architecture diagrams and technical design documents detailing data flow, failure modes, and recovery strategies for distributed systems."
]


layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Hello, I am Muntasir Hossain"),
            html.P("I'm a Software Engineer II at McDonald's Corporation with 3 years of experience designing and implementing distributed, cloud-native backend systems at scale. Proven ability to develop reliable microservices, event-driven architectures, and asynchronous processing pipelines used in production environments. Experience includes decomposing monolithic systems into scalable microservices and operating distributed backend services in production environments. Strong foundation in data structures, algorithms, and system design; with end-to-end ownership of features from technical design and architecture to production release and on-call support.", style={"color": "white", "font-size": "large"}),
            html.Ul([
                html.Li(
                    html.A(
                        "Email",
                        href="mailto:muntasir.hoss@gmail.com",
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
        ], lg={'size': 6}, align="center"),
        dbc.Col(
            html.Img(src="./assets/images/profile.PNG", height="300px", style={"border-radius": "25px"}),
            lg={'size': 6},
            className="d-flex justify-content-center"),
    ], className='mt-5'),
    dbc.Row([
        html.H2('Summary of Qualifications'),
        html.Div(html.Ul([
            html.Li(html.Div([html.B("Backend & Systems: "), ".NET, RESTful APIs, Microservices, Distributed Systems, Asynchronous Processing, Event-Driven Architecture, Messaging Systems"], style={"color": "white"})),
            html.Li(html.Div([html.B("Programming Languages & Framework: "), "C#, Python, Go, TypeScript, JavaScript, SQL, Java, C++, React, Next.js, Node.js."], style={"color": "white"})),
            html.Li(html.Div([html.B("Data & Storage: "), "Postgres, Supabase, DynamoDB, MongoDB, Redis, Data Modeling, Database Migrations"], style={"color": "white"})),
            html.Li(html.Div([html.B("Cloud & DevOps: "), "AWS, Docker, Kubernetes, Terraform, GitHub Actions, Jenkins, RabbitMQ, JFrog Artifactory"], style={"color": "white"})),
            html.Li(html.Div([html.B("Quality & Collaboration: "), "Unit & Integration Testing, Automated Testing, Production Monitoring, Incident Response, On-call Support"], style={"color": "white"})),
            html.Li(html.Div([html.B("Algorithms & CS Fundamentals: "), "Data Structures (Arrays, Hash Maps, Trees, Graphs, Heap, Stack), Algorithms (Two Pointers, BFS/DFS, Sorting, Dynamic Programming, Greedy, Caching Strategies), Time & Space Complexity Analysis"], style={"color": "white"})),
        ]))
    ], className='mt-4'),
    dbc.Row(html.H2('Professional Experience'), className='mt-4'),
    dbc.Row([
            html.B("Software Engineer II at McDonald's Corporation", style={"font-size": "large"}),
            html.P(job5_date, style={"color": "white"}),
            html.Div(html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in job5_description])),

            html.B("Software Engineer I at McDonald's Corporation", style={"font-size": "large"}),
            html.P(job4_date, style={"color": "white"}),
            html.Div(html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in job4_description])),

            html.B("Software Engineer at Next Level Sports Management", style={"font-size": "large"}),
            html.P(job3_date, style={"color": "white"}),
            html.Div(html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in job3_description])),

            html.B("Software Engineering Intern at McDonald's Corporation", style={"font-size": "large"}),
            html.P(job2_date, style={"color": "white"}),
            html.Div(html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in job2_description])),

            html.B("Controls and Software Intern at Nel Hydrogen", style={"font-size": "large"}),
            html.P(job1_date, style={"color": "white"}),
            html.Div(html.Ul([html.Li(html.Div(desc, style={"color": "white"})) for desc in job1_description])),
    ], className="mb-5")
])