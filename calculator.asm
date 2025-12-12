; Simple addition calculator
; Adds two numbers and outputs result as ASCII digits

MOV AX, 5      ; First number
MOV BX, 3      ; Second number
ADD AX, BX     ; AX = 5 + 3 = 8
ADD AX, 48     ; Convert to ASCII ('0' = 48)
OUT AX         ; Output the digit
HLT
