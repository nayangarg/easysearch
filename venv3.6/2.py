import spacy
import nltk
from read_write_create import *

nlp = spacy.load('en')

import neuralcoref
neuralcoref.add_to_pipe(nlp)


data_path = '/home/nayan/coding/Major/EasySearch/venv/data'

doc = nlp(read_text_from_file(data_path, '125347.txt'))

write_text_to_file('/home/nayan/coding/Major/EasySearch/venv3.6', '125347_1.txt', doc._.coref_resolved)
print(doc._.coref_clusters)
#print(type(doc))

doc = str(doc)

sent = nltk.sent_tokenize(doc)

words = []

for sen in sent:
	s = nltk.word_tokenize(sen)
	for i in s:
		words.append(i)

write_list_to_file('/home/nayan/coding/Major/EasySearch/venv3.6', '125347_2.txt', words)