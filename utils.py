from PIL import Image, ImageDraw, ImageFont
import os
import imageio


def text_to_image(input_text, output_image, font_size=20, image_size=(500, 500), text_color=(0, 0, 0),
                  background_color=(255, 255, 255)):
    # Create a blank image with the specified size and background color
    image = Image.new('RGB', image_size, background_color)

    # Choose a font (you may need to provide the path to a font file)
    font = ImageFont.load_default()

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Set the font size and color
    draw.font = ImageFont.truetype("LiberationSans-Regular.ttf", font_size)
    draw.text((10, 10), input_text, fill=text_color, font=font)

    # Save the image to a file
    image.save(output_image)


# Example usage
input_text = "Hello, this is a text file content!"
output_image = "output_image.png"

text_to_image(input_text, output_image)





#====================================================================PROMPTS=======================================================================================
hang_game_sys_prompt = {'content': ''''
You are an expert player of the game Hangman. These are the rules: In hangman, the computer picks a word from the on-line word list and you 
must try to guess it. The computer keeps track of which letters have been guessed and how many wrong guesses you have made 
on the screen in a graphic fashion. Your goal is to guess the word letter by letter before you run out of guesses. Your guesses should be 
limited to the letter you are trying to guess, in the format "letter". ''', 'role': 'system'}

hang_game_comp1 = {'content': '''
     ______
     |    |
     |                                               Guessed:
     |
     |                                               Word #:           1
     |                                               Current Average:  0.000
   __|_____                                          Overall Average:  0.000
   |      |___
   |_________|

 Word:  -------
Guess:  
''', 'role': 'user'}

hang_game_player1 = {'content': '''a''', 'role': 'assistant'}

hang_game_comp2 = {'content': '''
     ______
     |    |
     |                                                                    Guessed:  a
     |
     |                                                                    Word #:           1
     |                                                                    Current Average:  0.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  -a--a--a
Guess:  
''', 'role': 'user'}

hang_game_player2 = {'content': '''e''', 'role': 'assistant'}

hang_game_comp3 = {'content': '''

     ______
     |    |
     |    O                                                               Guessed:  ae
     |
     |                                                                    Word #:           1
     |                                                                    Current Average:  1.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  -a--a--a
Guess:  
''', 'role': 'user'}

hang_game_player3 = {'content': '''r''', 'role': 'assistant'}

hang_game_comp4 = {'content': '''
     ______
     |    |
     |    O                                                               Guessed:  aer
     |
     |                                                                    Word #:           1
     |                                                                    Current Average:  1.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  -ar-a--a
Guess:  
''', 'role': 'user'}

hang_game_player4 = {'content': '''t''', 'role': 'assistant'}

hang_game_comp5 = {'content': '''
     ______
     |    |
     |    O                                                               Guessed:  aert
     |    |
     |                                                                    Word #:           1
     |                                                                    Current Average:  2.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  -ar-a--a
Guess:  
''', 'role': 'user'}

hang_game_player5 = {'content': '''s''', 'role': 'assistant'}

hang_game_comp6 = {'content': '''
     ______
     |    |
     |    O                                                               Guessed:  aerst
     |    |
     |    |                                                               Word #:           1
     |                                                                    Current Average:  3.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  -ar-a--a
Guess:  
''', 'role': 'user'}

hang_game_player6 = {'content': '''n''', 'role': 'assistant'}

hang_game_comp7 = {'content': '''
     ______
     |    |
     |    O                                                               Guessed:  aenrst
     |    |
     |    |                                                               Word #:           1
     |   /                                                                Current Average:  4.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  -ar-a--a
Guess:  
''', 'role': 'user'}

hang_game_player7 = {'content': '''i''', 'role': 'assistant'}

hang_game_comp8 = {'content': '''
     ______
     |    |
     |    O                                                               Guessed:  aeinrst
     |   /|
     |    |                                                               Word #:           1
     |   /                                                                Current Average:  5.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  -ar-a--a
Guess:  
''', 'role': 'user'}

hang_game_player8 = {'content': '''l''', 'role': 'assistant'}

hang_game_comp9 = {'content': '''
     ______
     |    |
     |    O                                                               Guessed:  aeilnrst
     |   /|\\
     |    |                                                               Word #:           1
     |   /                                                                Current Average:  6.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  -ar-a--a
Guess:  
''', 'role': 'user'}

