import spacy
from read_write_create import *

nlp = spacy.load('en')

# Add neural coref to SpaCy's pipe
import neuralcoref

neuralcoref.add_to_pipe(nlp)

# You're done. You can now use NeuralCoref as you usually manipulate a SpaCy document annotations.

data_path = '/home/nayan/coding/Major/EasySearch/venv/data'

for every_file in (os.listdir(data_path)):
	print(every_file)
	doc = nlp(read_text_from_file(data_path, every_file))

	write_text_to_file(data_path, every_file, doc._.coref_resolved)
	#print(doc._.coref_clusters)
	#print(doc._.coref_resolved)
