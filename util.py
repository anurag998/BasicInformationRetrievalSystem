# Add your import statements here
import numpy as np


'''
Function giving relevance score to the documets of the range [0,5] with 5 being most relevant and 0 being least relevant.
'''
def relScore(pred,rel):
    score=[]
    for p_id in pred:
        p=0
        for q_id in rel:
            if int(q_id['id'])==p_id:
                p=1
                score.append(5-int(q_id['position']))
                break
        if p==0:
            score.append(0)
            
    return score

'''
Function calcualtes the discounted cumulative gain on the list of scores to be used by the nDCG fucntion in Evaluation.py.
'''
def dcg(scoreList):
    s_cg=0
    for i in range(len(scoreList)):
        s_cg+=(scoreList[i])/(np.log2(i+2))
        
    return s_cg






# Add any utility functions here