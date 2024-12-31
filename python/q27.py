'''27. Write a function to get all matches from a file using a regular expression pattern (All dates, Hyperlinks, Capitalized words, email-id, IP address).'''

import re    

def match_pattern(text, category):
    pattern_dict = {
        'email': r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        'ip': r"[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*",
        'date': r"[0-9]{4}-[0-9]{2}-[0-9]{2}",
        'hyperlink': r"https://www\.[a-zA-Z0-9]+\.[a-zA-Z]+/[a-zA-Z0-9]+",
        'capital': r"[A-Z]+[a-z]+",
    }
    match = re.findall(pattern_dict[category], text)
    if match:
        return match
    else:
        return "No match found."

if __name__=="__main__":
    file_path = "./dir/log_file.txt"
    with open(file_path, 'r') as file:
        for line in file:
            input_str = line.strip()
            print('Required line:', input_str)
            print('Email matched:', match_pattern(input_str, 'email'))
            print('ip matched:', match_pattern(input_str, 'ip'))
            print('hyperlink matched:', match_pattern(input_str, 'hyperlink'))
            print('capital matched:', match_pattern(input_str, 'capital'))
            print('date matched:', match_pattern(input_str, 'date'))
            print('\n')
