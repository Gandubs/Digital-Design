;mux but input value should be such that output values are always xor of select pins

.include "/data/data/com.termux/files/home/m328Pdef.inc"

.equ a_0 = 1
.equ a_1 = 1
.equ a_2 = 1
.equ a_3 = 0

.equ SEG_ONE = 0b11111001  ; Representation of '1' on a seven-segment display

.def rC = r20    ; Register for select line C
.def rD = r21    ; Register for select line D
.def rResult = r22  ; Register for MUX result
.def rXOR = r23  ; Register for XOR result
.def rTemp = r24  ; Temporary register

ldi r16, 0b11111100
out DDRD, r16

ldi r16, 0b00000001
out DDRB, r16

ldi rC, 0  ; Set C = 0
ldi rD, 0  ; Set D = 0

loop:
    mov rTemp, rC
    lsl rTemp          ; Shift left C into carry
    rol rD             ; Rotate left D through carry into rTemp

    brcc mux0          ; If carry clear (C=0, D=0), branch to mux0
    breq mux1          ; If Z flag set (C=0, D=1), branch to mux1
    brmi mux2          ; If N flag set (C=1, D=0), branch to mux2
    rjmp mux3          ; Otherwise, jump to mux3 (C=1, D=1)

mux0:
    ldi rResult, a_0
    rjmp check_xor

mux1:
    ldi rResult, a_1
    rjmp check_xor

mux2:
    ldi rResult, a_2
    rjmp check_xor

mux3:
    ldi rResult, a_3
    rjmp check_xor

check_xor:
    ; Calculate XOR of C and D
    mov rTemp, rC
    eor rTemp, rD  ; rTemp = C ^ D
    mov rXOR, rTemp

    ; Compare MUX result with XOR result
    cp rResult, rXOR
    breq display_one
    rjmp next_combination

display_one:
    ; Write the number '1' to the seven-segment display
    ldi r17, SEG_ONE
    out PORTD, r17
    ldi r17, 0b00000000
    out PORTB, r17
    rjmp next_combination

next_combination:
    ; Increment D
    inc rD
    cpi rD, 2
    brne loop

    ; Increment C
    inc rC
    cpi rC, 2
    brne loop

end:
    ; End of program
    rjmp end

