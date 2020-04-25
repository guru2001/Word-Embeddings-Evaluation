from gensim.models import Word2Vec
from smart_open import open
import re
file_name = "data_final.txt"
f = open(file_name)
data = f.read()




#sg defines if the parameter is skpgram or cbow
sentences_strings_ted = []
for line in data.split('\n'):
	m = re.match(r'^(?:(?P<precolon>[^:]{,20}):)?(?P<postcolon>.*)$', line)
	sentences_strings_ted.extend(sent for sent in m.groupdict()['postcolon'].split('.') if sent)

sentences_ted = []
for sent_str in sentences_strings_ted:
	tokens = sent_str.split()
	sentences_ted.append(tokens)


w2v_model = Word2Vec(sentences = sentences_ted,size=100, window=15, min_count=5, workers=4,sg=0)

fin = open("vocab.txt","r")

for i,lines in enumerate(fin):
	if i== 11590 or i == 12082 or i == 27354/2 - 1 or i == 0 or i == 1 or i == 6 or i == 17 or i == 16 or i == 60 or i == 59 or i == 20 or i == 19 or i == 70 or i == 24 or i == 7966:
		continue
	if i > 13690:
		break
	lines = lines.split()
	word = lines[0]
	print(word)
	print(w2v_model.wv.most_similar(word))