#!/usr/bin/env python3
"""
This script updates the project's changelog with a new entry for the current date.
It reads changelog entries from standard input or a file and writes them to CHANGELOG.md.
"""

def update_changelog():
 """
 Reads new changelog entries and appends them to the existing CHANGELOG.md file.
 """
 # Open the changelog file for appending
 with open('CHANGELOG.md', 'a') as changelog_file:
 # Get the new changelog entries from input
 new_entry = input("Enter changelog entries: ")
 # Append current date and new entries to the changelog
 changelog_file.write(f"\n## [Unreleased]\n### {datetime.date.today()}\n{new_entry}\n")

if __name__ == "__main__":
 import datetime
 # Call the update function
 update_changelog()
