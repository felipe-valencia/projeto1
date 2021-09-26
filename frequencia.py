# =====================================================================================
# Script para computar as frequencias
# =====================================================================================
# Esse script abre os arquivos de log da reunião do Google Meets e computa
# a frequencia dos alunos. O script necessita das informações correspondentes 
# ao nome da aula (ex: aula01) para o seu correto funcionamento.
#
# Para executa-lo:
#	python frequencia.py

from unicodedata import normalize
import os

# Para remover acentos dos nomes dos alunos
def remover_acentos(txt):
	return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def print_escreve(txt, f):
	print(txt)
	f.write(txt + "\n")

# Recebe a informação correspondente a aula
aula = input("Digite o nome da aula (ex: aula01): ")

# Verifica todos os arquivos de log do Meets e concatena as informações
linhas = []
for file in os.listdir():
	if file.startswith(aula):
		f = open(file, "r", encoding="utf8")
		linhasp = f.readlines()
		linhas = linhas + linhasp
		f.close()

presente = []	# Lista de alunos que escreveram "presente" no chat
pratica  = []	# Lista de alunos que escreveram "pratica" no chat
saida    = []	# Lista de alunos que escreveram "saida" no chat

for linha in linhas:
	linha = remover_acentos(linha)

	if "presente" in linha or "Presente" in linha:
		aluno = linha.split(":")[0]
		presente.append(aluno)

	if "pratica" in linha or "Pratica" in linha:
		aluno = linha.split(":")[0]
		pratica.append(aluno)	

	if "saida" in linha or "saida" in linha:
		aluno = linha.split(":")[0]
		saida.append(aluno)

presente.sort()
pratica.sort()
saida.sort()

presente = list(dict.fromkeys(presente))
pratica  = list(dict.fromkeys(pratica))
saida    = list(dict.fromkeys(saida))

# Arquivo de saída
f = open(aula + "_log.txt", "w")

print_escreve("=" * 90, f)
print_escreve("Alunos que enviaram 'presente' no chat", f)
print_escreve("=" * 90, f)

for aluno in presente:
	print_escreve(aluno, f)

print_escreve("=" * 90, f)
print_escreve("Alunos que enviaram 'pratica' no chat", f)
print_escreve("=" * 90, f)

for aluno in pratica:
	print_escreve(aluno, f)

print_escreve("=" * 90, f)
print_escreve("Alunos que enviaram 'saida' no chat", f)
print_escreve("=" * 90, f)

for aluno in saida:
	print_escreve(aluno, f)

f.close()