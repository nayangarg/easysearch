import csv
import networkx as nx
import nltk
from nltk.stem import PorterStemmer
from ast import literal_eval

ps = PorterStemmer()

G = nx.Graph()
rdr = csv.reader(open('knoGraph.csv', 'r'))
rdr = list(rdr)
for i in rdr:
    G.add_edge(i[0], i[1], weight=float(i[2]))

rdr = csv.reader(open('index1.csv', 'r'))
rdr = list(rdr)

d = dict()

for i in rdr:
    d[i[0]] = i[1:]

q = input()

q = q.lower()
words = nltk.word_tokenize(q)
words = [ps.stem(i) for i in words]

l = len(words)

q = words[0]

for i in range(1, l):
    q = q + '-' + words[i]

nbr = sorted(G.edges(nbunch=q, data=True), key=lambda t: t[2].get('weight', 1))[::-1]

for i in range(len(d[q])):
    d[q][i] = literal_eval(d[q][i])
d[q].sort(key=lambda x: x[1])

vis = []

for i in d[q][:8]:
    vis.append(i[0][:-4])
    print(i[0][:-4])

y = 8

for n in nbr[:7]:
    print(n[1])
    if n[1] not in d.keys():
        continue
    for i in range(len(d[n[1]])):
        d[n[1]][i] = literal_eval(d[n[1]][i])
    d[n[1]].sort(key=lambda x: [1])

    j = 1

    for i in d[n[1]]:
        if i[0][:-4] in vis:
            continue
        vis.append(i[0][:-4])
        print(i[0][:-4])
        j += 1
        if j >= y:
            break
    y -= 1
