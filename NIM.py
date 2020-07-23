import time

def computador_escolhe_jogada(n_pecas,maximo):
	"""int, int -> int"""
	print("Vez do computador")
	time.sleep(1) #Da uma fluidez para o jogo 
	i = 1
	while i < maximo:
		if ((n_pecas-i) % (maximo+1) == 0): #Verifica se é multiplo
			return i
		i = i + 1
	return maximo 	

def usuario_escolhe_jogada(n_pecas,maximo):
	"""int, int -> int"""
	jogada = int(input("Qual a sua jogada? "))
	while jogada > maximo or jogada <= 0 or n_pecas-jogada < 0 : 
		print("Jogada Invalida")
		jogada = int(input("Qual a sua jogada? "))
	return jogada

def situacao_atual(n_pecas, removidas):
	pecas_atualizada = n_pecas - removidas
	print("Número de peças removidas:",removidas)
	print ("Número de peças restantes: {}\n".format(pecas_atualizada))
	return pecas_atualizada


def campeonato():
	i = 0
	while i < 3:
		cont = 0 
		cont = cont + partida()
		i = i + 1
	print("Placar:Você",cont,"X",3-cont,"Computador")		

def partida():
	peças = int(input("Quantidade de peças: "))
	jogadas = int(input("Máximo de peças possíveis de retirar: "))

	if (peças%(jogadas+1) == 0): # Se for multiplo o usuario comeca
		print("Você começa\n")
		removidas =  usuario_escolhe_jogada(peças,jogadas)
		peças = situacao_atual(peças, removidas)
		if peças == 0:
			print("Você ganhou!\n")
			return 1
	else:
		print("\nComputador começa\n")	
	while  peças > 0		
		removidas = computador_escolhe_jogada(peças, jogadas)
		peças = situacao_atual(peças, removidas)
		if peças == 0:
			print("O computador ganhou!\n")
			return 0
		else:
			removidas =  usuario_escolhe_jogada(peças,jogadas)
			peças = situacao_atual(peças, removidas)
			if peças == 0:
				print("Você ganhou!\n")
				return 1

if __name__ == "__main__":					
	print("Partida: Digite 1    Campeonato: Digite 2")
	menu = int(input())
	if	menu == 1:
		partida()
	if menu == 2:
		campeonato()