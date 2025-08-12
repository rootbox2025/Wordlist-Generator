# Wordlist-Generator


git clone https://github.com/rootbox2025/Wordlist-Generator.git

How to Use This Tool:

    Save the script as custom_wordlist.py

    Make it executable: chmod +x custom_wordlist.py

    Run it with your parameters:

Basic Usage:
bash

./custom_wordlist.py -b name1 name2 -o my_wordlist.txt

Advanced Usage:
bash

./custom_wordlist.py -b john doe -t ".upper()" ".title()" --min 6 --max 16 -o john_wordlist.txt

Features:

    Base Words: Input any names or keywords you want to include

    Automatic Variations:

        Case variations (upper, lower, capitalize)

        Number appending (name1, name123, etc.)

        Leet speak substitutions (a->@, e->3, etc.)

    Custom Transformations: Apply Python string methods like .upper(), .title(), etc.

    Word Combination: Combines multiple base words in permutations

    Length Control: Set minimum and maximum password lengths

    Output File: Save to a specified filename

Requirements:

    Python 3 (pre-installed in Kali Linux)

    No additional dependencies needed

This tool will help you create targeted wordlists for password cracking, especially useful for CTFs or penetration testing engagements where you have some information about the target.
