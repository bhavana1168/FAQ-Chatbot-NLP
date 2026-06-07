from flask import Flask, render_template, request, jsonify
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load FAQ data
with open("faqs.json", "r") as file:
    faqs = json.load(file)

# Extract questions and answers
questions = [faq["question"] for faq in faqs]
answers = [faq["answer"] for faq in faqs]

# Convert questions into vectors
vectorizer = TfidfVectorizer(stop_words='english')
question_vectors = vectorizer.fit_transform(questions)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_answer", methods=["POST"])
def get_answer():

    user_input = request.json["question"]

    # Greeting responses
    greetings = ["hello", "hi", "hey", "good morning", "good evening"]

    if user_input.lower() in greetings:
        return jsonify({
            "answer": "Hello! How can I help you today?"
        })

    # Convert user input into vector
    user_vector = vectorizer.transform([user_input])

    # Calculate similarity
    similarity = cosine_similarity(user_vector, question_vectors)

    # Find best match
    best_match_index = similarity.argmax()
    best_score = similarity[0][best_match_index]

    # Check similarity score
    if best_score > 0.1:
        answer = answers[best_match_index]
    else:
        answer = "Sorry, I couldn't understand your question."

    return jsonify({
        "answer": answer
    })

if __name__ == "__main__":
    app.run(debug=True)