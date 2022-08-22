from util import *
from nltk.tokenize import punkt
import json
# Add your import statements here




class SentenceSegmentation():
    def naive(self, text):
        """
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""
        segmentedText = []        
        
        size = len(text)
        i = 0
        temp = ''
        while(i<size):
            
            if(text[i] != '.' and text[i]!= '?' and text[i]!= '!'):
                temp+=text[i]
            else:
                temp+=text[i]
                segmentedText.append(temp)
                temp = '' #? / .
                while(i+1 < size and text[i+1] == " "):
                    i+=1
                
            i+=1
        

		#Fill in code here
        return segmentedText
    
    def punkt(self, text):
        """
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

        # Fill in code here
        
        sent_splitter = punkt.PunktSentenceTokenizer()
        segmented_text = sent_splitter.tokenize(text)
        return segmented_text


# a = SentenceSegmentation()
# listt = a.punkt("Hello World...    I am anurag. ccc has a book. Hello people? No doubt! good morning.")
# print(listt)
