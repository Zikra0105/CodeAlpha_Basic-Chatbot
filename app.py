from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random
import spacy 

nlp = spacy.load("en_core_web_sm") 

app = Flask(__name__)
CORS(app)

# Your responses dictionary and chatbot_response() stay unchanged

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():

    if request.method == "OPTIONS":
        # Handle preflight request for CORS
        return jsonify({"message": "CORS preflight response"}), 200

    data = request.json
    user_message = data.get("message", "")
    return jsonify({"response": chatbot_response(user_message)})

responses = {
   "hello": ["Hi there!", "Hello! How can I assist you?"],
    "hii": ["Hello! How can I help you today?"],
    "how are you": ["I'm just a bot, but I'm doing great! How about you?"],
    "goodbye": ["Goodbye! Take care!", "See you later!"],
    "help": ["I'm here to help! What do you need assistance with?"],
    "bye": ["Goodbye! Have a great day!", "See you later!"],
    "thanks": ["You're welcome!", "Happy to help!"],
    "weather": ["I'm not a weather bot, but you can check weather.com!"],
    "name": ["I'm your friendly chatbot.", "I don't have a name yet!"],
    "joke": ["Why don't scientists trust atoms? Because they make up everything!","Why did the computer go to therapy? Because it had too many bytes of emotional baggage!"],
    "one more joke": ["How does a penguin build its house? Igloos it together."],
    "creator": ["I was built by a developer using Python and Flask."],
    "age": ["I was created recently — I'm pretty new!"],
    "purpose": ["I'm here to chat and help you with information or just pass time."],
    "bored": ["Want to hear a joke?", "Let's chat! Ask me anything."],
    "who are you": ["I'm your friendly chatbot built to chat and have fun!"],
    "i am sad": ["I'm here for you. Want to talk about it?", "Sending positive vibes your way!"],
    "tell me something": ["Did you know? Honey never spoils!", "Octopuses have three hearts!"],
    "good morning": ["Good morning! Hope you have a fantastic day!", "Rise and shine!"],
    "good night": ["Sweet dreams!", "Good night! Talk to you later."],
    "okay": ["Got it!", "Alright!", "Cool!"],
    "cool": ["Thanks!", "I know, right? 😎"],
    "lol": ["Glad I made you laugh!", "😂 That's the spirit!"],
    "you're funny": ["Thanks! I try my best!", "I'm flattered!"],
    "i'm tired": ["Get some rest. You deserve it!", "Rest is important! Take a break if you need it."]
}

def chatbot_response(message):
    message = message.lower()
    doc = nlp(message) 

    for token in doc:
        if token.lemma_ in responses:
            return random.choice(responses[token.lemma_])
        
    for key in responses:
        if key in message:
            return random.choice(responses[key])
    return "I'm not sure, but I'm learning more every day!"





if __name__ == "__main__":
    app.run(debug=True)