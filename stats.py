def count_words(text):
    words= text.split()
    return len(words)

def character_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sorted_list (dict_var):
    dict_list = []
    for x,y in dict_var.items(): 
            new_dict = {}
            new_dict["char"] = x
            new_dict["num"]= y
            dict_list.append(new_dict)
    
    dict_list.sort(reverse=True ,key=sort_on)
    
    return dict_list
    