hang_game_player9 = {'content': '''o''', 'role': 'assistant'}

hang_game_comp10 = {'content': '''
     ______
     |    |
     |    O                                                               Guessed:  aeilnorst
     |   /|\\
     |    |                                                               Word #:           1
     |   /                                                                Current Average:  6.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  -ar-a-oa
Guess:  
''', 'role': 'user'}

hang_game_player10 = {'content': '''u''', 'role': 'assistant'}

hang_game_comp11 = {'content': '''
     ______
     |    |
     |    O                                                               Guessed:  aeilnorstu
     |   /|\\
     |    |                                                               Word #:           1
     |   / \\                                                              Current Average:  9.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  -ar-a-oa
Guess:  
Sorry, the word was "barbacoa"
another world? (y/n)
''', 'role': 'user'}

hang_game_player11 = {'content': '''y''', 'role': 'assistant'}

HANGMAN_GAME_PROMPT = [hang_game_sys_prompt, hang_game_comp1, hang_game_player1, hang_game_comp2, hang_game_player2,
                       hang_game_comp3, hang_game_player3, hang_game_comp4, hang_game_player4, hang_game_comp5,
                       hang_game_player5, hang_game_comp6, hang_game_player6, hang_game_comp7, hang_game_player7,
                       hang_game_comp8, hang_game_player8, hang_game_comp9, hang_game_player9, hang_game_comp10,
                       hang_game_player10, hang_game_comp11, hang_game_player11]

hang_state_sys_prompt = {"content": ''' You are a useful assistant that is also an expert player of the game Hangman. 
These are the rules: In hangman, user picks a word from the on-line word list and you 
must try to guess it. User keeps track of which letters have been guessed and how many wrong guesses you have made 
on the screen in a graphic fashion. The information about the word are given to you by user, the number of dashes indicates the number of missing letters.
Your goal is to observe the state of the game and explain it.''',
                         "role": "system"}

hang_state_comp1 = {"content": ''' 
     ______
     |    |
     |                                                                    Guessed:
     |
     |                                                                    Word #:           1
     |                                                                    Current Average:  0.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  -----
Guess:  

please player, explain the state of the game''',
                    "role": "user"}

hang_state_player1 = {
    "content": '''the word is 5 letters long, the game is just started and the player has not guessed any letter yet.''',
    "role": "assistant"}

hang_state_comp2 = {"content": '''     
     ______
     |    |
     |    O                                                               Guessed:  aer
     |    |
     |                                                                    Word #:           1
     |                                                                    Current Average:  2.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  -r----
Guess:  

please player, explain the state of the game''',
                    "role": "user"}

hang_state_player2 = {
    "content": '''the word is 6 letters long, the player has guessed the letters a, e and r and has made 2 wrong guesses.''',
    "role": "assistant"}

hang_state_comp3 = {"content": '''     
     ______
     |    |
     |    O                                                               Guessed:  abdeiloprst
     |   /|\\
     |    |                                                               Word #:           1
     |   / \\                                                              Current Average:  9.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  s-ri-e-
Guess:  
Sorry, the word was "shriven"

please player, explain the state of the game''',
                    "role": "user"}

hang_state_player3 = {"content": '''the word is 7 letters long, the player has guessed the letters a, b, d, e, i, l, o, p, r, s, t and has made 8 wrong guesses,
losing the game. The correct word was "shriven"''',
                      "role": "assistant"}

hang_state_comp4 = {"content": '''
     ______
     |    |
     |    O                                                               Guessed:  tilon
     |    |
     |    |                                                               Word #:           1
     |                                                                    Current Average:  3.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  t--i--
Guess:  

please player, explain the state of the game''',
                    "role": "user"}

hang_state_player4 = {
    "content": '''the word is 6 letters long, the player has guessed the letters t, i, l, o, n and has made 3 wrong guesses.''',
    "role": "assistant"}

hang_state_comp5 = {"content": '''
     ______
     |    |
     |    O                                                               Guessed:  aelnrst
     |    |
     |    |                                                               Word #:           2
     |   /                                                                Current Average:  6.500
   __|_____                                                               Overall Average:  9.000
   |      |___
   |_________|

 Word:  entente
Guess:  
You got it!

please player, explain the state of the game''',
                    "role": "user"}

