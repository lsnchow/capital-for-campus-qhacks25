import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import random


#getting api key
load_dotenv()
API_KEY = os.getenv('API_KEY')



#creating the client
client = OpenAI(
    api_key=API_KEY
)




#initializing flask
app = Flask(__name__)
CORS(app)

# Reading and scrambling themes
def read_and_scramble_themes():
    with open('themes.txt', 'r') as file:
        themes = file.readlines()
    random.shuffle(themes)
    return [theme.strip() for theme in themes]


#generating response with message input
def generate_response(user_message):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        response = completion.choices[0].message.content
        return response
    except Exception as e:
        return str(e)

def generate_response_list(user_message_list):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message} for message in user_message_list]
        )
        response = completion.choices[0].message.content
        return response
    except Exception as e:
        return str(e)


#app route for chat response
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')

        response = generate_response(user_message)
        print(response)
        return jsonify({"message": str(response)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/', methods=['GET'])
def home():
    print("Server is running on port 8080")
    return jsonify({"message": "server running, all good!"})
    

@app.route('/imageA',methods=['GET'])
def image_a():
    imageOutput = generateImage("8 bit style of a hackathon")
    print("response worked or something idk")
    return jsonify({"message": imageOutput})

def generateImage(prompt):
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    )
    print(response.data[0].url)
    imageOutput = str(response.data[0].url)
    return imageOutput

@app.route('/startScramble',methods=['GET'])
def scramble():
    try:
        scrambled_themes = read_and_scramble_themes()
        #call openai with first message
        first_response_output = first_response()

        if len(first_response_output) <= 3:
            list_input = [getFirstPromptInput(),"generate 3 character, don't add anything that wasn't asked for"]
            character_response = str(generate_response_list(list_input))
            
        else:
            print("error")
            return jsonify({"error": str(e)}), 500
        response = generate_response("")
        return jsonify({"themes": scrambled_themes}), 200
        print(scrambled_themes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def getFirstPromptInput():
    with open('firstPrompt.txt', 'r') as file:
        textString = file.readlines()
    return textString

def first_response():
    output=generate_response(getFirstPromptInput())
    print(str(output))
    return str(output)


if __name__ == '__main__':
    app.run(port=8080)