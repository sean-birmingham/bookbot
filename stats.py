def get_num_words(text):
    return len(text.split())

def count_chars(text):
    char_counts = {}

    for char in text:
        char = char.lower()

        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
            
    return char_counts

def sort_on(dict):
    return dict["num"]

def sort_chars(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():  # Only include alphabetical characters
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list