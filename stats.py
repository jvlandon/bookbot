        
def get_word_count(words):
    return len(words.split())

def symbols(words):
    letters_dict = {}
    for letter in words.lower():
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict

def sort_on(items):
    return items["num"]

def list_out(characters):
    alpha = []
    for ch, count in characters.items():
        alpha.append({"char": ch, "num": count})
    alpha.sort(reverse=True, key=sort_on)
    return alpha


    