#!/usr/bin/env python3
"""
Morse Assembly Assembler
Converts regular assembly code to Morse Assembly Language
"""

import sys

class MorseEncoder:
    """Encodes text to Morse code"""
    
    CHAR_TO_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',
        '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-',
        '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-',
        '!': '-.-.--', '.': '.-.-.-', '-': '-....-', 'X': '-..-',
        '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    
    @classmethod
    def encode_line(cls, text: str) -> str:
        """Encode a line of assembly to morse code"""
        # Remove comments
        if ';' in text:
            text = text.split(';')[0]
        
        text = text.strip()
        if not text:
            return ''
        
        # Split by comma for operands
        # Keep spaces, commas, and colons
        result = []
        current_word = []
        
        for char in text:
            if char == ',':
                if current_word:
                    word = ''.join(current_word).strip()
                    if word:
                        result.append(cls.encode_word(word))
                    current_word = []
                result.append(cls.CHAR_TO_MORSE[','])
            elif char == ':':
                if current_word:
                    word = ''.join(current_word).strip()
                    if word:
                        result.append(cls.encode_word(word))
                    current_word = []
                result.append(cls.CHAR_TO_MORSE[':'])
            elif char == ' ':
                if current_word:
                    word = ''.join(current_word).strip()
                    if word:
                        result.append(cls.encode_word(word))
                    current_word = []
            else:
                current_word.append(char)
        
        # Don't forget the last word
        if current_word:
            word = ''.join(current_word).strip()
            if word:
                result.append(cls.encode_word(word))
        
        return ' / '.join(result)
    
    @classmethod
    def encode_word(cls, word: str) -> str:
        """Encode a single word to morse"""
        morse_chars = []
        for char in word.upper():
            if char in cls.CHAR_TO_MORSE:
                morse_chars.append(cls.CHAR_TO_MORSE[char])
            elif char == ' ':
                continue
        return ' '.join(morse_chars)


def assemble_file(input_file: str, output_file: str):
    """Assemble a regular assembly file to morse assembly"""
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
        
        morse_lines = []
        for line in lines:
            morse_line = MorseEncoder.encode_line(line)
            if morse_line:
                morse_lines.append(morse_line)
        
        with open(output_file, 'w') as f:
            f.write('\n'.join(morse_lines))
        
        print(f"Successfully assembled {input_file} -> {output_file}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) < 3:
        print("Usage: python morse_assembler.py <input.asm> <output.morse>")
        print("\nConverts regular assembly code to Morse Assembly Language")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    assemble_file(input_file, output_file)


if __name__ == '__main__':
    main()
