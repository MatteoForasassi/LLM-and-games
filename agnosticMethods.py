import requests
import json
import utils


def insert_state():

    prompt = ""
    while True:
        line = input("")

        if line.lower() == 'stop':
            break

        prompt += line + "\n"

    return prompt


def call_model_for_agn_evaluation(name,cot_list):

    if name == 'vicuna':
        url = 'http://131.175.15.22:61111/llama-server/v1/chat/completions'
    elif name == 'llama':
        url = 'http://127.0.0.1:8000/v1/chat/completions'
    else:
        raise Exception('Invalid model name')

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    global_prompt = []
    [global_prompt.append(element) for element in cot_list]

    with open("global_prompt.txt", "w") as output_file:
        for element in global_prompt:
            output_file.write(str(element) + "\n")
    print("len global prompt: " + str(len(global_prompt)))
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
        # Save the response as a JSON in a file
        with open('response.json', 'w') as response_file:
            response_file.write(response.text)

        # Load the response data from the saved file
        with open('response.json', 'r') as file:
            response_data = json.load(file)

        assistant_response = response_data['choices'][0]['message']['content']

    else:
        assistant_response = None
        print("HTTP request failed with status code:", response.status_code)

    return assistant_response
