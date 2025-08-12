#!/usr/bin/env python3
"""
Custom Wordlist Generator for Kali Linux
Author: Your Name
Date: 2023-11-15
"""

import itertools
import sys
import argparse
from datetime import datetime

def banner():
    print("""
    ██████╗ ██████╗ ███████╗██████╗ ███████╗██████╗ 
    ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗
    ██████╔╝██████╔╝█████╗  ██████╔╝█████╗  ██████╔╝
    ██╔═══╝ ██╔══██╗██╔══╝  ██╔══██╗██╔══╝  ██╔══██╗
    ██║     ██║  ██║███████╗██║  ██║███████╗██║  ██║
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    Custom Wordlist Generator - Kali Linux Edition
    """)

def generate_wordlist(base_words, transformations, min_length=4, max_length=12):
    wordlist = set()
    
    # Add base words
    for word in base_words:
        if min_length <= len(word) <= max_length:
            wordlist.add(word)
    
    # Apply transformations
    for word in base_words:
        # Case variations
        wordlist.add(word.lower())
        wordlist.add(word.upper())
        wordlist.add(word.capitalize())
        
        # Add numbers
        for i in range(100):
            wordlist.add(f"{word}{i}")
            wordlist.add(f"{word.capitalize()}{i}")
            wordlist.add(f"{i}{word}")
        
        # Common substitutions
        substitutions = {
            'a': ['@', '4'],
            'e': ['3'],
            'i': ['1', '!'],
            'o': ['0'],
            's': ['$', '5'],
            'l': ['1', '!'],
            't': ['7']
        }
        
        # Generate substitution variations
        for char in word.lower():
            if char in substitutions:
                for sub in substitutions[char]:
                    new_word = word.lower().replace(char, sub)
                    wordlist.add(new_word)
                    wordlist.add(new_word.capitalize())
    
    # Combine words (if multiple base words provided)
    if len(base_words) > 1:
        for combo in itertools.permutations(base_words, 2):
            combined = ''.join(combo)
            if min_length <= len(combined) <= max_length:
                wordlist.add(combined)
    
    # Apply custom transformations if provided
    if transformations:
        for transform in transformations:
            for word in list(wordlist):
                transformed = eval(f'word{transform}')  # Be careful with eval!
                if min_length <= len(transformed) <= max_length:
                    wordlist.add(transformed)
    
    return sorted(wordlist, key=lambda x: (len(x), x))

def save_wordlist(wordlist, filename):
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(f"{word}\n")
    print(f"\n[+] Wordlist saved to {filename}")
    print(f"[+] Total words generated: {len(wordlist)}")

def main():
    banner()
    parser = argparse.ArgumentParser(description='Custom Wordlist Generator')
    parser.add_argument('-b', '--base', nargs='+', required=True, help='Base words for wordlist')
    parser.add_argument('-o', '--output', default='custom_wordlist.txt', help='Output filename')
    parser.add_argument('-t', '--transform', nargs='+', help='Additional transformations (e.g. ".title()")')
    parser.add_argument('--min', type=int, default=4, help='Minimum password length')
    parser.add_argument('--max', type=int, default=12, help='Maximum password length')
    
    args = parser.parse_args()
    
    print("\n[+] Generating wordlist with the following parameters:")
    print(f"    Base words: {', '.join(args.base)}")
    print(f"    Output file: {args.output}")
    print(f"    Min length: {args.min}, Max length: {args.max}")
    if args.transform:
        print(f"    Transformations: {', '.join(args.transform)}")
    
    wordlist = generate_wordlist(args.base, args.transform, args.min, args.max)
    save_wordlist(wordlist, args.output)

if __name__ == "__main__":
    main()