arquivo = 'prog.py'
#verifica se começou com a letra passada
teste = arquivo.startswith('p')
print(teste)
#verifica se terminou com a letra passada
teste1 = arquivo.endswith('py')
print(teste1)
resposta = 'SIM'
print(resposta)
#deixa a palavra em minúsculo
teste2 = resposta.lower()
print(teste2)
#deixa a palavra em maiúsculo
teste3 = resposta.upper()
print(teste3)
resposta2 = 'no'
print(resposta2.lower() in "sim yes no")

s = " HAVIA uma mafagafa que tinha 7 mafagafinhos a mafagafa morreu ficaram os 7 mafagafinhos a mafagafar sozinhos"
#find procura a palvra passada como parâmetro
print(s[1:6].lower())
s = s.replace('mafagafa','piranha')
s = s.lower().replace('havia','teste')
print(s.find('uma'))
print(s)

