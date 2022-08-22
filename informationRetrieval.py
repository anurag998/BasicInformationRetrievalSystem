from util import *
import pandas as pd
import numpy as np

# Add your import statements here




class InformationRetrieval():
    def __init__(self):
        self.index = None
        self.vocab = None
        self.docIDs = None
        self.vocab = None
    
    def buildIndex(self, docs, docIDs):
        """
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""
        idx = None
        self.docIDs = docIDs

        '''
        Creating the Vocabulary of the corpus
        '''
        vocab = []
        self.vocab = vocab
        #[[[], []], [[], []], [[], []]]
        for doc in range(len(docs)):
            for sen in docs[doc]:
                for word in sen:
                    if word not in self.vocab:
                        self.vocab.append(word)
        
        self.vocab.sort()
        
        '''
        Initializing the dataframe for the storing the tf-idf values for the words in vocab against the documents.
        '''
        idx = pd.DataFrame(data=np.zeros((len(self.vocab), len(self.docIDs) + 2)), index=self.vocab,columns=self.docIDs + ['n_i', 'idf'])

        
        for i in range(len(docs)):
            word_list = []
            for sent in docs[i]:
                for word in sent:
                    if word in self.vocab:
                        idx.loc[word, docIDs[i]] += 1 #calculating the tf value
                        if word not in word_list:
                            idx.loc[word, 'n_i'] += 1 # calculating the n_i value to be used for the idf value.
                            word_list.append(word)
        idx['idf'] = idx['n_i'].apply(lambda x: np.log10(len(docs) / x) if x > 0 else 0) #calculating the idf value.
        idx[docIDs] = idx[docIDs].mul(idx['idf'].to_numpy(), axis='rows') #storing the tf*idf values in the columns of the data frame.
        idx.pop('n_i') # following column is no longer required, but the idf is required.
                             
        self.index = idx
        print(self.docIDs)
        
    def rank(self, queries):
        """
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""
        doc_IDs_ordered = []

        '''
        Initializing the query_array
        '''
        query_array = []
        for i in range(len(self.vocab)):
            temp = []
            for j in range(len(queries)):
                temp.append(0)
            query_array.append(temp)
        
        
        '''
        Calculating the tf values for the queries.
        '''
        for q in range(len(queries)):
            for sen in queries[q]:
                for words in sen:

                    if words in self.vocab:
                        ind = self.vocab.index(words)

                        query_array[ind][q] = query_array[ind][q] + 1
        
        query_array = np.array(query_array)

        doc_arr = self.index.to_numpy()
        
        query_array = query_array*(doc_arr[:, -1].reshape((doc_arr.shape[0], 1))) #tf*idf value calculation
        
        sim = np.dot(doc_arr.T, query_array) #calculating the un normalized cosine similarity 

        
        '''
        Normalizing the cosine similarity.
        '''
        for i in range(sim.shape[0]):
            doc_i = doc_arr[:, i]
            doc_i_len =np.sqrt(np.dot(doc_i.T, doc_i))
            
            if doc_i_len!=0:
                sim[i] = sim[i]/doc_i_len
            else:
                sim[i] = 0
                
        
        for i in range(sim.shape[1]):
            query_i = query_array[:, i]
            query_i_len = np.sqrt(np.dot(query_i.T, query_i))
            
            if query_i_len!=0:
                sim[:, i] = sim[:, i]/query_i_len
            else:
                sim[i] = 0
        
        '''
        Sorting each column of the cosine similarity matrix and storing the document ids.
        '''
        ordered_rank = np.argsort(sim, axis = 0)
        
        ordered_rank = np.flipud(ordered_rank)
        ordered_rank = ordered_rank+1
        
        
        '''
        Generating the list ot be returned containing lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
        '''
        for i in range(ordered_rank.shape[1]):
            doc_IDs_ordered.append(ordered_rank[:, i].tolist())
        return doc_IDs_ordered



