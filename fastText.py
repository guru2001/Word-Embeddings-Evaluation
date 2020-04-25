from gensim.models import FastText
from smart_open import open
import re
file_name = "test1.txt"
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


embedding_size = 100 ##embedding_size is the size of the embedding vector.
window_size = 5 #window_size is the size of the number of words
min_word = 6 #min_word, which specifies the minimum frequency of a word 
down_sampling = 1e-2 #most frequently occurring word will be down-sampled by a number specified by the down_sampling attribute


ft_model = FastText(sentences = sentences_ted,size=embedding_size,window=window_size,min_count=min_word,sample=down_sampling,sg=1,iter=10)
#sg defines if the parameter is skpgram or cbow

print(ft_model.vectors)

model3 = FastText(size=4, window=3, min_count=1)
model3.build_vocab(corpus_file='test1.txt')
total_words = model3.corpus_total_words
print(total_words)
# print("అక్క")
# print(ft_model.wv.most_similar("అక్క"))
# print("గుడ్డి")
# print(ft_model.wv.most_similar("గుడ్డి"))
# print("ఆంగ్ల")
# print(ft_model.wv.most_similar("ఆంగ్ల"))
# print("దృష్టి")
# print(ft_model.wv.most_similar("దృష్టి"))
# print("అంతే")
# print(ft_model.wv.most_similar("అంతే"))
# print("పెంచుకో")
# print(ft_model.wv.most_similar("పెంచుకో"))
# print("సౌఖ్యంగా")
# print(ft_model.wv.most_similar("సౌఖ్యంగా"))
# print("కొత్త")
# print(ft_model.wv.most_similar("కొత్త"))
# print("కష్టం")
# print(ft_model.wv.most_similar("కష్టం"))
# print("తాను")
# print(ft_model.wv.most_similar("తాను"))


