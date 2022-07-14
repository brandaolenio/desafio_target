'''Escreva um programa que inverta os caracteres de um string. IMPORTANTE: 
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;'''

def stranger_string(str):
    lista_string = [x for x in str]
    string_invertida = ''
    
    for i in lista_string:
        string_invertida = i + string_invertida
    
    return string_invertida

print(stranger_string('cuscuz é muito bom'))