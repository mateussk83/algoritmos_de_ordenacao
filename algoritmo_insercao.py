import time
# Função do Algoritmo de Inserção


numbers = [500, 5000, 10000, 20000, 50000]


def algoritmoInsercao(arr):
    n = len(arr)
    # Percorre o arranjo A.
    for j in range(1, n):
        chave = arr[j]
        i = j - 1
        # Insere o elemento A[j] na posição correta.
        while i >= 0 and arr[i] > chave:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = chave


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
