from util import relScore, dcg

# Add your import statements here




class Evaluation():
    def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""
        precision = -1
        ret=set(query_doc_IDs_ordered[:k])
        rel=set(true_doc_IDs)
        precision = len(list(ret.intersection(rel)))/k

		#Fill in code here
        return precision
    
    def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
        """
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""
        meanPrecision = -1
        sp=0
        for q_no in range(len(query_ids)):
            true_doc_IDs = []
            for query_dict in qrels:
                if int(query_dict['query_num']) == query_ids[q_no]:
                    true_doc_IDs.append(int(query_dict['id']))
            sp+=self.queryPrecision(doc_IDs_ordered[q_no],query_ids[q_no],true_doc_IDs,k)

		#Fill in code here
        meanPrecision=sp/len(query_ids)
        return meanPrecision
    
    def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""
        recall = -1
        if len(true_doc_IDs)==0:
            recall=0
        else:
            ret=set(query_doc_IDs_ordered[:k])
            rel=set(true_doc_IDs)
            recall = len(list(ret.intersection(rel)))/len(true_doc_IDs)
		#Fill in code here
        return recall
    
    def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
        """
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""
        meanRecall = -1
        sr=0
        for q_no in range(len(query_ids)):
            true_doc_IDs = []
            for query_dict in qrels:
                if int(query_dict['query_num']) == query_ids[q_no]:
                    true_doc_IDs.append(int(query_dict['id']))
            sr+=self.queryRecall(doc_IDs_ordered[q_no],query_ids[q_no],true_doc_IDs,k)

		#Fill in code here
        meanRecall=sr/len(query_ids)
		#Fill in code here
        return meanRecall
    
    def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""
        fscore = -1
        precision=self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
        recall=self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
        if precision==0 or  recall==0:
            fscore=0
        else:
            fscore=(2*precision*recall)/(precision+recall)
		#Fill in code here
        return fscore
    
    def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
        """
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""
        meanFscore = -1
        sf=0
        for q_no in range(len(query_ids)):
            true_doc_IDs = []
            for query_dict in qrels:
                if int(query_dict['query_num']) == query_ids[q_no]:
                    true_doc_IDs.append(int(query_dict['id']))
            sf+=self.queryFscore(doc_IDs_ordered[q_no],query_ids[q_no],true_doc_IDs,k)
		#Fill in code here
        meanFscore=sf/len(query_ids)
        return meanFscore
    
    def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""
        nDCG = -1
        true_doc_id_list=[]
        #print(true_doc_IDs)
        for t_id in true_doc_IDs:
            true_doc_id_list.append(int(t_id['id']))
        query_score=relScore(query_doc_IDs_ordered[:k],true_doc_IDs)
        ideal_score = relScore(true_doc_id_list,true_doc_IDs)
        if sorted(ideal_score,reverse=True)[0]==0:
            nDCG=0
        else:
            nDCG=dcg(query_score)/dcg(sorted(ideal_score,reverse=True)[:k])
            
		#Fill in code here
        return nDCG
    def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
        """
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""
        meanNDCG = -1
        s_ndcg=0
        #ndcg_list=[]
        for  q_no in range(len(query_ids)):
            rel_list = []
            for query_dict in qrels:
                if int(query_dict['query_num']) == query_ids[q_no]:
                    rel_list.append(query_dict)
            ndcg=self.queryNDCG(doc_IDs_ordered[q_no], query_ids[q_no], rel_list, k)
            s_ndcg+=ndcg
            
        meanNDCG=s_ndcg/len(query_ids)
		#Fill in code here
        return meanNDCG
    
    def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""
        avgPrecision = -1
        counter = 1
        sp=0
        for q_no in range(k):
            if query_doc_IDs_ordered[q_no] in true_doc_IDs:
                counter+=1
                sp+=self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, q_no+1)
            else:
                counter=k
                break
        avgPrecision = sp/counter

		#Fill in code here
        return avgPrecision
    
    def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
        """
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""
        meanAveragePrecision = -1
        sap=0
        for q_no in range(len(query_ids)):
            true_doc_IDs = []
            for query_dict in q_rels:
                if int(query_dict['query_num']) == query_ids[q_no]:
                    true_doc_IDs.append(int(query_dict['id']))
            sap+=self.queryAveragePrecision(doc_IDs_ordered[q_no],query_ids[q_no],true_doc_IDs,k)

		#Fill in code here
        meanAveragePrecision = sap/len(query_ids)
        return meanAveragePrecision

