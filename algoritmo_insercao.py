import time 
# Função do Algoritmo de Inserção
def algoritmoInsercao(arr):

	# Percorra de 1 até o número de casas que tem em len
	for i in range(1, len(arr)):

		key = arr[i]

		# Mova elementos de arr[0..i-1], que são
        # maior que chave, para uma posição à frente
        # de sua posição atual
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key

arrNumber = []



# abrindo arquivo numbers.txt
with open('a.in-500.txt', 'r') as arquivo:
    inicio = 0
    fim = 0
    arquivo = arquivo.read()
    arr = arquivo.split()
    n = len(arr)
    
    # percorrendo o array arr
    for num in arr:
        arrNumber.append(int(num))
        
    #mostrando o array desordenado 
    print("\n\nArray Desordenado: ")
    for i in range(n):
        print("%d" % arrNumber[i], end=" ")
    inicio = time.time()
    #chamando função algoritmo de Inserção
    algoritmoInsercao(arrNumber)
    fim = time.time()
    #mostrando o array desordenado 
    print("\n\nArray Ordernado: ")
    for i in range(n):
        print("%d" % arrNumber[i], end=" ")



#Criando resultsInsercao
results = open("a.out-Insert500.txt", "w")

results.write("tempo:" + str(fim - inicio))
results.write("\n\n" +str(arrNumber).replace("[", "").replace("]", "").replace(",", ""))

results.close()