hang_state_player5 = {
    "content": '''the word is 7 letters long, the player has guessed the letters a, e, l, n, r, s, t and has made 4 wrong guesses, the player won the game.''',
    "role": "assistant"}

HANGMAN_STATE_PROMPT = [hang_state_sys_prompt, hang_state_comp1, hang_state_player1, hang_state_comp2,
                        hang_state_player2, hang_state_comp3, hang_state_player3, hang_state_comp4,
                        hang_state_player4, hang_state_comp5, hang_state_player5]

"""================================================================CHAIN OF THOUGHTS MODIFICATION OF THE STATE EVALUATION TASK======================================================="""

hang_state_ccomp1 = {"content": '''     
     ______
     |    |
     |    O                                                               Guessed:  aer
     |    |
     |                                                                    Word #:           1
     |                                                                    Current Average:  2.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  -r----
Guess:  

please player, tell me how many letters are in the word''',
                     "role": "user"}
hang_state_cplay1 = {"content": '''based on the information given by "Word: -r----", the word is 6 letters long ''',
                     "role": "assistant"}

hang_state_ccomp2 = {"content": '''which letters have been correctly guessed? ''', "role": "user"}

hang_state_cplay2 = {
    "content": '''based on the information given by "Word: -r----" and "Guessed: aer", the letter r has been correctly guessed''',
    "role": "assistant"}

hang_state_ccomp3 = {"content": '''which letters have been wrongly guessed? ''', "role": "user"}

hang_state_cplay3 = {
    "content": '''based on the information given by "Word: -r----" and "Guessed: aer", the letters a, e have been wrongly guessed''',
    "role": "assistant"}

hang_state_ccomp4 = {"content": '''how many letters are missing to guess the word?''', "role": "user"}

hang_state_cplay4 = {"content": '''based on the information given by "Word: -r----", there are five letters missing''',
                     "role": "assistant"}

hang_state_ccomp5 = {"content": '''summarize the previous information explaining the state of the game''',
                     "role": "user"}

hang_state_cplay5 = {
    "content": '''the word is 6 letters long, the player has guessed the letters a, e and r and has made 2 wrong guesses.''',
    "role": "assistant"}

hang_state_c2comp1 = {"content": ''' 
     ______
     |    |
     |                                                                    Guessed:
     |
     |                                                                    Word #:           1
     |                                                                    Current Average:  0.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  -----
Guess:  

please player, tell me how many letters are in the word''',
                      "role": "user"}

hang_state_c2play1 = {"content": '''based on the information given by "Word: -----", the word is 5 letters long ''',
                      "role": "assistant"}

hang_state_c2comp2 = {"content": '''which letters have been correctly guessed? ''', "role": "user"}

hang_state_c2play2 = {
    "content": '''based on the information given by "Word: -----" and "Guessed: ", no letter has been correctly guessed''',
    "role": "assistant"}

hang_state_c2comp3 = {"content": '''which letters have been wrongly guessed? ''', "role": "user"}

hang_state_c2play3 = {
    "content": '''based on the information given by "Word: -----" and "Guessed: ", no letter has been wrongly guessed''',
    "role": "assistant"}

hang_state_c2comp4 = {"content": '''how many letters are missing to guess the word?''', "role": "user"}

hang_state_c2play4 = {"content": '''based on the information given by "Word: -----", there are five letters missing''',
                      "role": "assistant"}

hang_state_c2comp5 = {"content": '''summarize the previous information explaining the state of the game''',
                      "role": "user"}

hang_state_c2play5 = {
    "content": '''the word is 5 letters long, the game is just started and the player has not guessed any letter yet.''',
    "role": "assistant"}

hang_state_c3comp1 = {"content": '''     
     ______
     |    |
     |    O                                                               Guessed:  abdeiloprst
     |   /|\\
     |    |                                                               Word #:           1
     |   / \\                                                              Current Average:  9.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  s-ri-e-
Guess:  
Sorry, the word was "shriven"

please player, tell me how many letters are in the word''',
                      "role": "user"}

hang_state_c3play1 = {"content": '''based on the information given by "Word: s-ri-e-", the word is 7 letters long ''',
                      "role": "assistant"}

hang_state_c3comp2 = {"content": '''which letters have been correctly guessed? ''', "role": "user"}

hang_state_c3play2 = {
    "content": '''based on the information given by "Word: s-ri-e-" and "Guessed: abdeiloprst", the letters s, r, i and e have been correctly guessed''',
    "role": "assistant"}

