# 0.

import os
import re
import nltk
import string
import pandas as pd
from read_write_create import *
from nltk.stem import PorterStemmer
# from nltk.stem import WordNetLemmatizer
import unicodedata
import csv
from read_write_create import *

global cwd, path, data_path

def convert_text_to_sentences(text):
    return nltk.sent_tokenize(text)

cwd = os.getcwd()
path = cwd
data_path = cwd + "/data"
create_folder(cwd, "positions")

newline_ex = re.compile("\n")
hyphen = re.compile("-")
numbers_ex = re.compile("[0-9]+(-[0-9]+)?")
punctuation_ex = re.compile("[^a-z ]")
roman_num_ex = re.compile("\\b[i|v|x|l|c|d|m]{1,3}\\b")
stopwords = read_list_from_file(path, "stopwords.txt")
ps = PorterStemmer()
# lemmatizer = WordNetLemmatizer()

print("create-position-info-sCake")
# li = ['255519.txt']
for every_file in (os.listdir(data_path)):

    print(every_file)
    text = read_text_from_file(data_path, every_file)
    text = re.sub(newline_ex, ' ', text)
    text = re.sub(hyphen, ' ', text)
    text = unicode(text, errors='replace')
    sen = convert_text_to_sentences(text)

    ## pre-processing text
    text = text.strip()
    text = text.lower()
    text = re.sub(numbers_ex, '', text)
    text = re.sub(punctuation_ex, '', text)
    text = re.sub(roman_num_ex, '', text)

    words = nltk.word_tokenize(text)
    #print(words)
    words = [i for i in words if i not in stopwords]
    words = [ps.stem(i) for i in words]
    # words = [lemmatizer.lemmatize(i) for i in words]

    l = len(words)
    i = 0

    while i < l:
        #print(i,l)
        if len(words[i]) < 3:
            words.pop(i)
            i -= 1
            l -= 1
        i += 1
    # print(type(i))

    # print(words)

    bigrams = nltk.collocations.BigramAssocMeasures()
    bigramFinder = nltk.collocations.BigramCollocationFinder.from_words(words)
    # x = []
    # for k, v in bigramFinder.ngram_fd.items():
    #     if (v<3):
    #         x.append(k)
            # print(k, v)
    # print(bigramFinder.ngram_fd["(u'except', u'ada')"])

    bigramFinder.apply_freq_filter(4)
    # print(bigramFinder.ngram_fd["(u'except', u'asynchron')"])
    bi = list(bigramFinder.score_ngrams(bigrams.pmi))

    # for b in bi:
    #     if b[0] == "(u'except', u'asynchron')":
    #         print('bfrdsn')

    # for k, v in bigramFinder.ngram_fd.items():
    #     if (v==2):
    #         print(k, v)

    
    # print(bi)
    # bigramPMITable = pd.DataFrame(list(bigramFinder.score_ngrams(bigrams.pmi)), columns=['bigram', 'PMI']).sort_values(
    #     by='PMI', ascending=False)

    # print(bigramPMITable[:50])

    trigrams = nltk.collocations.TrigramAssocMeasures()
    trigramFinder = nltk.collocations.TrigramCollocationFinder.from_words(words)
    # for k, v in trigramFinder.ngram_fd.items():
    #     if (v >= 2):
    #         print(k, v)
    trigramFinder.apply_freq_filter(4)
    # trigramPMITable = pd.DataFrame(list(trigramFinder.score_ngrams(trigrams.pmi)),
    #                                columns=['trigram', 'PMI']).sort_values(by='PMI', ascending=False)

    tri = list(trigramFinder.score_ngrams(trigrams.pmi))
    # print(tri)

    #     unicodedata.normalize('NFKD', t[0][0]).encode('ascii', 'ignore')
    #     unicodedata.normalize('NFKD', t[0][1]).encode('ascii', 'ignore')
    #     unicodedata.normalize('NFKD', t[0][2]).encode('ascii', 'ignore')

    # print(biG)



    l = len(sen)
    # print(sen[0])

    s = 0
    new_sen = sen[s].strip()
    new_sen = new_sen.lower()
    new_sen = re.sub(numbers_ex, '', new_sen)
    new_sen = re.sub(punctuation_ex, '', new_sen)
    new_sen = re.sub(roman_num_ex, '', new_sen)
    # print(new_sen)
    sen_words = nltk.word_tokenize(new_sen)
    # print(sen_words)

    sen_words = [i for i in sen_words if i not in stopwords]
    # print(sen_words)
    sen_words = [ps.stem(sw) for sw in sen_words]
    # print(sen_words)

    if sen_words == []:
        last = ''
    else:
        last = sen_words[-1]

    #print(i)
    new_sen = (sen[s+1]).strip()
    new_sen = new_sen.lower()
    new_sen = re.sub(numbers_ex, '', new_sen)
    new_sen = re.sub(punctuation_ex, '', new_sen)
    new_sen = re.sub(roman_num_ex, '', new_sen)
    # print(new_sen)
    sen_words = nltk.word_tokenize(new_sen)
    # print(sen_words)

    sen_words = [i for i in sen_words if i not in stopwords]
    # print(words)
    sen_words = [ps.stem(sw) for sw in sen_words]
    # print(sen_words)

    if sen_words == []:
        first = ''
    else:
        first = sen_words[0]
    # print(words)

    w = 0
    while w < len(words) - 2:
        # print('bahar', w, len(words))
        for b in bi:
            # print(b)
            if s < l-1 and last == b[0][0] and first == b[0][1]:
                s += 1
                if sen_words == []:
                    last = ''
                else:
                    last = sen_words[-1]
                new_sen = sen[s + 1].strip()
                new_sen = new_sen.lower()
                new_sen = re.sub(numbers_ex, '', new_sen)
                new_sen = re.sub(punctuation_ex, '', new_sen)
                new_sen = re.sub(roman_num_ex, '', new_sen)
                # print(new_sen)
                sen_words = nltk.word_tokenize(new_sen)
                # print(words)

                sen_words = [i for i in sen_words if i not in stopwords]
                # print(words)
                sen_words = [ps.stem(sw) for sw in sen_words]

                if sen_words == []:
                    first = ''
                else:
                    first = sen_words[0]
                continue

            # print('andar', w, len(words))
            if words[w] == b[0][0] and words[w + 1] == b[0][1]:

                f = 0
                for t in tri:
                    if b[0][0] == t[0][0] and b[0][1] == t[0][1]:

                        if s < l - 1 and last == t[0][1] and first == t[0][2]:
                            s += 1
                            if sen_words == []:
                                last = ''
                            else:
                                last = sen_words[-1]
                            new_sen = sen[s + 1].strip()
                            new_sen = new_sen.lower()
                            new_sen = re.sub(numbers_ex, '', new_sen)
                            new_sen = re.sub(punctuation_ex, '', new_sen)
                            new_sen = re.sub(roman_num_ex, '', new_sen)
                            # print(new_sen)
                            sen_words = nltk.word_tokenize(new_sen)
                            # print(words)

                            sen_words = [i for i in sen_words if i not in stopwords]
                            # print(words)
                            sen_words = [ps.stem(sw) for sw in sen_words]
                            if sen_words == []:
                                first = ''
                            else:
                                first = sen_words[0]
                            continue

                        f = 1
                        words[w] = words[w] + '-' + words[w + 1] + '-' + words[w + 2]
                        # words[w] = words[w].encode('utf-8')
                        words.pop(w + 1)
                        words.pop(w + 1)
                        break

                if f is 0:
                    words[w] = words[w] + '-' + words[w + 1]
                    # words[w] = words[w].encode('utf-8')
                    words.pop(w + 1)

                break
        w += 1

    # print(words)

    #

    #
    # print(trigramPMITable[:50])
    #
    selected_words = list(set(words))

    # print(selected_words[:10])
    # print(selected_words)

    # for w in range(len(selected_words)):
    #     if selected_words[w] == 'except-asynchron':
    #         print(selected_words[w])

    ## end of pre-processing

    N = len(words) + 1
    posi = list()
    t = list()
    tf = list()

    for w in selected_words:

        if len(w) > 3:
            posw = [i for i, word in enumerate(words) if w == word]
            w_freq = len(posw) + 1
            posw.append(N)
            t.append(w)
            tf.append(w_freq)
            posi.append(posw)

    # print(posi)

    data = dict()
    data["words"] = t
    data["tf"] = tf
    data["positions"] = posi

    df = pd.DataFrame(data=data)

    print(df.head())
    df.to_pickle(cwd + "/positions/" + every_file[:-4] + ".pkl")
