# Morse Assembly Language (MAL)

An esoteric programming language where Assembly code is written entirely in Morse code

## Overview

Morse Assembly Language (MAL) is an Assembly-like language where every instruction, register, and value is encoded in Morse code. Programs are stored in `.morse` files and executed by the MAL interpreter.

## Features

- Full Assembly-style instruction set
- Registers: AX, BX, CX, DX, SP, IP
- Arithmetic, logic, comparison, and jump operations
- Stack operations
- Simple I/O
- Labels for control flow

## Installation

No installation needed! Just run the Python scripts:

```bash
chmod +x morse_interpreter.py morse_assembler.py
```

## Usage

### Running a Morse Assembly Program

```bash
py morse_interpreter.py program.morse
```

### Converting Regular Assembly to Morse

```bash
py morse_assembler.py input.asm output.morse
```

### Encoding/Decoding Text

```bash
# Encode text to morse
py morse_interpreter.py --encode "Hello World"

# Decode morse to text
py morse_interpreter.py --decode ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
```

## Syntax

### Character Encoding
- Individual morse characters are separated by spaces
- Words/tokens are separated by " / " (space-slash-space)
- Lines are separated by newlines

### Example
```
Regular Assembly:  MOV AX, 72
Morse Assembly:    -- --- ...- / .- -..- / --..-- / --... ..---
```

## Instruction Set

### Data Movement
- `MOV dest, src` - Move value from source to destination
- `PUSH value` - Push value onto stack
- `POP dest` - Pop value from stack to destination

### Arithmetic
- `ADD dest, src` - Add source to destination
- `SUB dest, src` - Subtract source from destination
- `MUL value` - Multiply AX by value
- `DIV value` - Divide AX by value
- `INC dest` - Increment destination
- `DEC dest` - Decrement destination

### Logic
- `AND dest, src` - Bitwise AND
- `OR dest, src` - Bitwise OR
- `XOR dest, src` - Bitwise XOR
- `NOT dest` - Bitwise NOT

### Comparison and Jumps
- `CMP a, b` - Compare two values
- `JMP label` - Unconditional jump
- `JE label` - Jump if equal (zero flag set)
- `JNE label` - Jump if not equal
- `JG label` - Jump if greater
- `JL label` - Jump if less

### I/O
- `OUT value` - Output value (as ASCII if 0-127)
- `IN dest` - Read input to destination

### Control
- `HLT` - Halt execution

## Example Programs

### Hello World (Regular Assembly)
```asm
MOV AX, 72     ; H
OUT AX
MOV AX, 101    ; e
OUT AX
MOV AX, 108    ; l
OUT AX
OUT AX         ; l
MOV AX, 111    ; o
OUT AX
HLT
```

### Hello World (Morse Assembly)
```morse
-- --- ...- / .- -..- / --..-- / --... ..---
--- ..- - / .- -..-
-- --- ...- / .- -..- / --..-- / .---- ----- .----
--- ..- - / .- -..-
-- --- ...- / .- -..- / --..-- / .---- ----- ---..
--- ..- - / .- -..-
--- ..- - / .- -..-
-- --- ...- / .- -..- / --..-- / .---- .---- .----
--- ..- - / .- -..-
.... .-.. -
```

## Morse Code Reference

### Letters
```
A .-    B -...  C -.-.  D -..   E .
F ..-.  G --.   H ....  I ..    J .---
K -.-   L .-..  M --    N -.    O ---
P .--.  Q --.-  R .-.   S ...   T -
U ..-   V ...-  W .--   X -..-  Y -.--
Z --..
```

### Numbers
```
0 -----  1 .----  2 ..---  3 ...--  4 ....-
5 .....  6 -....  7 --...  8 ---..  9 ----.
```

### Special Characters
```
, --..--  (comma)
: ---...  (colon)
/ -..-.   (slash)
```

## Architecture

The MAL Virtual Machine provides:
- 5 general-purpose registers (AX, BX, CX, DX) + SP, IP
- 1024 cells of memory
- Stack
- CPU flags (Zero, Sign, Carry)
- Label resolution for jumps

## Why?

I hate my life that's why

## License

Feel free to use, modify, and share! Nobody gonna use this anyway

## Contributing

Found a bug? Probably yes