# Executar o script como sudo na maquina remota
import os

grupos = ["grp01", "grp02", "grp03", "grp04", "grp05", "grp06",
          "grp07", "grp08", "grp09", "grp10", "grp11", "grp12"]

os.system("ipcs -m > log.txt")

f = open("log.txt", "r")
linhas = f.readlines()
f.close()

for linha in linhas:
	dados = linha.split(" ")
	
	if len(dados) > 4:
		shmid = dados[1]
		grupo = dados[3]

		if grupo in grupos:
			comando = "ipcrm -m " + shmid
			os.system(comando)

os.system("rm -rf log.txt")