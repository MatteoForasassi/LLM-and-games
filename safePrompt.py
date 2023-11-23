import random

import requests
import json
import utils



def call_model(name, game, episode_prompt, mod="play", approach="few", cot_list=None, add_prompt=None):

    if cot_list is None:
        cot_list = []


    print("name: ", name)
    print("game: ", game)
    print("mod: ", mod)
    print("approach: ", approach)

    if name == 'vicuna':
        url = 'http://131.175.15.22:61111/llama-server/v1/chat/completions'
    elif name == 'llama':
        url = 'http://127.0.0.1:8000/v1/chat/completions'
    else:
        raise Exception('Invalid model name')

    if game == 'hangman':
        if mod == 'state' and approach == 'few':
            global_prompt = utils.HANGMAN_STATE_PROMPT
        elif mod == 'state' and approach == 'chain':
            global_prompt = utils.HANGMAN_CHAIN_OF_THOUGHTS_STATE_PROMPT
        elif mod == 'play':
            global_prompt = utils.HANGMAN_GAME_PROMPT
        else:
            raise Exception('Invalid mod')
    elif game == 'snake':
        if mod == 'state' and approach == 'few':
            global_prompt = utils.SNAKE_STATE_PROMPT
        else:
            raise Exception('Invalid mod')
    elif game == 'ninvaders':
        if mod == 'play':
            global_prompt = utils.NINVADERS_GAME_PROMPT[:7]


        else:
            raise Exception('Invalid mod')
    else:
        global_prompt = [{'content': 'you are a helpful assistant that is also an expert game player', 'role': 'assistant'}]
    # Set the request headers
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    if approach == 'few' or approach == 'zero':
        if add_prompt is not None:
            message_struct = {"content": add_prompt + "\n\n" + episode_prompt, "role": "user"}
            print("LEN ADD PROMPT: " + str(len(add_prompt)))
            print("LEN EPISODE PROMPT: " + str(len(episode_prompt)))

        else:
            message_struct = {"content": episode_prompt, "role": "user"}
        global_prompt.append(message_struct)



    elif approach == 'chain':
        message_struct = episode_prompt
        [global_prompt.append(element) for element in cot_list]
        global_prompt.append(message_struct)
    else:
        raise Exception('Invalid approach')
    request_data = {
        "messages": global_prompt,

        "max_tokens": 400,

    }

    # Convert the request data to JSON
    request_json = json.dumps(request_data)

    # Send the POST request
    response = requests.post(url, headers=headers, data=request_json)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the response to a file (you can customize the file name and path)
        with open('response.json', 'w') as response_file:
            response_file.write(response.text)

        # Load the response data from the saved file
        with open('response.json', 'r') as file:
            response_data = json.load(file)

        assistant_response = response_data['choices'][0]['message']['content']

    else:
        print("HTTP request failed with status code:", response.status_code)

    print("LEN OF PROMPT: " + str(len(global_prompt)))
    print("assistant response: ", assistant_response)
    return episode_prompt, assistant_response

