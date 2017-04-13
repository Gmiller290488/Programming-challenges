# Given a string of words and numbers
# check if there are 3 successive words"

def check_words(words):
    text = words.split()
    count = 0
    for word in text:
        if word.isnumeric() == False:
            count+=1
            if count == 3:
                return True
        else:
            count = 0
    return False


check_words("He is man")