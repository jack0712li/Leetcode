def longest_matching_substring(text, regex):

    prefix, _, suffix = regex.partition('*')
    
    max_length = 0
    longest_substring = ""
    

    for i in range(len(text)):
        # If the current segment starts with the prefix
        if text[i:].startswith(prefix):
            # Search for the suffix starting from the end of the prefix
            for j in range(i + len(prefix), len(text) - len(suffix) + 1):
                # If a matching suffix is found
                if text[j:].startswith(suffix):
                    # Calculate the length of the current substring
                    current_length = j + len(suffix) - i
                    # Update the longest substring if the current one is longer
                    if current_length > max_length:
                        max_length = current_length
                        longest_substring = text[i:j + len(suffix)]
    
    return longest_substring