from util import *
from nltk.tokenize.treebank import TreebankWordTokenizer
# Add your import statements here




class Tokenization():
    def naive(self, text):
        """
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""
        tokenizedText = []
        
        for sentences in text:
            size = len(sentences)
            i = 0
            temp = ''
            new_list = []
            while(i < size):
                if(sentences[i]!= '.' and sentences[i]!= '?' and sentences[i]!= '!' and sentences[i]!= ' '):
                    temp+=sentences[i]
                else:
                    new_list.append(temp)
                    temp = ''
                    while( i+1 < size and (sentences[i+1]== '.' or sentences[i+1]== '?' or sentences[i+1]== '!' or sentences[i+1]== ' ')):
                        i+=1
                i+=1
            if(temp != ''):
                new_list.append(temp)
            tokenizedText.append(new_list)
        
        
        

		#Fill in code here
        return tokenizedText
    
    def pennTreeBank(self, text):
        """
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""
        
                # Fill in code here
        penn = TreebankWordTokenizer()
        tokenizedText = []
        for sentence in text:
            tokenizedText.append(penn.tokenize(sentence))



        return tokenizedText
    
# t = Tokenization()
# listt = t.pennTreeBank(["I can't do anything", 'Hello World...    I am anurag.', 'ccc has a book.', 'Hello people?', 'No doubt!', 'good morning.'])
# print(listt)