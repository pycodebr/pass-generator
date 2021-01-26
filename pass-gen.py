import random

# Caracteres usados para formar senhas #
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '#@$%&*-=+/.'

# Agrupa todos os caracteres #
all = lower + upper + numbers + symbols

# Define tamanho da senha #
length = 16

# Gera senha #
password = "".join(random.sample(all, length))

# Mostra resultado #
print(password)