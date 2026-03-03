#!/usr/bin/env python3
"""
Morse Assembly Language (MAL) Interpreter
An esoteric programming language where Assembly is written in Morse code
"""

import sys
from typing import Dict, List, Optional, Union

class MorseDecoder:
    """Converts Morse code to text"""
    
    # Morse code mapping
    MORSE_TO_CHAR = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7',
        '---..': '8', '----.': '9',
        '.-...': '&', '.----.': "'", '.--.-.': '@', '-.--.-': ')',
        '-.--.': '(', '---...': ':', '--..--': ',', '-...-': '=',
        '-.-.--': '!', '.-.-.-': '.', '-....-': '-', '-..-': 'X',
        '.-.-.': '+', '.-..-.': '"', '..--..': '?', '-..-.': '/'
    }
    
    CHAR_TO_MORSE = {v: k for k, v in MORSE_TO_CHAR.items()}
    
    @classmethod
    def decode(cls, morse_code: str) -> str:
        """Decode morse code to text"""
        # Split by word separator " / "
        words = morse_code.split(' / ')
        result = []
        
        for word in words:
            if not word.strip():
                continue
            # Split by character separator (space)
            chars = word.split(' ')
            word_result = ''
            for char in chars:
                if char.strip() in cls.MORSE_TO_CHAR:
                    word_result += cls.MORSE_TO_CHAR[char.strip()]
            result.append(word_result)
        
        return ' '.join(result)
    
    @classmethod
    def encode(cls, text: str) -> str:
        """Encode text to morse code"""
        words = text.split(' ')
        morse_words = []
        
        for word in words:
            morse_chars = []
            for char in word.upper():
                if char in cls.CHAR_TO_MORSE:
                    morse_chars.append(cls.CHAR_TO_MORSE[char])
            if morse_chars:
                morse_words.append(' '.join(morse_chars))
        
        return ' / '.join(morse_words)


