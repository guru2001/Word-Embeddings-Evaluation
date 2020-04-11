from gensim.models import FastText
from smart_open import open
import re
file_name = "Stemming/Stem&cleaned1.txt"
f = open(file_name)
data = f.read()

sentences_strings_ted = []
for line in data.split('\n'):
	m = re.match(r'^(?:(?P<precolon>[^:]{,20}):)?(?P<postcolon>.*)$', line)
	sentences_strings_ted.extend(sent for sent in m.groupdict()['postcolon'].split('.') if sent)

# final_corpus = [for sentence in f if sentence.strip() !='']
# word_punctuation_tokenizer = nltk.WordPunctTokenizer()
# word_tokenized_corpus = [word_punctuation_tokenizer.tokenize(sent) for sent in final_corpus]

sentences_ted = []
for token in sentences_strings_ted:
	tokens = token.split()
	sentences_ted.append(tokens)


embedding_size = 60 ##embedding_size is the size of the embedding vector.
window_size = 40 #window_size is the size of the number of words
min_word = 5 #min_word, which specifies the minimum frequency of a word 
down_sampling = 1e-2 #most frequently occurring word will be down-sampled by a number specified by the down_sampling attribute

print(sentences_ted)

ft_model = FastText(sentences = sentences_ted,size=embedding_size,window=window_size,min_count=min_word,sample=down_sampling,sg=1,iter=10)
#sg defines if the parameter is skpgram or cbow



print(ft_model.most_similar("నీవు"))

print(ft_model.most_similar("అనే"))
