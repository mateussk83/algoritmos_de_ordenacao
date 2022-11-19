import time
# algoritmo de intercalação

numbers = [500, 5000, 10000, 20000, 50000]


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Chamada de cada metade
        mergeSort(left)
        mergeSort(right)

        # Dois iteradores para percorrer as duas metades
        i = 0
        j = 0
        
        # Iterador para a lista principal
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # O valor da metade esquerda foi usado
              myList[k] = left[i]
              # Move o iterador para frente
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Mover para o próximo slot
            k += 1

        # Para todos os valores restantes
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1


def orderNumbers(number):
         
    # abrindo arquivo numbers.txt
    with open('a.in-'+str(number)+'.txt', 'r') as arquivo:

        fim = 0
        inicio = 0
        arrNumber = []
        arquivo = arquivo.read()
        arr = arquivo.split()
        n = len(arr)

        for num in arr:
            arrNumber.append(int(num))

        print("\n\nArray Desordenado: ")
        for i in range(n):
            print("%d" % arrNumber[i], end=" ")

        inicio = time.time()
        mergeSort(arrNumber)

        fim = time.time()
        print("\n\nArray Ordernado: ")
        for i in range(n):
            print("%d" % arrNumber[i], end=" ")

    results = open('a.out-Merge'+str(number)+'.txt', "w")

    results.write("tempo:" + str(fim - inicio))
    results.write("\n\n" + str(arrNumber).replace("[", "").replace("]", "").replace(",", ""))
    results.close()


for num in numbers:
    orderNumbers(num)