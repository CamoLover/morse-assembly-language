# Morse Assembly Language (MAL)

## Overview
Morse Assembly Language (MAL) is an esoteric programming language where all code is written in Morse code. It follows Assembly-like syntax and semantics.

## File Extension
`.morse`

## Character Encoding

### Letters
- A: .-
- B: -...
- C: -.-.
- D: -..
- E: .
- F: ..-.
- G: --.
- H: ....
- I: ..
- J: .---
- K: -.-
- L: .-..
- M: --
- N: -.
- O: ---
- P: .--.
- Q: --.-
- R: .-.
- S: ...
- T: -
- U: ..-
- V: ...-
- W: .--
- X: -..-
- Y: -.--
- Z: --..

### Numbers
- 0: -----
- 1: .----
- 2: ..---
- 3: ...--
- 4: ....-
- 5: .....
- 6: -....
- 7: --...
- 8: ---..
- 9: ----.

### Special Characters
- & (Ampersand): .-...
- ' (Apostrophe): .----.
- @ (At sign): .--.-.
- ) (Close parenthesis): -.--.-
- ( (Open parenthesis): -.--.
- : (Colon): ---...
- , (Comma): --..--
- = (Equals): -...-
- ! (Exclamation): -.-.--
- . (Period): .-.-.-
- - (Hyphen): -....-
- × (Multiplication/x): -..-
- % (Percentage): ----- -..-. -----
- + (Plus): .-.-.
- " (Quote): .-..-.
- ? (Question): ..--..
- / (Slash): -..-.

## Syntax Rules

1. **Character Separation**: Individual Morse characters are separated by a single space
2. **Word Separation**: Words/tokens are separated by " / " (space-slash-space)
3. **Line Separation**: Lines are separated by newlines

## Assembly Instructions

### Registers
- AX, BX, CX, DX (general purpose)
- SP (stack pointer)
- IP (instruction pointer)

### Basic Instructions

#### Data Movement
- `MOV dest, src` - Move data from source to destination
- `PUSH value` - Push value onto stack
- `POP dest` - Pop value from stack

#### Arithmetic
- `ADD dest, src` - Add src to dest
- `SUB dest, src` - Subtract src from dest
- `MUL value` - Multiply AX by value
- `DIV value` - Divide AX by value
- `INC dest` - Increment dest
- `DEC dest` - Decrement dest

#### Logic
- `AND dest, src` - Bitwise AND
- `OR dest, src` - Bitwise OR
- `XOR dest, src` - Bitwise XOR
- `NOT dest` - Bitwise NOT

#### Comparison and Jumps
- `CMP a, b` - Compare two values
- `JMP label` - Unconditional jump
- `JE label` - Jump if equal
- `JNE label` - Jump if not equal
- `JG label` - Jump if greater
- `JL label` - Jump if less

#### I/O
- `OUT value` - Output value
- `IN dest` - Input to destination

#### Control
- `CALL label` - Call subroutine
- `RET` - Return from subroutine
- `HLT` - Halt execution

### Syntax Format
```
INSTRUCTION / OPERAND1 / OPERAND2
```

### Labels
Labels end with a colon:
```
LABEL:
```

### Comments
Comments start with semicolon (not in morse, just planning):
```
; This is a comment
```

## Example Program

### Hello World (in regular Assembly)
```asm
START:
    MOV AX, 72    ; H
    OUT AX
    MOV AX, 101   ; e
    OUT AX
    MOV AX, 108   ; l
    OUT AX
    OUT AX        ; l
    MOV AX, 111   ; o
    OUT AX
    HLT
```

### Same in Morse
```morse
... - .- .-. - ---... / -- --- ...- / .- -..- --..-- / --... ..--- / --- ..- - / .- -..-
-- --- ...- / .- -..- --..-- / .---- ----- .---- / --- ..- - / .- -..-
-- --- ...- / .- -..- --..-- / .---- ----- ---.. / --- ..- - / .- -..-
--- ..- - / .- -..-
-- --- ...- / .- -..- --..-- / .---- ----- .---- .---- / --- ..- - / .- -..-
.... .-.. -
```

## Implementation Notes

The interpreter should:
1. Parse the morse code into tokens
2. Build an instruction list
3. Execute instructions with a virtual machine that maintains:
   - Register state
   - Memory array
   - Stack
   - Instruction pointer
   - Flags (Zero, Sign, Carry, etc.)