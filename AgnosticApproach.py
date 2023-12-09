import pexpect
import pyte
import time
from safePrompt import call_model
import utils
import agnosticMethods
import re


# TODO adventure inventario e goal aggiuntivi
# TODO traiettorie vanno selezionate con le risposte

def game_evaluation(game, mod="rt"):
    if mod == "test":
        print("enter first game state (type 'stop' to finish): \n")
        first_state = agnosticMethods.insert_state()
        print("enter second game state (type 'stop' to finish): \n")
        second_state = agnosticMethods.insert_state()
    else:
        with open("first_state.txt", "r") as first_file:
            first_state = first_file.read()
        with open("second_state.txt", "r") as second_file:
            second_state = second_file.read()

    system_prompt = {"content": '''you are a helpful assistant, you have to understand the game: ''' + game + '''.
    By observing two states of the game, your task is to find the important aspects of the game, such as the general settings ,
    the score and the goal of the game. Then, you have to compare the two states and to decide which is better in terms of score and goal of the game.
    Finally, you have to give a numerical value from -2 to 2 to your preference, where -2 means that the first state is much better than the second one
    and +2 means the opposite.''', "role": "system"}
    first_prompt = {"content": '''This is the first state:\n''' + first_state + '''\n
    This is the second state:\n''' + second_state + '''\n
    tell me what is the setting of this game''', "role": "user"}
    second_prompt = {"content": '''is there an explicit score in this game? if not, how do you detect progress?''',
                     "role": "user"}
    third_prompt = {"content": '''how do you progress and accumulate rewards in this game?''', "role": "user"}
    fourth_prompt = {
        "content": '''based on your previous answers, which is the best state between the first and the second?''',
        "role": "user"}
    fifth_prompt = {"content": '''based on the previous answer, evaluate your preference with a numerical value between -2 and +2. Remember that -2 means that the first state is way
    better than the second, while +2 means that the second is much better than the first''', "role": "user"}

    cot_list = [system_prompt]
    cot_list = cot_list + utils.AGNOSTIC_EVALUATION_COT

    prompt_list = [first_prompt, second_prompt, third_prompt, fourth_prompt, fifth_prompt]

    cot_list = cot_reasoning(cot_list, prompt_list)[0]

    with open("agno_transcripts.txt", "w") as cot_file:
        for i in cot_list:
            cot_file.write(str(i) + "\n")


"""the following method is used to extract useful information regarding rules, goals and actions from the manual of the game"""


def game_description():
    with open("hangman_example.txt", "r") as example_file:
        example = example_file.read()

    example = "no example today"
    print("insert the manual of the game:")
    manual = agnosticMethods.insert_state()

    system_prompt = {"content": '''you are a helpful assistant, you are provided with a manual of a game and an example of the game execution.
    This is the manual: \n''' + manual + '''.
    This is an example of the game: \n''' + example + '''.
    By reading the manual and observing the execution, you have to answer user's questions. ''', "role": "system"}

    first_prompt = {"content": '''what is the goal of the game?''', "role": "user"}
    second_prompt = {"content": '''what is the correct format in which the player should insert the action?''',
                     "role": "user"}
    third_prompt = {"content": '''describe the format of valid actions synthetically ''', "role": "user"}
    fourth_prompt = {"content": '''is there an explicit score in this game? if not, how do you detect progress?''',
                     "role": "user"}
    fifth_prompt = {"content": '''how do you progress in this game?''', "role": "user"}
    sixth_prompt = {"content": '''what should a player avoid in this game?''', "role": "user"}
    seventh_prompt = {"content": '''is it possible to win the game? how?''', "role": "user"}
    eight_prompt = {"content": '''is it possible to lose the game? how?''', "role": "user"}
    ninth_prompt = {
        "content": '''based on your previous answers, list all the information that are useful to succesfully play the game''',
        "role": "user"}
    prompt_list = [first_prompt, second_prompt, third_prompt, fourth_prompt, fifth_prompt, sixth_prompt, seventh_prompt,
                   eight_prompt, ninth_prompt]

    cot_list = [system_prompt]

    cot_list = cot_reasoning(cot_list, prompt_list)[0]

    with open("agno_transcripts.txt", "w") as cot_file:
        for i in cot_list:
            cot_file.write(str(i) + "\n")

    return cot_list[4]['content'], cot_list[6]['content'], cot_list[18]['content']


"""the following function is used to make the language model act in the game"""


