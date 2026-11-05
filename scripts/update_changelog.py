import json
import random

def load_quotes(filename):
    """Load the quotes from a JSON file.

    Args:
        filename (str): The path to the quotes JSON file.

    Returns:
        list: A list of quotes.
    """
    with open(filename, 'r') as file:
        quotes = json.load(file)
    return quotes

def add_random_quote(quotes, new_quote):
    """Add a new random quote to the list of quotes.

    Args:
        quotes (list): The list of existing quotes.
        new_quote (str): The new quote to add.

    Returns:
        list: The updated list of quotes.
    """
    quotes.append(new_quote)
    return quotes

def save_quotes(filename, quotes):
    """Save the updated quotes to a JSON file.

    Args:
        filename (str): The path to the quotes JSON file.
        quotes (list): The list of quotes to save.
    """
    with open(filename, 'w') as file:
        json.dump(quotes, file, indent=2)

def main():
    """Main function to manage the quotes workflow."""
    quotes_file = 'json/quotes.json'
    quotes = load_quotes(quotes_file)

    new_quote = "This is a new random quote."
    quotes = add_random_quote(quotes, new_quote)

    save_quotes(quotes_file, quotes)

if __name__ == "__main__":
    main()