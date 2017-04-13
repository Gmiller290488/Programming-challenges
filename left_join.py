# Given a set of words, join them together into directions but replace
# "right" with "left"

def left_join(phrases):
    new_phrases = ""
    for word in phrases:
        new_phrases += word.replace("right", "left")
        new_phrases += ","
    print(new_phrases[:-1])

left_join(("bright aright", "ok"))