hang_state_c3comp3 = {"content": '''which letters have been wrongly guessed? ''', "role": "user"}

hang_state_c3play3 = {
    "content": '''based on the information given by "Word: s-ri-e-" and "Guessed: abdeiloprst", the letters a, b, d, l, o, p, t have been wrongly guessed''',
    "role": "assistant"}

hang_state_c3comp4 = {"content": '''how many letters are missing to guess the word?''', "role": "user"}

hang_state_c3play4 = {
    "content": '''based on the information given by "Word: s-ri-e-", there are three letters missing''',
    "role": "assistant"}

hang_state_c3comp5 = {"content": '''summarize the previous information explaining the state of the game''',
                      "role": "user"}

hang_state_c3player5 = {"content": '''the word is 7 letters long, the player has guessed the letters a, b, d, e, i, l, o, p, r, s, t and has made 8 wrong guesses,
losing the game. The correct word was "shriven"''',
                        "role": "assistant"}

hang_state_c4comp1 = {"content": '''
     ______
     |    |
     |    O                                                               Guessed:  tilon
     |    |
     |    |                                                               Word #:           1
     |                                                                    Current Average:  3.000
   __|_____                                                               Overall Average:  0.000
   |      |___
   |_________|

 Word:  t--i-
Guess:  

please player, tell me how many letters are in the word''',
                      "role": "user"}

hang_state_c4play1 = {"content": '''based on the information given by "Word: t--i-", the word is 5 letters long ''',
                      "role": "assistant"}

hang_state_c4comp2 = {"content": '''which letters have been correctly guessed? ''', "role": "user"}

hang_state_c4play2 = {
    "content": '''based on the information given by "Word: t--i-" and "Guessed: tilon", the letter t and i have been correctly guessed''',
    "role": "assistant"}

hang_state_c4comp3 = {"content": '''which letters have been wrongly guessed? ''', "role": "user"}

hang_state_c4play3 = {
    "content": '''based on the information given by "Word: t--i-" and "Guessed: tilon", the letters l, o and n have been wrongly guessed''',
    "role": "assistant"}

hang_state_c4comp4 = {"content": '''how many letters are missing to guess the word?''', "role": "user"}

hang_state_c4play4 = {"content": '''based on the information given by "Word: t--i-", there are three letters missing''',
                      "role": "assistant"}

hang_state_c4comp5 = {"content": '''summarize the previous information explaining the state of the game''',
                      "role": "user"}

hang_state_player5 = {
    "content": '''the word is 5 letters long, the player has guessed the letters t, i, l, o, n and has made 3 wrong guesses.''',
    "role": "assistant"}

hang_state_c5omp1 = {"content": '''
     ______
     |    |
     |    O                                                               Guessed:  aelnrst
     |    |
     |    |                                                               Word #:           2
     |   /                                                                Current Average:  6.500
   __|_____                                                               Overall Average:  9.000
   |      |___
   |_________|

 Word:  entente
Guess:  
You got it!

please player, tell me how many letters are in the word''',
                     "role": "user"}

hang_state_c5play1 = {"content": '''based on the information given by "Word: entente", the word is 7 letters long ''',
                      "role": "assistant"}

hang_state_c5comp2 = {"content": '''which letters have been correctly guessed? ''', "role": "user"}

hang_state_c5play2 = {
    "content": '''based on the information given by "Word: entente" and "Guessed: aelnrst", the letters e, n, t have been correctly guessed''',
    "role": "assistant"}

hang_state_c5comp3 = {"content": '''which letters have been wrongly guessed? ''', "role": "user"}

hang_state_c5play3 = {
    "content": '''based on the information given by "Word: entente and "Guessed: aelnrst", the letters a, l, r and s have been wrongly guessed''',
    "role": "assistant"}

hang_state_c5comp4 = {"content": '''how many letters are missing to guess the word?''', "role": "user"}

hang_state_c5play4 = {
    "content": '''based on the information given by "Word: entente", the player has guessed each letter''',
    "role": "assistant"}

hang_state_c5comp5 = {"content": '''summarize the previous information explaining the state of the game''',
                      "role": "user"}

hang_state_c5play5 = {
    "content": '''the word is 7 letters long, the player has guessed the letters a, e, l, n, r, s, t and has made 4 wrong guesses, the player won the game.''',
    "role": "assistant"}

