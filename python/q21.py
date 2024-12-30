'''21. Write a program to implement a spell checker using the dictionary lookup.'''

import difflib

# dictionary of correctly spelled words
dictionary = set([
    "hello", "world", "apple", "banana", "computer", "python", "programming", "data", "science", "machine", "learning"
])

def check_spelling(word):
    """Check if a word is in the dictionary. If not, suggest close matches."""
    if word in dictionary:
        return f"'{word}' is spelled correctly."
    else:
        suggestions = difflib.get_close_matches(word, dictionary, n=3, cutoff=0.6)
        if suggestions:
            return f"'{word}' is not found. Did you mean: {', '.join(suggestions)}?"
        else:
            return f"'{word}' no close matches were found for this word."

def spell_check(text):
    """Check the spelling of each word in the text."""
    results = check_spelling(text)
    return results

if __name__ == "__main__":
    input_text = "helloo"
    print(spell_check(input_text))

    input_text = "python"
    print(spell_check(input_text))

    input_text = "sciance"
    print(spell_check(input_text))
