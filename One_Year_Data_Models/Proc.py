import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer 

df = pd.read_excel(r'C:\Users\shrinidhi.mahishi\OneDrive - Happiest Minds Technologies Limited\Documents\TMF\Cleaned\All_Incident_TAC_Cleaned.xlsx')

def find_common_words(corpus, n=1,k=1):    
    vec = CountVectorizer(ngram_range=(k,k),stop_words = 'english').fit(corpus)     
    bag_of_words = vec.transform(corpus)     
    sum_words = bag_of_words.sum(axis=0)      
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]     
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True) 
    return words_freq

corpus = ['india won match', 'india 100B strong', 'i won cup']
wrds=find_common_words(corpus)[:50]
wrds=find_common_words(df['Summary'])[:50]