HANGMAN_CHAIN_OF_THOUGHTS_STATE_PROMPT = [hang_state_sys_prompt, hang_state_ccomp1, hang_state_cplay1,
                                          hang_state_ccomp2, hang_state_cplay2, hang_state_ccomp3, hang_state_cplay3,
                                          hang_state_ccomp4, hang_state_cplay4, hang_state_ccomp5, hang_state_cplay5,
                                          hang_state_c2comp1, hang_state_c2play1, hang_state_c2comp2,
                                          hang_state_c2play2, hang_state_c2comp3, hang_state_c2play3,
                                          hang_state_c2comp4, hang_state_c2play4, hang_state_c2comp5,
                                          hang_state_c2play5,
                                          hang_state_c3comp1, hang_state_c3play1, hang_state_c3comp2,
                                          hang_state_c3play2, hang_state_c3comp3, hang_state_c3play3,
                                          hang_state_c3comp4, hang_state_c3play4, hang_state_c3comp5,
                                          hang_state_c3player5]
# hang_state_c4comp1, hang_state_c4play1, hang_state_c4comp2, hang_state_c4play2, hang_state_c4comp3, hang_state_c4play3, hang_state_c4comp4, hang_state_c4play4, hang_state_c4comp5, hang_state_player5]
# hang_state_c5omp1, hang_state_c5play1, hang_state_c5comp2, hang_state_c5play2, hang_state_c5comp3, hang_state_c5play3, hang_state_c5comp4, hang_state_c5play4, hang_state_c5comp5, hang_state_c5play5]


"""================================================================SNAKE======================================================="""

snake_state_sys_prompt = {'content': '''     snake is a display-based game which must be played on a CRT terminal.
     The object of the game is to make as much money as possible without get‐
     ting eaten by the snake.  The -l and -w options allow you to specify the
     length and width of the field.  By default the entire screen is used.
     The -t option makes the game assume you are on a slow terminal.

     You are represented on the screen by an I.  The snake is 6 squares long
     and is represented by s's with an S at its head.  The money is $, and an
     exit is #.  Your score is posted in the upper left hand corner.
    ''', 'role': 'system'}

snake_state_comp1 = {'content': '''
|------------------------------------------------------------------------------|
|$50                                                                           |
|                                                                              |
|                                                                              |
|                                                                              |
|             I                                                                |
|                                                                              |
|                                                                              |
|                                                                              |
|      S                                                                       |
|    ss                                                                        |
|    ss                                                                        |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                             #                |
|                                                                              |
|                                                                              |
|$                                                                             |
|                                                                              |
|                                                                              |
|                                                                              |
|------------------------------------------------------------------------------|

assistant, describe the state of the game''', 'role': 'user'}

snake_state_player1 = {'content': '''the current score is $50, the player is positioned approximately in the upper left part of the field. 
The snake is slightly under him. There is money in the bottom left corner and an exit in the bottom right corner.''',
                       'role': 'assistant'}

snake_state_comp2 = {'content': '''
|------------------------------------------------------------------------------|
|$25                                                                           |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                  $                           |
|                                                                              |
|                                                        I                s    |
|                                                                         ssS  |
|                                                                          s   |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                          #                   |
|------------------------------------------------------------------------------|

assistant, describe the state of the game''', 'role': 'user'}

snake_state_player2 = {'content': '''the current score is $25, the player is positioned approximately in the upper right part of the field. 
                       There is money at left and the snake is at right. There is an exit in the bottom right corner''',
                       'role': 'assistant'}

snake_state_comp3 = {'content': '''
|------------------------------------------------------------------------------|
|$175                                                                          |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                     #                               ss                       |
|                                                     s                        |
|                                                    ssS                       |
|                                                $                             |
|                                                                              |
|                                                                 I            |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|------------------------------------------------------------------------------|

assistant, describe the state of the game''', 'role': 'user'}

snake_state_player3 = {'content': '''the current score is $175, the player is positioned approximately in the right part of the field. The serpent is at the left. 
                       There is money at the left and there is an exit in the upper left corner of the field.''',
                       'role': 'assistant'}