class MorseVM:
    """Virtual Machine for executing Morse Assembly"""
    
    def __init__(self):
        # Registers
        self.registers = {
            'AX': 0, 'BX': 0, 'CX': 0, 'DX': 0,
            'SP': 1000, 'IP': 0
        }
        
        # Memory (1024 cells)
        self.memory = [0] * 1024
        
        # Stack
        self.stack = []
        
        # Flags
        self.flags = {
            'ZF': False,  # Zero flag
            'SF': False,  # Sign flag
            'CF': False   # Carry flag
        }
        
        # Labels
        self.labels = {}
        
        # Instructions
        self.instructions = []
        
        # Halt flag
        self.halted = False
        
    def load_program(self, morse_code: str):
        """Load and parse a morse assembly program"""
        lines = morse_code.strip().split('\n')
        
        for line_num, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            
            # Decode the morse line
            decoded = MorseDecoder.decode(line)
            
            # Check for label
            if ':' in decoded:
                label_name = decoded.split(':')[0].strip()
                self.labels[label_name] = len(self.instructions)
                # If there's more after the colon, process it
                after_colon = ':'.join(decoded.split(':')[1:]).strip()
                if after_colon:
                    decoded = after_colon
                else:
                    continue
            
            # Parse instruction - split by comma and then by space
            parts = [p.strip() for p in decoded.replace(',', ' ').split()]
            if parts:
                self.instructions.append(parts)
    
    def execute(self):
        """Execute the loaded program"""
        while not self.halted and self.registers['IP'] < len(self.instructions):
            instruction = self.instructions[self.registers['IP']]
            self.execute_instruction(instruction)
            self.registers['IP'] += 1
    
    def execute_instruction(self, parts: List[str]):
        """Execute a single instruction"""
        if not parts:
            return
        
        cmd = parts[0].upper()
        
        # Data Movement
        if cmd == 'MOV':
            dest, src = parts[1], parts[2]
            self.set_value(dest, self.get_value(src))
        
        elif cmd == 'PUSH':
            value = self.get_value(parts[1])
            self.stack.append(value)
            self.registers['SP'] -= 1
        
        elif cmd == 'POP':
            if self.stack:
                value = self.stack.pop()
                self.set_value(parts[1], value)
                self.registers['SP'] += 1
        
        # Arithmetic
        elif cmd == 'ADD':
            dest = parts[1]
            src = self.get_value(parts[2])
            result = self.get_value(dest) + src
            self.set_value(dest, result)
            self.update_flags(result)
        
        elif cmd == 'SUB':
            dest = parts[1]
            src = self.get_value(parts[2])
            result = self.get_value(dest) - src
            self.set_value(dest, result)
            self.update_flags(result)
        
        elif cmd == 'MUL':
            value = self.get_value(parts[1])
            result = self.registers['AX'] * value
            self.registers['AX'] = result & 0xFFFFFFFF  # Keep 32-bit
            self.update_flags(result)
        
        elif cmd == 'DIV':
            value = self.get_value(parts[1])
            if value != 0:
                self.registers['AX'] = self.registers['AX'] // value
                self.update_flags(self.registers['AX'])
        
        elif cmd == 'INC':
            dest = parts[1]
            result = self.get_value(dest) + 1
            self.set_value(dest, result)
            self.update_flags(result)
        
        elif cmd == 'DEC':
            dest = parts[1]
            result = self.get_value(dest) - 1
            self.set_value(dest, result)
            self.update_flags(result)
        
        # Logic
        elif cmd == 'AND':
            dest = parts[1]
            src = self.get_value(parts[2])
            result = self.get_value(dest) & src
            self.set_value(dest, result)
            self.update_flags(result)
        
        elif cmd == 'OR':
            dest = parts[1]
            src = self.get_value(parts[2])
            result = self.get_value(dest) | src
            self.set_value(dest, result)
            self.update_flags(result)
        
        elif cmd == 'XOR':
            dest = parts[1]
            src = self.get_value(parts[2])
            result = self.get_value(dest) ^ src
            self.set_value(dest, result)
            self.update_flags(result)
        
        elif cmd == 'NOT':
            dest = parts[1]
            result = ~self.get_value(dest) & 0xFFFFFFFF
            self.set_value(dest, result)
            self.update_flags(result)
        
        # Comparison
        elif cmd == 'CMP':
            a = self.get_value(parts[1])
            b = self.get_value(parts[2])
            result = a - b
            self.update_flags(result)
        
        # Jumps
        elif cmd == 'JMP':
            label = parts[1]
            if label in self.labels:
                self.registers['IP'] = self.labels[label] - 1
        
        elif cmd == 'JE' or cmd == 'JZ':
            if self.flags['ZF']:
                label = parts[1]
                if label in self.labels:
                    self.registers['IP'] = self.labels[label] - 1
        
        elif cmd == 'JNE' or cmd == 'JNZ':
            if not self.flags['ZF']:
                label = parts[1]
                if label in self.labels:
                    self.registers['IP'] = self.labels[label] - 1
        
        elif cmd == 'JG':
            if not self.flags['ZF'] and not self.flags['SF']:
                label = parts[1]
                if label in self.labels:
                    self.registers['IP'] = self.labels[label] - 1
        
        elif cmd == 'JL':
            if self.flags['SF']:
                label = parts[1]
                if label in self.labels:
                    self.registers['IP'] = self.labels[label] - 1
        
        # I/O
        elif cmd == 'OUT':
            value = self.get_value(parts[1])
            # Try to print as character if in ASCII range
            if 0 <= value <= 127:
                print(chr(value), end='')
            else:
                print(value, end='')
        
        elif cmd == 'IN':
            try:
                value = int(input())
                self.set_value(parts[1], value)
            except:
                self.set_value(parts[1], 0)
        
        # Control
        elif cmd == 'HLT':
            self.halted = True
    
    def get_value(self, operand: str) -> int:
        """Get value from register or immediate"""
        operand = operand.strip().upper()
        if operand in self.registers:
            return self.registers[operand]
        try:
            return int(operand)
        except:
            return 0
    
    def set_value(self, dest: str, value: int):
        """Set value to register"""
        dest = dest.strip().upper()
        if dest in self.registers:
            self.registers[dest] = value & 0xFFFFFFFF
    
    def update_flags(self, result: int):
        """Update CPU flags based on result"""
        self.flags['ZF'] = (result == 0)
        self.flags['SF'] = (result < 0)


def main():
    if len(sys.argv) < 2:
        print("Usage: python morse_interpreter.py <file.morse>")
        print("\nOr use one of these options:")
        print("  --encode <text>  : Encode text to morse")
        print("  --decode <morse> : Decode morse to text")
        return
    
    if sys.argv[1] == '--encode':
        text = ' '.join(sys.argv[2:])
        print(MorseDecoder.encode(text))
        return
    
    if sys.argv[1] == '--decode':
        morse = ' '.join(sys.argv[2:])
        print(MorseDecoder.decode(morse))
        return
    
    # Load and execute morse file
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as f:
            morse_code = f.read()
        
        vm = MorseVM()
        vm.load_program(morse_code)
        vm.execute()
        print()  # Final newline
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
