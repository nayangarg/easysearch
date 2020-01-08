from glove import Corpus, Glove
import csv

corpus = Corpus()

# rdr = csv.reader(open('/home/nayan/coding/Major/sCake Phrase/venv/wordList/52795.csv', 'r'))
#
# print(list(rdr))

data_path = '/home/nayan/coding/Major/sCake Phrase/venv/wordList'

for every_file in (os.listdir(data_path)):