snake_state_comp4 = {'content': '''
|------------------------------------------------------------------------------|
|$200                                                                          |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                      ssss                                                    |
|                        s                                                     |
|                       S                                                      |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                  I                                                           |
|                  $                                                           |
|                                                                              |
|                                                                              |
| #                                                                            |
|                                                                              |
|------------------------------------------------------------------------------|

assistant, describe the state of the game''', 'role': 'user'}

snake_state_player4 = {'content': '''the current score is $200, the player is positioned approximately in the bottom left part of the field. The serpent is at the slightly above. 
There is money right above player and there is an exit in the bottom left part of the field.''', 'role': 'assistant'}

SNAKE_STATE_PROMPT = [snake_state_sys_prompt, snake_state_comp1, snake_state_player1, snake_state_comp2,
                      snake_state_player2, snake_state_comp3, snake_state_player3, snake_state_comp4,
                      snake_state_player4]

"""===============================================================NINVADERS======================================================="""

ninvaders_game_sys_prompt = {'content': '''

       The object of the game is to shoot all the aliens  (the  multi-coloured
       moving things) before they reach the ground.  Since these aliens aren't
       friendly (which is why you're trying to  stop  them)  they  will  shoot
       back.   Dodge the descending bullets or hang about under the large sta‐
       tionary blocks for cover. move the spaceship by digiting left and right 
       and shoot by digiting shoot. The game ends when you run out of lives.
       ''', 'role': 'system'}

ninvaders_game_comp1 = {'content': '''

   ,^,,^,,^,,^,,^,,^,,^,,^,,^,,^,
   
   _O-_O-_O-_O-_O-_O-_O-_O-_O-_O-
   
   _O-_O-_O-_O-_O-_O-_O-_O-_O-_O-
   
   -o--o--o--o--o--o--o--o--o--o-
   
   -o--o--o--o--o--o--o--o--o--o-







        ###                 ###                 ###                 ###
       #####               #####               #####               #####
      #######             #######             #######             #######
      ##   ##             ##   ##             ##   ##             ##   ##


/-^-\\
                Level: 01 Score: 0000000 Lives: /-\ /-\ 
''', 'role': 'user'}

ninvaders_game_player1 = {'content': '''right''', 'role': 'assistant'}

ninvaders_game_comp2 = {'content': '''

                                .-..-..-..-..-..-..-..-..-..-.

                                -O_-O_-O_-O_-O_-O_-O_-O_-O_-O_

                                -O_-O_-O_-O_-O_-O_-O_-O_-O_-O_

                                /o\/o\/o\/o\/o\/o\/o\/o\/o\/o\\

                                   /o\/o\   /o\/o\/o\/o\/o\/o\\






  ###                 ###                 ###                 ###
 #####               #####               #####               #####
#######             #######              ######             #######
##   ##             ##   ##             ##   ##             ##   ##


                           /-^-\\
          Level: 01 Score: 0000200 Lives: /-\ /-\ 
          
          

                     .-..-..-..-..-..-..-..-..-..-.
                     
                     -O_-O_-O_-O_-O_-O_-O_-O_-O_-O_
                     
                     -O_-O_-O_-O_-O_-O_-O_-O_-O_-O_
                     
                     /o\   /o\/o\/o\/o\/o\/o\/o\/o\
                     
                        :o\/o\   /o\/o\/o\/o\/o\/o\





        ###                 ###                 ###                 ###
       #####               ####                #####               #####
      #######             #######              ######             #######
      ##   ##             ##   ##             ##   ##             ##   ##


                                 /-^-\\
                Level: 01 Score: 0000300 Lives: /-\ /-\ 

''', 'role': 'user'}

ninvaders_game_player2 = {'content': '''shoot''', 'role': 'assistant'}

ninvaders_game_comp3 = {'content': '''







                                      .-..-..-..-..-..-..-..-..-..-.

                                      -O_-O_-O_   -O_-O_   -O_-O_-O_

                                                        -O_-O_-O_-O_

                                                           /o\/o\/o\\

                                                        /o\         
  ###                 # #                 # #                 ###
 ### #               ####                #####               #####
 ### ##             #######   :          ######              ######
##   ##             ##   ##              #   ##             ##   ##


                                               /-^-\\
          Level: 01 Score: 0002800 Lives: /-\ /-\ 








                                   ,^,,^,,^,,^,,^,,^,,^,,^,,^,,^,

                                   _O-_O-_O-   _O-_O-   _O-_O-_O-

                                                     _O-_O-_O-_O-

                                                        -o--o--o-

                                                     -o-         
  ###                 # #                 # #                 ###
 ### #               ####                #####               #####
 ### ##             #######              ######              ######
##   ##             ##   ##              #   ##             ##   ##
                              :

                                               /-^-\\
          Level: 01 Score: 0002800 Lives: /-\ /-\ 
''', 'role': 'user'}

