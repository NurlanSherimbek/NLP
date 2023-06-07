# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 20:42:13 2023

"""

import pandas as pd


from sklearn.base import BaseEstimator, TransformerMixin
import zeyrek



class text_tokenize2text_lem(BaseEstimator, TransformerMixin):
    def __init__(self ):
        self.analyzer = zeyrek.MorphAnalyzer()
        return
    def fit(self, X, y = None):
        return self
    
    def transform(self, X):
        X['lem_text']=X['tokenize_text'].apply(self.lemmatize_string)
        
        return X
    
    def lemmatize_string(self, s):
        tokens=s.split(sep=' ')
        
        tokens1=[]
        for i in tokens:
            
            try:
                t=self.analyzer.lemmatize(i)[0][1][0]
            except:
                continue
            tokens1.append(t)     
        tokens=tokens1
        
        if len(tokens)==0:
            return ''
        tokens=' '.join(tokens)
        return tokens
        
        
if __name__ == '__main__':
    df=pd.read_excel('Data_token.xlsx')
    transformer=text_tokenize2text_lem()
    transformer=transformer.fit(df)
    df1=transformer.transform(df)
    df1.to_excel('Data_lem.xlsx')
    

            
    