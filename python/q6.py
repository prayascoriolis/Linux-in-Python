'''6.	Develop a script that validates if a given string is a valid email address.'''

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    return False

if __name__ == "__main__":
    emails = "prayas.kumar@coriolis.co.in"
    print(f"{emails}: {is_valid_email(emails)}")
