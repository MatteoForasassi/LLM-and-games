import pexpect
import pyte
import time
from safePrompt import call_model
import utils

# TODO: PPO con space invaders, prompti il modello per farlo ragionare sui progressi nel gioco e se vede progeressi gli dai una reward.
# TODO: provalo su space invaders, passagli gli stati e vediamo se riesce a contare il numero di invasori o comunque a dire se sono meno o piu di prima.
# TODO: pensare all'idea di fare reinforcement learning mirato non all'allenamento ma a selezionare i few shots.

def play(game, double_prompt=False):

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

    while True:
        with open("step.txt", "r") as input_file:
            prompt = input_file.read()
        if double_prompt and episode_prompt is not None:
            episode_prompt, model_response = call_model("vicuna", game, prompt, add_prompt=episode_prompt)
        else:
            episode_prompt, model_response = call_model("vicuna", game, prompt)

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

        child.expect(pexpect.TIMEOUT, timeout=0.05)
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





def evaluate_state(mod=None):

    screen = pyte.Screen(80, 24)
    stream = pyte.ByteStream(screen)

    game = input("select game: ")
    approach = input("select approach: ")

    prompt = ""

    if mod == "compare":
        first_prompt = "this is the first state:\n"
        while True:
            line = input("Enter game state (type 'stop' to finish): ")

            if line.lower() == 'stop':
                break

            prompt += line + "\n"
        first_state = first_prompt + prompt
        second_prompt = "this is the second state:\n"
        question = "please player, compare the two states and tell me if the second state is better or worse than the second one"
        prompt = ""

        while True:
            line = input("Enter game state (type 'stop' to finish): ")

            if line.lower() == 'stop':
                break

            prompt += line + "\n"

        prompt = first_state + second_prompt + prompt + "\n" + question

        print(prompt)

    else:
        while True:
            line = input("Enter game state (type 'stop' to finish): ")

            if line.lower() == 'stop':
                break

            prompt += line + "\n"
    if approach == "few" or approach == "zero":
        model_response = call_model("vicuna", game, prompt, "state", approach)
        stream.feed(str.encode(prompt))
        if game == "hangman":
            with open("stateTranscript.txt", "a") as st_file:
                st_file.write("\n" + prompt + "\n" + model_response + "\n")
        elif game == "ninvaders":
            with open("ninvaders_state_transcripts.txt", "a") as st_file:
                st_file.write("\n" + prompt + "\n" + model_response + "\n")
        elif game == "snake":
            with open("snake_state_transcripts.txt", "a") as st_file:
                st_file.write("\n" + prompt + "\n" + model_response + "\n")
    elif approach == "chain":
        cot_list = []
        cot1 = {"content": prompt + "\n" + "please player, tell me how many letters there are in the word", "role": "user"}
        stream.feed(str.encode(cot1['content']))
        model_response1 = call_model("vicuna", game, cot1, "state", "chain")
        print(cot1['content'] + "\n" + model_response1)
        cot1answer = {"content": model_response1, "role": "assistant"}
        cot_list.append(cot1)
        cot_list.append(cot1answer)
        cot2 = utils.hang_state_ccomp2
        model_response2 = call_model("vicuna", game, cot2, "state", "chain", cot_list)
        print(cot2['content'] + "\n" + model_response2)
        cot2answer = {"content": model_response2, "role": "assistant"}
        cot_list.append(cot2)
        cot_list.append(cot2answer)
        cot3 = utils.hang_state_ccomp3
        model_response3 = call_model("vicuna", game, cot3, "state", "chain", cot_list)
        print(cot3['content'] + "\n" + model_response3)
        cot3answer = {"content": model_response3, "role": "assistant"}
        cot_list.append(cot3)
        cot_list.append(cot3answer)
        cot4 = utils.hang_state_ccomp4
        model_response4 = call_model("vicuna", game, cot4, "state", "chain", cot_list)
        print(cot4['content'] + "\n" + model_response4)
        cot4answer = {"content": model_response4, "role": "assistant"}
        cot_list.append(cot4)
        cot_list.append(cot4answer)
        cot5 = utils.hang_state_ccomp5
        model_response5 = call_model("vicuna", game, cot5, "state", "chain", cot_list)
        print(cot5['content'] + "\n" + model_response5)

        if game == "hangman":
            with open("cot_hangman_state_transcripts.txt", "a") as cot_file:
                cot_file.write("\n" + cot1["content"] + "\n" +
                               model_response1 + "\n" + cot2["content"] + "\n" + model_response2 +
                               "\n" + cot3["content"] + "\n" + model_response3 + "\n" +
                               cot4["content"] + "\n" + model_response4 + "\n" + cot5["content"] + "\n" + model_response5 + "\n")


def human_player():
    game = input("select game: ")

    screen = pyte.Screen(80, 24)
    stream = pyte.ByteStream(screen)
    child = pexpect.spawn(game)
    child.expect(pexpect.TIMEOUT, timeout=0.1)
    stream.feed(child.before)
    print(*screen.display, sep="\n")
    while (True):
        command = input("enter command: ")
        if game == "ninvaders":
            child.sendline("p")
        if command == "r":
            command = '\033\117\103'
        elif command == "l":
            command = '\033\117\104'
        elif command == "u":
            command = '\033\117\101'
        elif command == "d":
            command = '\033\117\102'
        elif command == "s":
            command = " "

        child.send(command)
        if game == "ninvaders":
            time.sleep(0.02)
            child.sendline("p")

        child.expect(pexpect.TIMEOUT, timeout=0.05)
        stream.feed(child.before)
        print(*screen.display, sep="\n")


evaluate_state()

#play("ninvaders", True)

#human_player()
