from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from groq import Groq
from datetime import datetime
from flask_cors import CORS  # Import CORS

# Load the .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

# Initialize the Groq client with the API key
client = Groq(api_key=api_key)

# Initialize Flask app
app = Flask(__name__)

# Allow CORS for all domains (for development purposes)
CORS(app)

# Store chat history in memory
chat_history = []

# Home route to render chat interface
@app.route("/")
def home():
    return render_template("index.html")

# API endpoint for chat
@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        # Get the user input from the request
        data = request.json
        user_input = data.get("message", "")
        print(user_input)

        if not user_input:
            return jsonify({"status": "error", "message": "No input provided."}), 400

        # Generate a response using the Groq client
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "you are a helpful assistant. " + user_input + " give all the response in short form and in bullet points",
                }
            ],
            model="llama-3.3-70b-versatile",  # Ensure this model is correct
        )

        # Get the current timestamp
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Check if the response has valid choices and content
        if chat_completion and chat_completion.choices:
            response_content = chat_completion.choices[0].message.content

            # Split the response into bullet points
            response_list = response_content.split("\n")

            # Ensure that empty responses are not included
            response_list = [line.strip() for line in response_list if line.strip()]

            # Format the response for the front end

            print(response_list)
            formatted_response = {
                "status": "success",
                "response": response_list,  # Send the response as a list for bullet points
                "suggestions": ["Translate", "Ask a question", "Get help"],  # Example suggestions
            }

            # Add to chat history with date, user input, and bot response
            chat_history.append({'date': current_date, 'user': user_input, 'bot': response_content})
            print(chat_history)

            return jsonify(formatted_response)
        else:
            return jsonify({"status": "error", "message": "No valid response from the AI."}), 500

    except Exception as e:
        return jsonify({"status": "error", "message": f"An error occurred: {e}"}), 500


# API endpoint for getting chat history
@app.route("/api/history", methods=["GET"])
def history():
    return jsonify(chat_history)

# Run the Flask app
if __name__ == "__main__": 
    port = int(os.environ.get("PORT", 8000))  # Use environment variable for port
    app.run(host='0.0.0.0', port=port, debug=True)