def act(game, information, valid_actions):
    system_prompt = {"content": '''You are an expert player of the game : ''' + game + '''. 
    These are the rules: ''' + information + '''. 
    Your answer should be limited to the format of valid actions:: ''' + valid_actions, "role": "system"}

    cot_list = [system_prompt]
    screen = pyte.Screen(80, 24)
    stream = pyte.ByteStream(screen)
    child = pexpect.spawn(game)
    if game == "ninvaders":
        child.sendline(" ")
        time.sleep(0.02)
        child.sendline("p")
    child.expect(pexpect.TIMEOUT, timeout=0.1)
    stream.feed(child.before)
    episode_prompt = None
    print(*screen.display, sep="\n")
    with open("step.txt", "w") as output_file:
        output_file.write("\n".join(screen.display))
    count = 0
    while True:
        with open("step.txt", "r") as input_file:
            game_state = input_file.read()
        # The following three lines are useful to save the frames and create the timelapse video
        output_image = "/home/matteo/PycharmProjects/llm_and_games/time_lapse/frame_" + str(count) + ".png"
        utils.text_to_image(game_state, output_image)
        count += 1
        prompt_state = {"content": game_state, "role": "user"}
        if len(cot_list) == 5:
            cot_list = [system_prompt, cot_list[3], cot_list[4]]
        cot_list.append(prompt_state)
        model_response = agnosticMethods.call_model_for_agn_evaluation("vicuna", cot_list)
        cot_list.append({"content": model_response, "role": "assistant"})
        print('model_response:' + model_response)
        command = None
        if game == "ninvaders":
            child.sendline("p")
        if "right" in model_response:
            command = '\033\117\103'
        elif "left" in model_response:
            command = '\033\117\104'
        elif "up" in model_response:
            command = '\033\117\101'
        elif "down" in model_response:
            command = '\033\117\102'
        elif "shoot" in model_response or "space" in model_response:
            command = " "

        child.send(command) if command is not None else child.send(model_response)

        if game == "ninvaders":
            time.sleep(0.02)
            child.sendline("p")
        try:
            child.expect(pexpect.TIMEOUT, timeout=0.1)
        except pexpect.EOF:
            return "game over"
        stream.feed(child.before)

        print(*screen.display, sep="\n")
        # write the game step in a text file
        with open("step.txt", "w") as output_file:
            output_file.write("\n".join(screen.display))
        # write the transcript of the game in a file
        if game == "hangman":
            with open("hangman_transcript.txt", "a") as transcr_file:
                transcr_file.write("\n".join(screen.display))
        elif game == "ninvaders":
            with open("ninvaders_transcript.txt", "a") as transcr_file:
                transcr_file.write("\n".join(screen.display))
        # write the model response in a file
        with open("responses.txt", "a") as resp_file:
            resp_file.write(model_response + "\n")


