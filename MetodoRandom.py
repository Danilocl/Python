import random

#gera um número aleatório de 1 a 100
r = random.randint(1,100)
print(r)
heroes = ['Spider Man','Superman','Shazam','Thor','Iron Man','Capitão América','Hulk']

#escolhe uma palavra aleatória dentre as outras na lista passada
c = random.choice(heroes)
print(c)
#Embaralha a porra toda
random.shuffle(heroes)
print(heroes)
# gera um número aleatório em um intervalo (início,fim,intervalo)
print(random.randrange(0,12,2))

st = 'teste'

print(list(st))