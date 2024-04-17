import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, "/projects", title="Projects")

# Personal Project 1
pp1_desc = "Developed a Social Media and Digital Reputation Management software application for Sentiment Analysis using Python. \
The system employs a client-server architecture, with communication facilitated via a RESTful API. \
The process begins with the user navigating to the dashboard's Home Page developed using Dash (Python framework for building analytical web application). \
The user then initiates a search by entering a keyword and submitting it. This action triggers an HTTP POST request \
transmitted to the Listener Module. Integrated with an Azure Functions HTTP Trigger, \
the Listener Module receives the request, forwarding the keyword to the Aggregator Module. \
The Aggregator Module, a pivotal component, queries and retrieves data related to the keyword \
from designated social media platforms like Twitter, Reddit, and Tumblr using their respective APIs. \
Once collected, the data is published to an Azure Service Bus Topic named General Cleaner, ensuring \
organized flow for subsequent cleaning. The Cleaner Module subscribes to this topic, retrieving data \
for a comprehensive cleaning process encompassing data preprocessing, tokenization, and lemmatization. \
Following cleaning, the data is sent to the Sentiment Analysis Module, which employs sentiment analysis \
engines like MTA, GCNLA, and IWNLU to assign numerical sentiment scores ranging from -1 to +1.\
The resulting sentiment analysis data is stored in a cloud-based MongoDB Atlas database \
for visualization and exploration in the SASM dashboard. "

pp2_desc = "Recreated the Wordle game using NextJS and integrated it with a Discord bot to allow users in my Discord server to guess words submitted by other members of the community. \
The Discord bot was built using Node.js and it was configured with slash commands to enable users to submit 5-letter words, which are subsequently \
stored in a MongoDB database. \
Additionally, the server executes a daily cron job to randomly select a word from the database and update the daily WordCord prompt. \
The application was built to enhance engagement within the community."

layout = dbc.Container([
    dbc.Row(html.H2('Personal Projects'), className='mt-4 mb-4 text-center'),
    dbc.Row([
        html.H3("Sentiment Analysis of Social Media (SASM)", style={"font-size": "large", "margin-bottom": "30px", "text-align": "center"}),
        html.Img(src="./assets/SASM.png", style={"border-radius": "25px", "width": "50%", "margin-bottom": "20px"}),
        html.P(pp1_desc, style={"color": "white"}),
    ], className="mb-4", justify="center"),
    dbc.Row([
        html.H3("WordCord", style={"font-size": "large", "margin-bottom": "30px", "text-align": "center"}),
        html.Img(src="./assets/WordCord.JPG", style={"border-radius": "25px", "width": "30%", "margin-bottom": "20px"}),
        html.P(pp2_desc, style={"color": "white"}),
    ], className="mb-4", justify="center"),
])