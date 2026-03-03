# MAL Example Programs

This directory contains example programs demonstrating various features of Morse Assembly Language.

## Running Examples

To run any example:
```bash
py ../src/morse_interpreter.py example.morse
```

To assemble from .asm to .morse:
```bash
py ../src/morse_assembler.py example.asm example.morse
```

## Available Examples

### hello.asm / hello.morse
Classic "Hello" program demonstrating basic output.
- Uses MOV and OUT instructions
- Outputs ASCII characters

### calculator.asm / calculator.morse
Simple arithmetic calculator demonstration.
- Shows arithmetic operations (ADD, SUB)
- Uses multiple registers

### counter.asm / counter.morse
Counting demonstration with loops.
- Uses labels and jump instructions
- Demonstrates CMP and JNE for control flow

### fibonacci.asm / fibonacci.morse
Fibonacci sequence generator.
- More complex control flow
- Multiple register usage
- Stack operations

## Learning Path

1. Start with `hello.asm` - understand basic output
2. Try `calculator.asm` - learn arithmetic operations
3. Move to `counter.asm` - understand loops and jumps
4. Finally `fibonacci.asm` - combine all concepts

## Modifying Examples

Feel free to modify these examples! To test your changes:

1. Edit the .asm file
2. Reassemble with morse_assembler.py
3. Run with morse_interpreter.py
