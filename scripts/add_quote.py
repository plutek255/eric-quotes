"""A script to add a new quote to the quotes.json file."""

import json
from pathlib import Path
from datetime import datetime

QUOTES_FILE = Path('json/quotes.json')

def add_quote(author, text, context="No context", description="No description"):
    """Add a new quote to the quotes.json file."""
    with QUOTES_FILE.open('r+', encoding='utf-8') as file:
        data = json.load(file)
        quote_id = datetime.now().isoformat()
        data['quotes'][quote_id] = {
            "author": author,
            "name": text,
            "context": context,
            "description": description
        }
        file.seek(0)
        json.dump(data, file, ensure_ascii=False, indent=4)
    print("Quote added successfully.")

if __name__ == "__main__":
    # Example usage
    add_quote("Eric", "Always preface your advice with 'over the years' to make it sound wise.", "Reflective advice", "Sharing experience")
