from gensim.models import Word2Vec
from smart_open import open
import re
file_name = "test1.txt"
f = open(file_name)
data = f.read()




#sg defines if the parameter is skpgram or cbow
sentences_strings_ted = []
for line in data.split('\n'):
	m = re.match(r'^(?:(?P<precolon>[^:]{,20}):)?(?P<postcolon>.*)$', line)
	sentences_strings_ted.extend(sent for sent in m.groupdict()['postcolon'].split('.') if sent)

# final_corpus = [for sentence in f if sentence.strip() !='']
# word_punctuation_tokenizer = nltk.WordPunctTokenizer()
# word_tokenized_corpus = [word_punctuation_tokenizer.tokenize(sent) for sent in final_corpus]

sentences_ted = []
for sent_str in sentences_strings_ted:
	tokens = sent_str.split()
	sentences_ted.append(tokens)



embedding_size = 60 ##embedding_size is the size of the embedding vector.
window_size = 40 #window_size is the size of the number of words
min_word = 5 #min_word, which specifies the minimum frequency of a word 
down_sampling = 1e-2 #most frequently occurring word will be down-sampled by a number specified by the down_sampling attribute


w2v_model = Word2Vec(sentences = sentences_ted,size=100, window=5, min_count=1, workers=4)

print("అక్క")
print(w2v_model.wv.most_similar("అక్క"))
print("గుడ్డి")
print(w2v_model.wv.most_similar("గుడ్డి"))
print("ఆంగ్ల")
print(w2v_model.wv.most_similar("ఆంగ్ల"))
print("దృష్టి")
print(w2v_model.wv.most_similar("దృష్టి"))
print("అంతే")
print(w2v_model.wv.most_similar("అంతే"))
print("పెంచుకో")
print(w2v_model.wv.most_similar("పెంచుకో"))
print("సౌఖ్యంగా")
print(w2v_model.wv.most_similar("సౌఖ్యంగా"))
print("కొత్త")
print(w2v_model.wv.most_similar("కొత్త"))
print("కష్టం")
print(w2v_model.wv.most_similar("కష్టం"))
print("తాను")
print(w2v_model.wv.most_similar("తాను"))