ninvaders_game_player3 = {'content': '''left''', 'role': 'assistant'}


NINVADERS_GAME_PROMPT = [ninvaders_game_sys_prompt, ninvaders_game_comp1, ninvaders_game_player1, ninvaders_game_comp2,
                         ninvaders_game_player2, ninvaders_game_comp3, ninvaders_game_player3]


"""===============================================================SNAKE_FEW_SHOT_COMPARISON_STATE======================================================"""

snake_few_shot_comparison_state_sys_prompt = snake_state_sys_prompt

snake_few_shot_comparison_state_comp1 = {'content': '''
this is the first state: 

|------------------------------------------------------------------------------|
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                 $                                                            |
|                 I                                                            |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                             Ss                                     #         |
|                          ss s                                                |
|                            s                                                 |
|                                                                              |
|                                                                              |
|------------------------------------------------------------------------------|

this is the second state:

|------------------------------------------------------------------------------|
|$25                                                                           |
|                                                                              |
|                                                               $              |
|                                                                              |
|                 I                                                            |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                             Ss                                     #         |
|                          ss s                                                |
|                            s                                                 |
|                                                                              |
|                                                                              |
|------------------------------------------------------------------------------|

please assistant, compare the two states and tell me if the second is better or worse than the second''', 'role': 'user'}

snake_few_shot_comparison_state_player1 = {'content': '''the second state is better than the first one because the score is higher as the player has caught the dollar''', 'role': 'assistant'}

snake_few_shot_comparison_state_comp2 = {'content': '''
this is the first state:
|------------------------------------------------------------------------------|
|$25                                                                           |
|                                                                              |
|                                                               $              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                ss                                            |
|                                  s                                           |
|                                   s  I                                       |
|                                  s                                           |
|                                 S                                            |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                    #         |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|------------------------------------------------------------------------------|

this is the second state: 

|------------------------------------------------------------------------------|
|$25                                                                           |
|                                                                              |
|                                                               $              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                 s                                            |
|                                  s                                           |
|                                   s I                                        |
|                                S s                                           |
|                                 s                                            |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                    #         |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|------------------------------------------------------------------------------|

please assistant, compare the two states and tell me if the second is better or worse than the second''', 'role': 'user'}

snake_few_shot_comparison_state_player2 = {'content': '''the second state is worse than the first one because the score is the same and the player is now closer to the snake''', 'role': 'assistant'}

snake_few_shot_comparison_state_comp3 = {'content': '''
|------------------------------------------------------------------------------|
|$100                                                                          |
|                                                                              |
|                                              #                               |
|                                                                              |
|                                I                                             |
|                                $                                             |
|                                    S                                         |
|                                     s                                        |
|                                      ss                                      |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|------------------------------------------------------------------------------|

this is the second state:

|------------------------------------------------------------------------------|
|$100                                                                          |
|                                                                              |
|                                              #                               |
|                                                                              |
|                               I                                              |
|                                $  S                                          |
|                                    s                                         |
|                                     s                                        |
|                                      ss                                      |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                                              |
|------------------------------------------------------------------------------|

please assistant, compare the two states and tell me if the second is better or worse than the second''', 'role': 'user'}

snake_few_shot_comparison_state_player3 = {'content': '''the second state is worse than the first one because the score is the same and in the first state, the player was
one move away from the dollar, now is two moves away''', 'role': 'assistant'}

SNAKE_FEW_SHOT_COMPARISON_STATE_PROMPT = [snake_few_shot_comparison_state_sys_prompt, snake_few_shot_comparison_state_comp1, snake_few_shot_comparison_state_player1,
                                          snake_few_shot_comparison_state_comp2, snake_few_shot_comparison_state_player2, snake_few_shot_comparison_state_comp3, snake_few_shot_comparison_state_player3]

#TODO guarda un po come comprimere e fare un po di preprocessing
# TODO pensare a fare la roa che avevo proposto a suo tempo, fare il time lapse del video del gioco,
# TODO deh 