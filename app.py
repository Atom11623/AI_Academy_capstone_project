from flask import Flask, render_template, request
import openai
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from getpass import getpass


app = Flask(__name__)


# Set your OpenAI API key
openai.api_key = "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"

def generate_book_recommendation(user_input):
    # User input for generating a lesson plan
    prompt = f"Could you please suggest a book for me to read based on my current mood or situation, and provide a summary along with the author's details:\n{user_input}\nBook recomendation:"

    # Generate response using GPT-3.5-turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",  # Use "gpt-3.5-turbo-16k" for GPT-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,  
        n=1,  
        stop=None, 
        temperature=0.7, 
    )

    # Extract the generated Book from the response
    Book_recomendation = response['choices'][0]['message']['content']

    return Book_recomendation


# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for processing user input
@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['user_input']
    
    # Generate the book recommendation
    book_recommendation = generate_book_recommendation(user_input)

    # Tokenize the book recommendation and count word frequencies
    tokens = book_recommendation.split()
    word_freq = Counter(tokens)

    # Generate a WordCloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

    # Save WordCloud to an image file (optional)
    wordcloud.to_file("static/wordcloud.png")

    return render_template('result.html', book_recommendation=book_recommendation)

if __name__ == '__main__':
    app.run(debug=True)
