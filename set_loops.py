def unique_strings(string):
    unique_chars = set()
    for char in string:
        if char not in unique_chars:
            unique_chars.add(char)
    return unique_chars

