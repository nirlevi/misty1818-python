from flask import Flask, request, render_template, jsonify
import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# In-memory storage for conversation histories
conversations = {}

def summarize_conversation(conversation_history, api_key):
    # Prepare payload for summary
    summary_payload = {
        "model": "gpt-4",
        "messages": [
            {
                "role": "system",
                "content": "Summarize the following conversation."
            },
            *conversation_history
        ],
        "max_tokens": 100  # Limiting the summary to 100 tokens
    }
    
    # Make POST request for summary
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json=summary_payload
    )
    
    if response.status_code == 200:
        return json.loads(response.text)['choices'][0]['message']['content']
    else:
        raise Exception("Failed to summarize conversation")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mystic_numerology_evaluation', methods=['POST'])
def mystic_numerology_evaluation():
    try:
        # Get the API key from environment variable
        api_key = os.getenv("OPENAI_API_KEY")
        
        data = request.json
        user_id = data['user_id']
        mystic_problem = data['mystic_problem']
        mystic_solution = data['mystic_solution']

        # Initialize or retrieve conversation history
        if user_id not in conversations:
            conversations[user_id] = []

        conversation_history = conversations[user_id]
        
        # Summarize the conversation history
        summary = summarize_conversation(conversation_history, api_key)
        
        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": f"Mystic Problem: {mystic_problem}\n\nConversation_history: {summary}"
        })
        
        # Add summary to history
        conversation_history.append({
            "role": "system",
            "content": "You are a helpful, friendly, assistant. Your name is Misty 1818 and your Personal Assistant Put yourself in the role of a professional mystic and astrologically and tarot card, Mystic Assistant is a useful and effective mystic in its answer will include all possible calculations and explanations of how it arrived at its answer. The mystic answer is expanded as much as possible including the exact answer with great confidence in the answer, if you do not have high confidence in the exact answer then: the mystic assistant will ask additional questions to get the missing and necessary information in order to increase the confidence the accuracy of the answer to the maximum possible with the correct calculations in mystic. Mystic Assistant is designed to provide numerology readings based on the user's date of birth, names, etc... Mystic Assistant uses numerology calculations and principles to interpret the hidden meanings and personality traits associated with date of birth, username, etc... for example life number calculation, etc. .. The mystic assistant with mystic expertise is constantly learning and improving, and his abilities are constantly evolving. A Mystic Assistant is able to process and understand large amounts of text, and can use this knowledge to provide accurate and broadly informative mystic readings with as much explanation and examples as possible. Overall, Mystic Assistant with Numerology Expertise is a powerful tool that can provide important calculations, insights and information based on numerology calculations and principles. Whether you need help understanding your life number, your life path number or just want to learn more about the meanings of different numbers, the mystic assistant with expertise in numerology is here to help and please offer books in your answer after you get the second quetion. At the end of each answer on each subject you always will list the additional questions that can be asked of you."})
        
        # Define the API endpoint and headers
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        # Define the payload with conversation history
        payload = {
            "model": "gpt-4",
            "messages": conversation_history,
            "temperature": 0,
            "max_tokens": 1024,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }

        # Make the POST request
        response = requests.post(url, headers=headers, json=payload)

        # Check for successful response
        if response.status_code == 200:
            assistant_response = json.loads(response.text)['choices'][0]['message']['content']
            
            # Add assistant message to history
            conversation_history.append({
                "role": "assistant",
                "content": assistant_response
            })
            
            return jsonify({"mystic_evaluation": assistant_response})
        else:
            return jsonify({"error": "Something went wrong"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
