import ast
import sys

def go_to_dialogue(id):
    scene = scenes[id]
    
    # if options is empty, it means this is a game_over dialogue
    if not scene["options"]:
        print(scene['dialogue'])
        sys.exit()
    
    i = 0
    user_prompt = scene['dialogue'] + "\n"
    # build a string with all the user's options
    for option in scene["options"]:
        user_prompt += str(i) + ". " + option['option_text'] + "\n"
        i += 1
    
    # loop through user inputs until they choose one of the options
    while True:
        user_choice = input(user_prompt)
        try:
            next_dialogue = scene["options"][int(user_choice)]
            break
        except IndexError:
            print("{} was not a valid choice".format(user_choice))
        
    go_to_dialogue(next_dialogue['next_scene'])
    
if __name__ == "__main__":
    with open('adventure_1.txt', 'r') as f:
        raw = f.read()
        scenes = ast.literal_eval(raw)
    go_to_dialogue(1)