def get_num_words(file_contents):
    counter = 0
    words = file_contents.split()
    for word in words:
        counter += 1
    return counter

def get_num_chars(file_contents):
    num_chars = {}
    all_chars = file_contents.lower()
    for char in all_chars:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def sort_on(item):
    return item["num"]

def get_sorted_list(num_chars):
    dlist = []
    for key, value in num_chars.items():
        if key.isalpha():
            dict = {"char": key, "num": value}
            dlist.append(dict)
    dlist.sort(reverse=True, key=sort_on)
    return dlist



    
        