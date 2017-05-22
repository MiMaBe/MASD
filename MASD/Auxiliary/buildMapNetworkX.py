import numpy as np
import networkx as nx


def writeMap(cmap, nRows, nCols):
    text = cmap.replace(' ', '')
    text = text.replace('SC', '-')
    text = text.replace('S', '-')
    text = text.replace('10', '%')
    text = text.replace('R', 'O')
    text = text.split('},{')
    text[0] = text[0].replace('{', '')
    text[-1] = text[-1].replace('}', '')
    text = "".join(list(map(lambda x: x + '\n', ["".join(row).replace(',', ' ') for row in text])))
    fileIn = open('map.txt', 'w')
    fileIn.write(text)
    fileIn.write('\n\n' + str(nRows) + ' x ' + str(nCols))
    fileIn.close()


cityMap1 = "{10, 10,  R, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10}," \
           "{10,  S,  S,  S,  SC, S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S, 10}," \
           "{10,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10}," \
           "{10,  S,  S, 10, 10,  S,  S,  S,  S,  S,  S, 10, 10,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S,  S,  S,  S,  S, 10, 10,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10, 10,  S,  S, 10}," \
           "{10,  S,  S, 10,  R,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S,  R, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, R, 10,  S,  S,  S, 10}," \
           "{10,  S,  S,  S,  S,  S,  S, 10, 10,  S,  S,  S,  S,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S,  S, 10}," \
           "{10,  S,  S,  S,  S,  S,  S, 10, 10,  S,  S,  S,  S,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S,  S, 10}," \
           "{10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10}"

cityMap2 = "{10, 10, 10, R, 10}," \
           "{10, S, S, S, 10}," \
           "{10, S, 10, SC, 10}," \
           "{10, R, 10, 10, 10}"

# 14x8
cityMap3 = "{10, 10,  R, 10, 10, 10, 10, 10}," \
           "{10,  S,  S,  S,  S,  S,  S, 10}," \
           "{10,  S,  S,  S,  S,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10}," \
           "{10,  S,  S, 10, 10,  S,  S, 10}," \
           "{10,  S,  S,  S,  S,  S,  S, 10}," \
           "{10,  S,  S,  S,  S,  S,  S, 10}," \
           "{10, 10,  R, 10, 10, 10,  R, 10}"

scout1_map3 = ['9','17','25','33','41','49','57','65','73','81','89','97','98','99','100','92','91','90','82','74','66',
               '58','50','42','34','26','18','10']
scout2_map3 = ['11','12','13','14','22','30','38','46','54','62','70','78','86','94','102','101','93','85','77','69',
               '61','53','45','37','29','21','20','19']

cityMap4 =     "{10, 10,  R, 10, 10, 10, 10, 10, 10, 10, 10, 10}," \
               "{10,  S,  S,  S,  SC, S,  S,  S,  S,  S,  S, 10}," \
               "{10,  S,  S,  S,  S,  S,  S,  S,  S,  S,  S, 10}," \
               "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10}," \
               "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10}," \
               "{10,  S,  S, 10, 10,  S,  S,  S,  S,  S,  S, 10}," \
               "{10,  S,  S, 10, 10,  S,  S,  S,  S,  S,  S, 10}," \
               "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10}," \
               "{10,  S,  S, 10,  R,  S,  S, 10, 10,  S,  S, 10}," \
               "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S,  R}," \
               "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10}," \
               "{10,  S,  S, 10, 10,  S,  S, 10, 10,  S,  S, 10}," \
               "{10,  S,  S,  S,  S,  S,  S, 10, 10,  S,  S, 10}," \
               "{10,  S,  S,  S,  S,  S,  S, 10, 10,  S,  S, 10}," \
               "{10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10}"

transformation = {'S': 0, '10': 1, 'R': 2, 'SC': 0}


###############  select map #################################################################
cityMap = cityMap4
#############################################################################################
text = cityMap.replace(' ', '').split('},{')
text[0] = text[0].replace('{', '')
text[-1] = text[-1].replace('}', '')

vec1 = list(map(lambda x: transformation[x], text[0].split(',')))
vec2 = list(map(lambda x: transformation[x], text[1].split(',')))
matrix = np.matrix([np.array(vec1), np.array(vec2)])
for i in range(2, len(text)):
    vec = list(map(lambda x: transformation[x], text[i].split(',')))
    matrix = np.vstack([matrix, np.array(vec)])

street = 0
building = 0
facts = []
nRows = np.shape(matrix)[0]
nCols = np.shape(matrix)[1]
writeMap(cityMap, nRows, nCols)
graph_facts = []
system_facts = []

G = nx.Graph()
G.add_nodes_from(range(nRows*nCols))

