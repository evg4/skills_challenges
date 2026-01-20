def make_snippet(sentence):
    words = sentence.split(" ")
    if len(words) <= 5:
        return " ".join(words[0:5]) 
    else:
        return " ".join(words[0:5]) + "..."
    

