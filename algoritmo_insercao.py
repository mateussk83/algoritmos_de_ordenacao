import time
# Função do Algoritmo de Inserção


numbers = [500, 5000, 10000, 20000, 50000]


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

def orderNumbers(number):

    # abrindo arquivo numbers.txt
    with open('a.in-'+str(number)+'.txt', 'r') as arquivo:
        arrNumber = []
        fim = 0
        inicio = 0
        arquivo = arquivo.read()
        arr = arquivo.split()
        n = len(arr)

        # percorrendo o array arr
        for num in arr:
            arrNumber.append(int(num))

        # mostrando o array desordenado
        print("\n\nArray Desordenado: ")
        for i in range(n):
            print("%d" % arrNumber[i], end=" ")
        inicio = time.time()
        # chamando função algoritmo de Inserção
        algoritmoInsercao(arrNumber)
        # Criando results Insercao
        fim = time.time()
        # mostrando o array desordenado
        print("\n\nArray Ordernado: ")
        for i in range(n):
            print("%d" % arrNumber[i], end=" ")

    results = open('a.out-Insert'+str(number)+'.txt', "w")

    results.write("tempo:" + str(fim - inicio))
    results.write(
        "\n\n" + str(arrNumber).replace("[", "").replace("]", "").replace(",", ""))

    results.close()


for num in numbers:
    orderNumbers(num)
