import matplotlib.pyplot as plt

palavras = ['500','5000','10000','20000','50000' ]
timeinsert = []
timeMerge = []

#abrindo os arquivos de resultados de inserção
resultsinsert500 = open('a.out-Insert500.txt') 
resultsinsert5000 = open('a.out-Insert5000.txt') 
resultsinsert10000 = open('a.out-Insert10000.txt') 
resultsinsert20000 = open('a.out-Insert20000.txt') 
resultsinsert50000 = open('a.out-Insert50000.txt') 

#pegando a primeira linha que tem o tempo
content500 = resultsinsert500.readlines()
value500  = content500[0]
content5000 = resultsinsert5000.readlines()
value5000  = content5000[0]
content10000 = resultsinsert10000.readlines()
value10000  = content10000[0]
content20000 = resultsinsert20000.readlines()
value20000  = content20000[0]
content50000 = resultsinsert50000.readlines()
value50000  = content50000[0]


#editando o valor tirando o tempo: e adcionando os valores no array de insert
value500 = round(float(str(value500).replace("tempo:","")),2)
timeinsert.append(value500 * 1000)
value5000 = round(float(str(value5000).replace("tempo:","")),2)
timeinsert.append(value5000 * 1000)
value10000 = round(float(str(value10000).replace("tempo:","")),2)
timeinsert.append(value10000 * 1000)
value20000 = round(float(str(value20000).replace("tempo:","")),2)
timeinsert.append(value20000 * 1000)
value50000 = round(float(str(value50000).replace("tempo:","")),2)
timeinsert.append(value50000 * 1000)

#abrindo os arquivos de resultados de Merge
resultsMerge500 = open('a.out-Merge500.txt') 
resultsMerge5000 = open('a.out-Merge5000.txt') 
resultsMerge10000 = open('a.out-Merge10000.txt') 
resultsMerge20000 = open('a.out-Merge20000.txt') 
resultsMerge50000 = open('a.out-Merge50000.txt') 

#pegando a primeira linha que tem o tempo
content500 = resultsMerge500.readlines()
value500  = content500[0]
content5000 = resultsMerge5000.readlines()
value5000  = content5000[0]
content10000 = resultsMerge10000.readlines()
value10000  = content10000[0]
content20000 = resultsMerge20000.readlines()
value20000  = content20000[0]
content50000 = resultsMerge50000.readlines()
value50000  = content50000[0]

#editando o valor tirando o tempo: e adcionando os valores no array de Merge
value500 = round(float(str(value500).replace("tempo:","")),2)
timeMerge.append(value500 * 1000)
value5000 = round(float(str(value5000).replace("tempo:","")),2)
timeMerge.append(value5000 * 1000)
value10000 = round(float(str(value10000).replace("tempo:","")),2)
timeMerge.append(value10000 * 1000)
value20000 = round(float(str(value20000).replace("tempo:","")),2)
timeMerge.append(value20000 * 1000)
value50000 = round(float(str(value50000).replace("tempo:","")),2)
timeMerge.append(value50000 * 1000)


#editando o grafico 
plt.plot(palavras, timeinsert, label="Algoritmo de Inserção")
plt.plot(palavras, timeMerge, label="Algoritmo de Intercalação" )
plt.legend()
plt.ylabel('Tempo(ms)',color='red')
plt.xlabel('Números',color='blue')
plt.axis(ymin=0, ymax=180000)
plt.title('Comparação de Ordenação')
plt.show()



