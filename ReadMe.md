Project Title: Book Recommendation Web App
Overview
This project is a web application that generates book recommendations based on user input regarding their current mood or situation. 
The recommendation is generated using OpenAI's GPT-3.5-turbo model, and it includes a summary along with the author's details. 
The application also displays a WordCloud visualizing the word frequencies in the generated book recommendation.

Project Structure
app.py: The main Flask application file.
templates: Contains HTML templates for the web application.
index.html: Home page template.
result.html: Result page template.
static: Static files (e.g., wordcloud images) generated by the application.

Dependencies
Flask: Web framework for building the application.
OpenAI: API for generating book recommendations using GPT-3.5-turbo.
WordCloud: Library for creating WordCloud visualizations.
Matplotlib: Library for plotting charts.

