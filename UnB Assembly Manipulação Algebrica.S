.data
dobro: .string "Dobro:"
metade: .string "\nMetade:"



.text
li a7, 5         # read int
ecall
mv t0, a0        # move conteudo de a0 para t0

#multiplicação
li s0, 2       
mul t1, t0, s0   # dobro 

li a7, 4
la a0, dobro     # print string
ecall

li a7, 1         # print valor da multiplicação
mv a0, t1
ecall

# divisão
srai t2, t0, 1   # divisao por 2
                #SRAI (Deslocamento Aritmético Imediato para a Direita).
li a7, 4
la a0, metade    # print string
ecall

li a7, 1         # print valor da divisao
mv a0, t2  
ecall

li a7, 10        # Exit
ecall