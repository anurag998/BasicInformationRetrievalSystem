from util import *
import nltk
from nltk.corpus import stopwords
# Add your import statements here




class StopwordRemoval():
    def fromList(self, text):
        """
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""
        stopwordRemovedText = []
        stop_words = set(stopwords.words('english'))
        
        for sentences in text:
            temp = []
            for words in sentences:
                if words not in stop_words:
                    temp.append(words)
            stopwordRemovedText.append(temp)

		#Fill in code here
        return stopwordRemovedText


# s = StopwordRemoval()
# listt = s.fromList([['i', "can't", 'do', 'anyth', 'grow'], ['hello', 'world', 'i', 'am', 'anurag'], ['ccc', 'has', 'a', 'book'], ['hello', 'peopl'], ['no', 'doubt'], ['good', 'morn']])
# print(listt)
	