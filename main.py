from lexer import lexer
from sintactico import parser  # <-- aquí cambiamos 'parser' por 'sintactico'

def analizar_entrada(entrada):
    lexer.input(entrada)
    print("\nTokens:")
    for token in lexer:
        print(token)

    print("\nResultado del parser:")
    resultado = parser.parse(entrada)
    print("Resultado:", resultado)

if __name__ == '__main__':
    while True:
        entrada = input(">>> ")
        if entrada.lower() in ('salir', 'exit'):
            break
        analizar_entrada(entrada)
