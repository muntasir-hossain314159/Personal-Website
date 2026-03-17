import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, "/", title="Meet Me")

# Job Experience 1
job1_date = "May 2021 - Aug 2021"
job1_description = [
    "Worked with 5 engineers as part of the team to build 2 Mega-Watt hydrogen generators.",
    "Integrated a centralized remote monitoring solution for hydrogen generators resulting in an 30% decrease in troubleshooting time.",
    "Developed a dashboard in Grafana using complex SQL queries to organize and display collected data to stakeholders including customers, engineers, and sales personnel increasing their performance by 27%.",
    "Tested software and verified results after configuration in collaboration with the principal electrical engineer."
]

# Job Experience 2
job2_date = "Jun 2022 - Aug 2022"
job2_description = [
    "Reduced Point-of-Sale startup time by ~15% by identifying algorithmic and I/O bottlenecks in backend initialization flows and optimizing critical execution paths.",
    "Decreased new-engineer onboarding time by 20% by documenting backend architecture and operational workflows.",
    "Utilized ReSharper dotTrace to profile and analyze the POS startup process, identifying and resolving critical bottlenecks.",
    "Worked in an Agile environment with a team of 5 software engineers on the Point-of-Sale (POS).",
]

# Job Experience 3
job3_date = "July 2020 - Jan 2021"
job3_description = [
    "Increased quarterly platform revenue by 10% as measured by transaction volume, by integrating scheduling and payment systems and coordinating cross-functional development."  
    "Reduced athlete onboarding time by 40% as measured by registration completion, by developing and deploying a responsive web application."
]

# Job Experience 4
job4_date = "June 2023 - June 2025"
job4_description = [
    "Improved scalability and fault isolation by decoupling a centralized logging component from a monolithic application and re-architecting it as a standalone production microservice.",  
    "Reduced request latency by 25–30% under sustained high write volume by building a high-throughput asynchronous logging pipeline using batching, non-blocking I/O, and retry strategies.",  
    "Decreased development iteration time by 20% by building internal tooling to automate testing and debugging workflows, improving overall service reliability.",
    "Reduced customer-visible downtime by 10% by designing and automating a fault-tolerant failover mechanism for critical backend services.",
    "Increased unit and integration test coverage by 35% by integrating comprehensive test execution into the CI pipeline, improving release stability and developer confidence."
]

job5_date = "June 2025 - Present"
job5_description = [
    "Enabled concurrent device configuration updates across 30,000 stores, reducing market-level workflows from hours to minutes, by architecting a distributed backend platform with parallel execution and fault-tolerant coordination.",
    "Achieved 99.9% message processing reliability by designing and developing an event-driven microservices system using RabbitMQ, with idempotent consumers and retry/backoff strategies to handle partial failures.",
    "Reduced end-to-end processing latency by 70–85% by introducing workload partitioning and concurrency-safe execution, replacing a previously sequential system.",
    "Cut execution time of a critical backend workflow from ~3 hours to under 2 minutes, eliminating manual IT involvement, by re-architecting the system into a fully automated, self-service pipeline.",
    "Improved system stability and infrastructure efficiency by performing production incident triage and root-cause analysis in AWS, analyzing Kubernetes CPU, memory, and throughput metrics to identify bottlenecks and right-size resources.",
    "Reduced AWS infrastructure footprint by eliminating redundant SQS and Lambda resources across 12 environments, consolidating message processing onto an existing RabbitMQ consumer and simplifying operational overhead.",
    "Led architectural design discussions and reviews for distributed services, authoring technical design documents that detailed data flow, failure modes, and recovery strategies, improving on-call effectiveness and reducing time to recovery during incidents.",
    "Collaborated with product managers, designers, and engineers to align backend designs, rollout strategies, and operational requirements across dependent services, enabling smoother releases and decreasing integration issues.",
    "Mentored two junior engineers through code reviews, design discussions, and production-readiness best practices, supporting their technical growth and onboarding."
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
            html.Li(html.Div([html.B("Cloud & DevOps: "), "AWS, Docker, Kubernetes, Terraform Helm, GitHub Actions, Jenkins, RabbitMQ, JFrog Artifactory"], style={"color": "white"})),
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