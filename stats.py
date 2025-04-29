def get_num_words(text:str):
    return len(text.split())

def get_num_chars(text:str):
    occurances = {}
    for ch in text:
        if ch.lower() not in occurances:
            occurances[ch.lower()] = 1
        else:
            occurances[ch.lower()] += 1
    return occurances

    
