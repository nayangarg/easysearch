from glove import Corpus, Glove
import csv

corpus = Corpus()
data_path = '/home/test/EasySearch/venv/wordList'

import os
import pandas as pd
import numpy as np
import networkx as nx
import operator
G = nx.Graph()

class Neighbor:
    def __init__(self, word, dist):
        self.word = word
        self.dist = dist
        
wordDocHsh = dict()

for every_file in (os.listdir(data_path)):
    print(every_file)
    df = pd.read_csv(open('/home/test/EasySearch/venv/SCScore_W/'+every_file[:-4]+"_ranked_list.csv", 'r'))
    key = list(df['Words'][:50])
    
    lines = list(csv.reader(open(data_path + '/' + every_file, 'r')))

    corpus.fit(lines, window=10)
    glove = Glove(no_components=300, learning_rate=0.01)

    glove.fit(corpus.matrix, epochs=50, no_threads=4, verbose=True)
    glove.add_dictionary(corpus.dictionary)
    
    
    
    for i in key:
        
        if i in wordDocHsh:
            wordDocHsh[i].append(every_file)
        else:
            wordDocHsh[i] = [every_file]
        
        if i not in glove.dictionary.keys():
            continue

        edges = []
        for j in key:
            if j not in glove.dictionary.keys() or i is j:
                continue
            edges.append(Neighbor(j, np.linalg.norm(glove.word_vectors[glove.dictionary[i]] - glove.word_vectors[glove.dictionary[j]])))

        edges.sort(key=operator.attrgetter('dist'))

        l = len(edges)
        if not G.has_node(i):
            G.add_node(i)
        #G[i][docs].append(data_path + '/' + every_file)        

        for j in range(0,l):
            if G.has_edge(i, edges[-j].word):
                G[i][edges[-j].word]['weight'] += 1/(j+1)
            else:
                G.add_edge(i, edges[-j].word, weight = 1/(j+1))
                
sortEdg = sorted(G.edges(data=True), key=lambda t: t[2].get('weight', 1),reverse = True)
cwd = os.getcwd()
edge_list = G.edges().data()
edgelist = []
for i in list(edge_list):
    tup = (i[0],i[1],i[2]['weight'])
    edgelist.append(tup)
    
df = pd.DataFrame(edgelist)
df.to_csv(cwd + "/knoGraph.csv", header=False, index=False)

hsh = pd.DataFrame.from_dict(wordDocHsh, orient='index')

hsh.to_csv(cwd + "/index.csv", header=True, index=True)