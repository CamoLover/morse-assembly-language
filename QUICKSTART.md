# Morse Assembly Language - Quick Start Guide

## What is Morse Assembly Language?

Morse Assembly Language (MAL) is an esoteric programming language where you write Assembly code using only dots (.) and dashes (-) - like Morse code

## Quick Example

Here's "Hello" in regular assembly vs Morse Assembly:

**Regular Assembly:**
```asm
MOV AX, 72
OUT AX
```

**Morse Assembly:**
```morse
-- --- ...- / .- -..- / --..-- / --... ..---
--- ..- - / .- -..-
```

## Getting Started

### 1. Write Regular Assembly (Optional)

Create a file `program.asm`:
```asm
MOV AX, 5
MOV BX, 3
ADD AX, BX
ADD AX, 48
OUT AX
HLT
```

### 2. Convert to Morse (Optional)

```bash
py morse_assembler.py program.asm program.morse
```

### 3. Run Your Program

```bash
py morse_interpreter.py program.morse
```

Output: `8`

## Understanding the Syntax

### Morse Encoding Rules

1. **Each character** is encoded as dots and dashes (e.g., `A` = `.-`)
2. **Characters in a word** are separated by **spaces**
3. **Words** are separated by **" / "** (space-slash-space)

### Example Breakdown

Let's decode: `-- --- ...- / .- -..-`

1. Split by " / ": `[-- --- ...-]` `[.- -..-]`
2. Split each word by spaces:
   - First word: `[--] [---] [...-]` = `M` `O` `V` = `MOV`
   - Second word: `[.-] [-..-]` = `A` `X` = `AX`
3. Result: `MOV AX`

## Available Instructions

### Basic Operations
- `MOV` - Move data
- `ADD` - Addition
- `SUB` - Subtraction
- `OUT` - Output
- `HLT` - Stop program

### Jumps & Labels
```asm
LOOP:
    OUT AX
    INC AX
    CMP AX, 10
    JNE LOOP
HLT
```

### Registers
- `AX`, `BX`, `CX`, `DX` - General purpose
- `SP` - Stack pointer
- `IP` - Instruction pointer

## Try It Yourself!

### Decode Some Morse
```bash
python3 morse_interpreter.py --decode ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
```

### Encode Some Text
```bash
python3 morse_interpreter.py --encode "HELLO WORLD"
```

## Tips for Writing MAL

1. Start with regular assembly
2. Use the assembler to convert to Morse
3. Test with the interpreter
4. For debugging, use the `--decode` flag to see what your morse code means

## Why MAL?

- **Educational**: Learn Assembly and Morse code
- **Challenging**: Try writing complex programs
- **Fun**: It's an esoteric language and it's assembly but harder
- **Historical**: Honors the legacy of Morse code

## Next Steps

1. Read through the example programs
2. Modify them to do different things
3. Write your own programs
4. Challenge yourself to write directly in Morse!

---

... .- -... -.-- / -.-. --- -.. .. -. --. -.-.--