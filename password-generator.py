#%%
from random import randint
character = input('Qual a quantidade de caracteres deve ter a senha?')
character = int(character)
generator = ("".join(chr(randint(33, 125)) for x in range(character)))
sentence = ("Senha gerada: {}").format(generator)

print(sentence)
#%%
