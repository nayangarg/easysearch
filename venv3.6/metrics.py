from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
from read_write_create import *
import csv
import pandas as pd
import os
import re
from nltk.util import ngrams


def generate_ngrams(s, n, sep):
    
    tokens = [token for token in s.split(sep) if token != ""]
    
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]

def glist(fil):
    gold_list=[]
    #keyword_list=[]
    # for every_file in (os.listdir(gold_data)):
        #file_name = every_file[:-4]
    with open(gold_data+'/'+fil, "r") as f:
        reader = csv.reader(f)
        reader=list(reader)
    #print(reader)
    l = len(reader)
    
    for row in reader:
        for word in row:
            word=word.replace("-"," ")            
            gold_list.append(" ".join([ps.stem(i) for i in word.split()]))

    #print(gold_list)
    gold=[]
    for word in gold_list:
        tokens=word.split(" ")
        for i in range(1,len(tokens)+1):
            gold.append(generate_ngrams(word,i," "))

    g = []
    for i in gold:
        for j in i:
            g.append(j)

    gold = []
    for i in g:
    #     for j in range(0,len(gold[i])):
        if ' ' in i:
            gold.append(i.replace(" ","-"))
            gold.append(i.replace(" ",""))
        else:
            gold.append(i)
            
    gold = set(gold)
            
    #print(gold)

    return [gold, l]
    
#print(gold)
def extList(fil, k):
    #gold_list=[]
    keyword_list=[]
    # for every_file in (os.listdir(gold_data)):
        #file_name = every_file[:-4]
    with open(phrase_data+'/'+fil, "r") as f:
        reader = csv.reader(f)
        reader=list(reader)
    #print(reader)
    for i in range(1,k+1):
        #if(int(reader[i][0])<=len(reader[:k])):
        keyword_list.append(reader[i][4])

    #print(gold_list)
    gold=[]
    for word in keyword_list:
        tokens=word.split("-")
        for i in range(1,len(tokens)+1):
            gold.append(generate_ngrams(word,i,'-'))
            
    #print(gold)

    g = []
    for i in gold:
        for j in i:
            g.append(j)

    gold = []
    for i in g:
    #     for j in range(0,len(gold[i])):
        if ' ' in i:
            gold.append(i.replace(" ","-"))
            gold.append(i.replace(" ",""))
        else:
            gold.append(i)
            
    gold = set(gold)
            
    #print(gold)

    return [gold, k]

def main():

	global cwd, path, phrase_data, gold_data, ps

	cwd=os.getcwd()
	path=cwd
	phrase_data= "/home/nayan/coding/Major/EasySearch/venv/SCScore_W"
	gold_data= "/home/nayan/coding/Major/EasySearch/venv/keys"

	ps = PorterStemmer()

	k = 10
	rec = 0
	#k = 8
	prec = 0
	for every_file in (os.listdir(gold_data)):
	    #print(every_file)
	    [g,l] = glist(every_file)
	    [ext,k] = extList(every_file[:-4]+'_ranked_list.csv',k)
	    #print(g,ext)
	    r=0
	    for i in g:
	        if i in ext:
	            #print(i)
	            r += 1
	    #print(r,l)
	    r /= l
	    rec += r

	    p=0
	    for i in ext:
	        if i in g:
	            #print(i)
	            p += 1
	    #print(r,l)
	    p /= k
	    prec += p

	rec /= 2304
	prec /= 2304

	f1 = 2*prec*rec
	f1 /= prec+rec

	return f1