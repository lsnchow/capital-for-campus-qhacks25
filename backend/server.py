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



def readBackground():
    background_images = []
    with open('background.txt', 'r') as file:
        for line in file:
            background_images.append(line.strip())
    
    return background_images


def read_content():
    background_images = []
    with open('content.txt', 'r') as file:
        for line in file:
            background_images.append(line.strip())
    
    return background_images


def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1792x1024",
        quality="standard",
        n=1,
    )
    print(response.data[0].url)
    image_output = str(response.data[0].url)
    return image_output

def get_input():
    with open('mpv.txt', 'r') as file:
        return file.read()




def getBackgroundImages(list):
    background_images = []
    #range 7 for 7 scenes
    for i in range(7):
        background_images.append(generate_image("based on this description create a simple pixelated artstyle image of the background of this setting, not including the character themselves:" + list[i]))
    return background_images


@app.route('/api', methods=['GET'])
def start():
    try:
        print("gotten here")
        big_prompt = get_first_prompt_input()
        #print(big_prompt)
        #print(type(big_prompt))
        response = generate_response(big_prompt)
        #print(response)

        clean = response.strip()
        split = split_string(clean)
        #print(split)

        split = [item for item in split if len(item) >= 16]
        print("start")
        result_dict = {}
        for item in split:
            if '-1' in item:
                result_dict[item] = -1
            elif '+2' in item:
                result_dict[item] = 2
            else:
                result_dict[item] = 0
        #print(result_dict)
        print("here")

        result_values = [value for value in result_dict.values() if value != 0]
        print("WHAT IS HAPPENDING: " + str(result_values))
        #print(result_values)
        #write result dictionary

        #print(split)

        chunked = chunk_list(split, 6)
        first_element_of_each_embeded_list = [chunk[0] for chunk in chunked]
        #print(first_element_of_each_embeded_list)
        linkOfBackgroundImages = getBackgroundImages(first_element_of_each_embeded_list)
        
        linkOfBackgroundImages = readBackground()

        #horrible naming but somehow it works

        #dont need to check if each chunk in chunked is the right amount of elemnts, always will be 6
        num_elements_in_chunked = [len(chunk) for chunk in chunked]
        #print(num_elements_in_chunked)
        second_elements = [chunk[1] for chunk in chunked]
        third_elements = [chunk[2] for chunk in chunked]
        fourth_elements = [chunk[3] for chunk in chunked]
        fifth_elements = [chunk[4] for chunk in chunked]
        sixth_elements = [chunk[5] for chunk in chunked]
        print("\n\n\n2nd" + str(second_elements))
        print("\n\n\n3rd" + str(third_elements))
        print("\n\n\n4th" + str(fourth_elements))
        print("\n\n\n5th" + str(fifth_elements))
        print("\n\n\n6th" + str(sixth_elements))

        print("made it this far")

        output_list = []
        for i in range(7):
            print(i)
            output_list.append(second_elements[i])
            output_list.append(third_elements[i])
            output_list.append(fourth_elements[i])
            output_list.append(fifth_elements[i])
            output_list.append(sixth_elements[i])

        print("made it this fa2r")
        with open('content.txt', 'w') as file:
            file.write('\n'.join(output_list))

        print(result_values)
        
        with open('content.txt', 'a') as file:
            file.write('\n'.join(map(str, result_values)))
        

        
        with open('background.txt', 'w') as file:
            file.write('\n'.join(linkOfBackgroundImages))
        print("made it this far4")
        

        

        json_output = json.dumps(final_output)
        print(json_output)

        return jsonify(True),200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

@app.route('/getResults', methods=['GET'])
def get_results():
    try:
        with open('mpv.txt', 'r') as file:
            content = file.read()
        
        return jsonify({content}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/output', methods=['POST'])
def output():
    try:
        data = request.json
        user_message = data.get('message', '')
        with open('mpv.txt', 'w') as file:
            file.write(user_message)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/background', methods=['GET'])
def get_background():
    try:
        return jsonify(readBackground()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/content', methods=['GET'])
def get_blurb():
    try:
        return jsonify(read_content()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=8080)



