; Counter program - counts from 1 to 5
MOV AX, 1
MOV BX, 5
LOOP:
MOV DX, AX
ADD DX, 48
OUT DX
INC AX
CMP AX, BX
JL LOOP
HLT