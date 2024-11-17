import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, "/projects", title="Projects")

pp1_desc = "Developed Deep, an application that helps people connect with strangers through meaningful prompts and encourages genuine in-person conversations. With Deep, users can create events to meet new people, share personal stories by responding to thoughtful prompts, and invite those who resonate with their posts to join them at events for authentic discussions. The platform fosters vulnerability and openness, using prompts as conversation starters to break the ice and build real connections. \
The web application was built using a Next.js React frontend, and deployed using Vercel. The client communicates via RESTful APIs with a .NET server written in C#. The server is running in a containerized environment on an AWS EC2 instance. For data storage, the application integrates with a PostgreSQL database powered by Supabase, and notifications, as seen above, are efficiently managed using Knock."

pp2_desc = "Developed a social media and digital reputation management software application for Sentiment Analysis using Python. \
The system employs a client-server architecture, with communication facilitated via a RESTful API. \
The process begins with the user navigating to the dashboard's home page developed using Dash (Python framework for building analytical web application). \
The user then initiates a search by entering a keyword and submitting it. This action triggers an HTTP POST request \
which is transmitted to the Listener Module. Integrated with an Azure Functions HTTP Trigger, \
the Listener Module receives the request, forwarding the keyword to the Aggregator Module. \
The Aggregator Module, a pivotal component, queries and retrieves data related to the keyword \
from the following social media platforms: Twitter, Reddit, and Tumblr using their respective APIs. \
Once collected, the data is published to an Azure Service Bus Topic, ensuring \
organized flow for subsequent cleaning. The Cleaner Module subscribes to this topic, retrieving data \
for a comprehensive cleaning process involving data preprocessing, tokenization, and lemmatization. \
Following cleaning, the data is sent to the Sentiment Analysis Module, which employs sentiment analysis \
engines like Microsoft Text Analytics, Google Cloud Natural Language API, and IBM Watson Natural Language Understanding to assign numerical sentiment scores ranging from -1 to +1. \
The resulting sentiment analysis data is stored in a cloud-based MongoDB Atlas database \
and then displayed in the SASM dashboard. "

pp3_desc = "Developed Day2Day - an AI driven budgeting web app for students and new graduates. \
The aim was to answer the fundamental question: 'How much should I allocate for spending and \
savings each day to meet my financial goals?' Leveraging Plaid, our system connects to users' bank accounts to gather transactional data. \
This data, along with the user inputted monthly saving goal, is analyzed by an AI model to determine spending patterns and provide personalized recommendations for daily spending and saving targets. \
The Node.js backend integrated with Plaid and OpenAI allows the application to collect relevant transactional data and generate financial insights. \
Utilizing the data and insights, a user-friendly interface constructed with Next.js displays intuitive graphs depicting spending by category and weekly spending predictions."

pp4_desc = "Recreated the Wordle game using Next.js and integrated it with a Discord bot to allow users in a Discord server to guess words submitted by other members of the community. \
The Discord bot was built using Node.js, and it was configured with slash commands to enable users to submit 5-letter words which are subsequently \
stored in a MongoDB database. \
The server then executes a daily Cron job to randomly select a word from the database and update the daily WordCord prompt. \
The application was built to enhance engagement within my Discord community."

layout = dbc.Container([
    dbc.Row(html.H1('Projects'), className='mt-4 mb-4 text-center'),
    dbc.Row([
        html.H2("Deep", style={"margin-bottom": "30px", "text-align": "center"}),
        html.Img(src="./assets/images/Deep_Landing_Page.PNG", style={"width": "50%", "margin-bottom": "20px"}),
        html.Img(src="./assets/images/Deep_Home_Page.PNG", style={"width": "50%", "margin-bottom": "20px"}),
        html.Img(src="./assets/images/Deep_Profile_Page.PNG", style={"width": "50%", "margin-bottom": "20px"}),
        html.Img(src="./assets/images/Deep_Add_Edit_Prompt_Page.PNG", style={"width": "50%", "margin-bottom": "20px"}),
        html.P(pp1_desc, style={"color": "white"}),
        html.A("Web Application Link", href="https://deep-mu.vercel.app/", style={"color": "white"}),

    ], className="mb-4", justify="center"),
    dbc.Row([
        html.H2("Sentiment Analysis of Social Media (SASM)", style={"margin-bottom": "30px", "text-align": "center"}),
        html.Iframe(src="https://player.vimeo.com/video/815209925?title=0&amp;byline=0&amp;portrait=0&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479", style={"width": "50%", "margin-bottom": "20px"}),
        html.Img(src="./assets/images/SASM_Architecture.png", style={"width": "50%", "margin-bottom": "20px"}),
        html.P(pp2_desc, style={"color": "white"}),
        html.A("Private Github Repository", href="mailto:muntasir.hoss@gmail.com", style={"color": "white"}),

    ], className="mb-4", justify="center"),
    dbc.Row([
        html.H2("Day2Day", style={"margin-bottom": "30px", "text-align": "center"}),
        html.Img(src="./assets/images/Day2Day_Dashboard.PNG", style={"width": "50%", "margin-bottom": "20px"}),
        html.Img(src="./assets/images/Day2Day_Plaid.PNG", style={"width": "50%","margin-bottom": "20px"}),
        html.P(pp3_desc, style={"color": "white"}),
        html.A("Github Repository", href="https://github.com/muntasir-hossain314159/hackillinois-repository", style={"color": "white"}),
    ], className="mb-4", justify="center"),
    dbc.Row([
        html.H2("WordCord", style={"margin-bottom": "30px", "text-align": "center"}),
        html.Img(src="./assets/images/WordCord_UI.JPG", style={"width": "40%", "margin-bottom": "20px"}),
        dbc.Col([
            html.Img(src="./assets/images/Discord_Bot.JPG", style={"width": "100%", "height": "40%", "padding-bottom": "20px"}),
            html.Img(src="./assets/images/WordCord_Database.JPG", style={"width": "100%", "height": "60%"}),
        ], className="mb-4"),
        
        html.P(pp4_desc, style={"color": "white"}),
        html.A("Github Repository", href="https://github.com/muntasir-hossain314159/WordCord", style={"color": "white"}),
    ], className="mb-4", justify="center"),

 
])