def act_simple(game, information, valid_actions):
    "method to act in games that wait for the user input"

    system_prompt = {"content": '''You are an expert player of the game : ''' + game + '''. 
    These are the rules: ''' + information + '''. 
    These are the valid actions: ''' + valid_actions, "role": "system"}

    first_prompt = {
        "content": '''based on the information you received, what are the valid action a player can take in this state?''',
        "role": "user"}
    second_prompt = {
        "content": '''based on the information you received and your previous answer, what is the best action a player can take in this state?''',
        "role": "user"}
    secondb_prompt = {"content": '''list some examples of valid action, in the correct format''', "role": "user"}
    secondc_promtp = {"content": '''pick the best action from the ones you listed in your previous answer''',
                      "role": "user"}
    third_prompt = {
        "content": '''answer with the action you selected in your previous answer. Express your answer in a strictly valid action format, use double quotes ("") to highlight the action''',
        "role": "user"}

    prompt_list = [first_prompt, second_prompt, secondb_prompt, secondc_promtp, third_prompt]

    cot_list = [system_prompt]

    screen = pyte.Screen(80, 24)
    stream = pyte.ByteStream(screen)
    child = pexpect.spawn(game)
    child.expect(pexpect.TIMEOUT, timeout=0.1)
    stream.feed(child.before)
    episode_prompt = None
    print(*screen.display, sep="\n")
    with open("step.txt", "w") as output_file:
        output_file.write("\n".join(screen.display))
    while True:
        with open("step.txt", "r") as input_file:
            game_state = input_file.read()
        prompt_state_1 = {"content": game_state + "Given this state, please choose an action", "role": "user"}
        prompt_state_2 = {
            "content": game_state + "assistant, based on the information you received, try to explain the state of the game",
            "role": "user"}

        cot_list.append(prompt_state_2)
        model_response = agnosticMethods.call_model_for_agn_evaluation("vicuna", cot_list)

        cot_list.append({"content": model_response, "role": "assistant"})

        cot_list, count = cot_reasoning(cot_list, prompt_list)
        #count = cot_reasoning(cot_list, prompt_list)[1]


        if count == len(prompt_list):
            #if len(cot_list) == 14:
            if game == 'hangman':
                cot_list = check_valid_answer(cot_list)

        pattern1 = r'"([^"]*)"'
        action = cot_list[-1]['content']
        print(action)
        #pattern2 = r"'([^']*)'"
        matches = []
        if game == "snake":
            matches = [action]
        elif game == "hangman":
            #match = re.findall(pattern1, action)

            #if len(match[0]) == 1:
            #    matches = [match[0]]
            #elif bool(re.search(pattern1, match[0])):
            #    matches = re.findall(pattern1, match[0])
            #else:
             #   matches = re.findall(pattern2, match[0])
            matches = re.findall(pattern1, action)

        cot_list = [system_prompt, prompt_state_1, {"content": matches[0], "role": "assistant"}]

        command = None
        if game == "snake":
            if "right" in model_response:
                command = '\033\117\103'
            elif "left" in model_response:
                command = '\033\117\104'
            elif "up" in model_response:
                command = '\033\117\101'
            elif "down" in model_response:
                command = '\033\117\102'

        child.send(command) if command is not None else child.send(matches[0])
        try:
            child.expect(pexpect.TIMEOUT, timeout=0.1)
        except pexpect.EOF:
            stream.feed(child.before)
            print(*screen.display, sep="\n")
            print("######################GAME OVER######################")
            return "game over"

        stream.feed(child.before)
        print(*screen.display, sep="\n")
        print(action)
        # write the game step in a text file
        with open("step.txt", "w") as output_file:
            output_file.write("\n".join(screen.display))
        # write the transcript of the game in a file
        if game == "hangman":
            with open("hangman_transcript.txt", "a") as transcr_file:
                transcr_file.write("\n".join(screen.display))
        # write the model response in a file
        with open("responses.txt", "a") as resp_file:
            resp_file.write(model_response + "\n")


def check_valid_answer(cot_list):
    pattern1 = r'"([^"]*)"'
    #final_cot = cot_list[-1]['content']

    if not bool(re.search(pattern1, cot_list[-1]['content'])):
        while True:
            cot_list.pop()
            model_response = agnosticMethods.call_model_for_agn_evaluation("vicuna", cot_list)
            print('response:' + model_response)
            cot_answer = {"content": model_response, "role": "assistant"}
            cot_list.append(cot_answer)
            if bool(re.search(pattern1, model_response)):
                match = re.findall(pattern1, model_response)
                if len(match[0]) == 1:
                    break
    #elif len(re.findall(pattern1, cot_list[-1]['content'])):
    else:
        while True:
            match = re.findall(pattern1, cot_list[-1]['content'])
            if len(match[0]) == 1:
                break
            else:
                cot_list.pop()
                model_response = agnosticMethods.call_model_for_agn_evaluation("vicuna", cot_list)
                print('response:' + model_response)
                cot_answer = {"content": model_response, "role": "assistant"}
                cot_list.append(cot_answer)
                if bool(re.search(pattern1, model_response)):
                    match = re.findall(pattern1, model_response)
                    if len(match[0]) == 1:
                        break

    return cot_list


def cot_reasoning(cot_list, prompt_list):
    count = 0
    for prompt in prompt_list:
        cot_list.append(prompt)
        model_response = agnosticMethods.call_model_for_agn_evaluation("vicuna", cot_list)
        print('content:' + prompt['content'] + "\n" + 'response:' + model_response)
        cot_answer = {"content": model_response, "role": "assistant"}
        cot_list.append(cot_answer)
        count = count + 1
    return cot_list, count


def pipeline(game):
    actions_format, actions_valid, information = game_description()
    print("information: " + information)
    print("actions format: " + actions_format)
    episode_count = 0
    act_simple(game, information, actions_format)
    # while act(game, information, actions_format) == "game over":
    #    episode_count += 1


# act("hangman", "the goal of the game is to guess the word that the computer has chosen. The player has 6 attempts to guess the word. The player can guess a letter or the entire word. The player wins if he guesses the word, otherwise he loses.", "the player can guess a letter or the entire word")

# game_description()

pipeline("hangman")

# act("hangman", "the goal of the game is to guess the word that the computer has chosen. The player has 6 attempts to guess the word. The player can guess a letter or the entire word. The player wins if he guesses the word, otherwise he loses.", "the player can guess a letter or the entire word")

# game_description()