for i in range(nRows - 1):
    for j in range(nCols - 1):
        if matrix[i, j] == 0:
            system_facts.append('roadCell(' + str(nCols*i + j) + ').')
            if matrix[i, j + 1] == 0:
                G.add_edge(nCols * i + j, nCols * i + j + 1)
                graph_facts.append('edge(' + str(nCols * i + j) + ',' + str(nCols * i + j + 1) + ').')
            else:
                facts.append('accessTo(' + str(nCols * i + j) + ',' + str(nCols * i + j + 1) + ').')
                if matrix[i, j + 1] == 2:
                    facts.append('recyclingCenter(' + str(nCols * i + j + 1) + ').')
            if matrix[i + 1, j] == 0:
                G.add_edge(nCols * i + j, nCols * (i + 1) + j)
                graph_facts.append('edge(' + str(nCols * i + j) + ',' + str(nCols * (i + 1) + j) + ').')
            else:
                facts.append('accessTo(' + str(nCols * i + j) + ',' + str(nCols * (i + 1) + j) + ').')
                if matrix[i + 1, j] == 2:
                    facts.append('recyclingCenter(' + str(nCols * (i + 1) + j) + ').')
            if matrix[i, j - 1] == 0 :
                G.add_edge(nCols * i + j, nCols * i + j - 1)
                graph_facts.append('edge(' + str(nCols * i + j) + ',' + str(nCols * i + j - 1) + ').')
            else:
                facts.append('accessTo(' + str(nCols * i + j) + ',' + str(nCols * i + j - 1) + ').')
                if matrix[i, j - 1] == 2:
                    facts.append('recyclingCenter(' + str(nCols * i + j - 1) + ').')
            if matrix[i - 1, j] == 0:
                G.add_edge(nCols * i + j, nCols * (i - 1) + j)
                graph_facts.append('edge(' + str(nCols * i + j) + ',' + str(nCols * (i - 1) + j) + ').')
            else:
                facts.append('accessTo(' + str(nCols * i + j) + ',' + str(nCols * (i - 1) + j) + ').')
                if matrix[i - 1, j] == 2:
                    facts.append('recyclingCenter(' + str(nCols * (i - 1) + j) + ').')

#print(nx.shortest_path(G, source=G.nodes()[20]))
# Remove building cells
for node in G.nodes():
    if G.degree(node) == 0:
        G.remove_node(node)

facts_SP = []
visited_nodes = []

for node in G.nodes():
    dict = nx.shortest_path(G, source=node)

    for visited in visited_nodes:
        del dict[visited]

    for key in dict.keys():
        facts_SP.append('shortest(' + str(node) + ',' + str(key) + ',[' +
                     ','.join(list(map(lambda x: str(x), dict[key]))) + '],' + str(len(dict[key]) - 1) + ').')

    visited_nodes.append(node)

# Create system agent knowledge base
fileSystem = open('../systemKB.pl', 'w')
fileSysAux = open('systemAuxiliar.pl', 'r')
fileSystem.write('\nnCols(' + str(nCols) + ').' + '\ncolsXrows(' + str(nCols*nRows) +').\n')
fileSystem.write("".join(list(map(lambda x: x + '\n', sorted(system_facts)))))
fileSystem.write(fileSysAux.read())
fileSysAux.close()

# Create harvesters knowledge bases
fileOut = open('../harvesterKB.pl', 'w')
fileHAux = open('harvesterAuxiliar.pl', 'r')
fileOut.write("".join(list(map(lambda x: x + '\n', sorted(graph_facts)))))
fileOut.write("".join(list(map(lambda x: x + '\n', sorted(facts)))))
fileOut.write("".join(list(map(lambda x: x + '\n', facts_SP))))
fileSP = open('finalCode.pl', 'r')
code = fileSP.read()
fileOut.write('\n\n' + code)
fileSP.close()
fileOut.close()

# Create scouts knowledge bases
fileScout = open('../scoutsKB.pl', 'w')
fileSAux = open('scoutAuxiliar.pl', 'r')
fileScout.write(fileSAux.read())
fileSAux.close()
fileScout.write("".join(list(map(lambda x: x + '\n', sorted(graph_facts)))))
pathText = ''
for i in range(len(scout1_map3)):
    if i == len(scout1_map3) - 1:
        pathText = pathText + 'path(' + scout1_map3[i] + ',' + scout1_map3[0] + ',1).\n'
    else:
        pathText = pathText + 'path(' + scout1_map3[i] + ',' + scout1_map3[i+1] + ',1).\n'

for i in range(len(scout2_map3) - 1):
    if i == len(scout2_map3) - 1:
        pathText = pathText + 'path(' + scout2_map3[i] + ',' + scout2_map3[0] + ',2).\n'
    else:
        pathText = pathText + 'path(' + scout2_map3[i] + ',' + scout2_map3[i+1] + ',2).\n'
fileScout.write(pathText)
fileScout.close()
