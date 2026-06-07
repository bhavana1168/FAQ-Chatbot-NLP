FAQ Chatbot Using NLP
Project Overview
This project is an intelligent FAQ Chatbot developed using Python, Flask, NLTK, and Scikit-learn. The chatbot is designed to answer frequently asked questions by processing user input and finding the most relevant response using Natural Language Processing (NLP) techniques.

Features
Interactive web-based chatbot interface
Natural Language Processing using NLTK
Text preprocessing and tokenization
Similarity-based response matching
User-friendly design
Fast and accurate FAQ retrieval
Technologies Used
Python
Flask
NLTK
Scikit-learn
HTML
CSS
JavaScript
Project Structure
faq_chatbot/

├── app.py

├── requirements.txt

├── README.md

├── templates/

│ └── index.html

├── static/

│ ├── style.css

│ └── script.js

└── faq_data.json

Installation
Clone the repository:
git clone 
https://github.com/bhavana1168/FAQ-Chatbot-NLP.git
Navigate to the project directory:
cd chatbot-for-FAQs

Install dependencies:
python -m pip install -r requirements.txt

Download NLTK resources:
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"

Run the application:
python app.py

Open your browser and visit:
http://127.0.0.1:5000

How It Works
User enters a question.
The chatbot preprocesses the text using NLP techniques.
The system compares the query with stored FAQ questions.
The most relevant answer is returned to the user.
Future Enhancements
Voice-based interaction
Database integration
Multi-language support
AI-powered response generation
Deployment on cloud platforms
Author
Bhavana pakide

License
This project is created for educational and internship purposes.
