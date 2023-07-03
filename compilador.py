import re

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

def lexer(source_code):
    tokens = []
    current_position = 0

    # Expresiones regulares para reconocer los diferentes tokens
    patterns = [
        ('INICIO', r'Inicio'),
        ('FINSI', r'FinSi'),
        ('FIN', r'Fin'),
        ('LEER', r'Leer'),
        ('MOSTRAR', r'Mostrar'),
        ('SI', r'Si'),
        ('ENTONCES', r'Entonces'),
        ('REPETIR', r'Repetir'),
        ('HASTAQUE', r'HastaQue'),
        ('MIENTRAS', r'Mientras'),
        ('HACER', r'Hacer'),
        ('FINMIENTRAS', r'FinMientras'),
        ('PARA', r'Para'),
        ('DESDE', r'Desde'),
        ('HASTA', r'Hasta'),
        ('CONPASO', r'ConPaso'),
        ('FINPARA', r'FinPara'),
        ('ASIGNACION', r'='),

        ('NUMERO', r'\d+'),
        ('CADENA', r'".*?"'),
        ('BOOLEANO', r'Verdadero|Falso'),

        ('IDENTIFICADOR', r'[a-zA-Z][a-zA-Z0-9]*'),

        ('OPERADOR', r'\+|-|\*|/'),
        ('ESPACIO', r'[ \t\r\n]+'),
        ('OTRO', r'.'),
        ('ERROR', r'[^ \t\r\n]+'),
    ]

    compiled_patterns = [(token_type, re.compile(pattern)) for token_type, pattern in patterns]

    while current_position < len(source_code):
        match = None

        for token_type, pattern in compiled_patterns:
            regex = pattern
            match = regex.match(source_code, current_position)

            if match:
                value = match.group(0)
                if token_type != 'ESPACIO':
                    tokens.append(Token(token_type, value))
                break

        if not match:
            raise ValueError(f'Carácter no reconocido en posición {current_position}')

        current_position = match.end()

    return tokens

# Ejemplo de uso
source_code = 'Inicio\nLeer variable\nMostrar variable\nFin'
print(source_code)
tokens = lexer(source_code)

for token in tokens:
    print(f'Tipo: {token.token_type}, Valor: {token.value}')
