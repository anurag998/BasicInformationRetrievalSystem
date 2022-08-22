from util import *
import nltk

# Add your import statements here




class InflectionReduction:
    def reduce(self, text):
        """
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""
        sno = nltk.stem.SnowballStemmer('english')
        reducedText = []
        for sentences in text:
            temp = []
            for words in sentences:
                temp.append(sno.stem(words))
            reducedText.append(temp)
        return reducedText

# stemm = InflectionReduction()
# listt = stemm.reduce([['I', "can't", 'do', 'anything', 'grows', 'ponies'], ['Hello', 'World', 'I', 'am', 'anurag'], ['ccc', 'has', 'a', 'book'], ['Hello', 'people'], ['No', 'doubt'], ['good', 'morning']])
# print(listt)