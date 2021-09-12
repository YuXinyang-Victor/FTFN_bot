from msg_type_greetings import msg_type_greetings_enum
from msg_type_talktome import msg_type_talktome_enum
import importlib
from list_of_types import list_of_types

from enum import Enum

def respond(input_text):
    parsed_input_text = input_parsing(input_text)
    input_type = classify_input(parsed_input_text)
    response = handle_response(input_type, parsed_input_text)
    return response

def classify_input(input_text):
    
    user_msg = str(input_text).lower()
    i = -1
    for input_type in list_of_enums_local:
        i = i + 1
        if input_text in input_type._member_names_:
            return i
    return -1

def handle_response(input_type, input_text):                        #input type is passed by classify_input(), should be an int. input text is string, passed by main handle function
    if (input_type == -1): 
        response = "I am sorry, doctor, but I cannot understand what you just said. "
    else: 
        inputtype = list_of_types[input_type]
                                                                    #print(inputtype)    ---DEBUG LINE
        response = inputtype.handle_dictionary.get(input_text)
    
                                                                    #print("infunc: response = ", response)  ---DEBUG LINE
    return response

def input_parsing(input_text):                                      #take out all the spaces and replace with underscore

    parsed_text = '_'.join(input_text.split())
                                                                    #print("parsed text is:" + parsed_text)     ---DEBUG LINE
    return parsed_text

list_of_enums_local = [msg_type_greetings_enum,msg_type_talktome_enum]

