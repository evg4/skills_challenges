def reading_estimate(string):
    num_of_words = len(string.split())
    mins = num_of_words/200
    seconds = mins*60
    print(f"num of words: {num_of_words} mins: {mins}, seconds: {seconds}")
    return f"{int(seconds)} seconds"


