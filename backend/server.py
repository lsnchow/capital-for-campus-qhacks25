import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import json
import re
import random


#getting api key
load_dotenv()
API_KEY = os.getenv('API_KEY')

def chunk_list(lst, chunk_size=6):
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]

def get_first_prompt_input():
    with open('firstPrompt.txt', 'r') as file:
        return str(file.read())

def first_response():
    output=generate_response(get_first_prompt_input())
    return str(output)




def list_to_json(data_list):
    import json
    return json.dumps(data_list)


def split_string(input_string):
    input_string = input_string.replace("Outcome one:", "")
    input_string = input_string.replace("Outcome two:", "")
    input_string = input_string.replace("Action one:", "")
    input_string = input_string.replace("Action two:", "")
    input_string = input_string.replace("Location:", "")
    input_string = input_string.replace("Scenario:", "")
    input_string = input_string.replace("\n", "")
    
    return input_string.split("@")



#creating the client
client = OpenAI(
    api_key=API_KEY
)


def chunk_list(lst, chunk_size=6):
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]


#initializing flask
app = Flask(__name__)
CORS(app)

# Reading and scrambling themes


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
        print("error with model")
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





def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    print(response.data[0].url)
    image_output = str(response.data[0].url)
    return image_output




def getBackgroundImages(list):
    background_images = []
    for i in range(6):
        background_images.append(generate_image("based on this description create a simple pixelated artstyle image of the background of this setting, not including the character themselves:" + list[i]))
    return background_images


@app.route('/api', methods=['GET'])
def start():
    try:
        print("gotten here")
        big_prompt = get_first_prompt_input()
        print(big_prompt)
        print(type(big_prompt))
        response = generate_response(big_prompt)
        print(response)
        print(type(response))

        clean = response.strip()
        split = split_string(clean)
        print(split)

        split = [item for item in split if len(item) >= 16]
        print(len(split))
        for i in split:
            print(i+"\n")
        result_dict = {}
        for item in split:
            if '-1' in item:
                result_dict[item] = -1
            elif '+2' in item:
                result_dict[item] = 2
            else:
                result_dict[item] = 0
        print(result_dict)

        print(split)

        chunked = chunk_list(split, 6)
        second_index_list = [chunk[0] for chunk in chunked if len(chunk) > 1]
        print(second_index_list)
        linkOfBackgroundImages = getBackgroundImages(second_index_list)
        
        for i in linkOfBackgroundImages:
            print(i)
        with open('background.txt', 'w') as file:
            file.write('\n'.join(linkOfBackgroundImages))
        
        
        finalOutput = chunked.append(linkOfBackgroundImages)


        

        json_output = json.dumps(finalOutput)
        print(json_output)
        return jsonify(json_output),200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


@app.route('/background', methods=['GET'])
def start():
    try:
        with open('background.txt', 'r') as file:
            return jsonify(file.read()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(port=8080)



