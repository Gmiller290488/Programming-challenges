# Given text where the Capitol letters spell a message, return the secret message

import re
def find_message(text):
    message = ""
    text = re.sub(r'[^\w\s]','',text)
    for char in text:
        if char.islower() == False and char.isnumeric() == False:
            message += char
    print(message.replace(" ", ""))


find_message("33778687787YDSDYH8987WHDJK")


#Others solution:
def find_message(text):
    return ''.join([l for l in text if l.isupper()])
