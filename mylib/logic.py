import wikipedia

def wiki(name="war goddness", length=1):
    my_wiki = wikipedia.summary(name, length)
    return my_wiki
