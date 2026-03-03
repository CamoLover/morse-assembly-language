; Fibonacci sequence generator  
; Prints first 6 Fibonacci numbers (0-8 as single ASCII digits)

MOV AX, 0      ; First number
MOV BX, 1      ; Second number  
MOV CX, 6      ; Counter

LOOP:
MOV DX, AX     ; Copy number to DX
ADD DX, 48     ; Convert to ASCII
OUT DX         ; Output as character
MOV DX, AX     ; Save AX  
ADD AX, BX     ; AX = AX + BX (next fib number)
MOV BX, DX     ; BX = old AX
DEC CX         ; Decrement counter
CMP CX, 0      ; Check if done
JNE LOOP       ; If not zero, continue
HLT
