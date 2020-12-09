import contractions
import numpy as np
import pandas as pd
from langdetect import detect

# 25999
df = pd.read_excel(r'C:\Users\shrinidhi.mahishi\OneDrive - Happiest Minds Technologies Limited\Documents\TMF\Cleaned\All_Incident_TAC_Cleaned_2.xls')
# df['Categorization Tier 1'].value_counts()

def isEnglish_ols(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def isEnglish(s):
    print(s)
    res = True
    try:
        res = detect(s) == 'en'
    except Exception:
        return False
    else:    
        return res    

def lengthCheck(s):
    if len(s) > 2:
        return True
    return False    


def clean_text(utterance):
    utterance = re.sub('[^a-zA-Z]', ' ', utterance)
    utterance = contractions.fix(utterance)    
    utterance =  re.sub(r"\b[a-zA-Z]\b", "", utterance)
    pattern = r'^\s*|\s\s*'
    return re.sub(pattern, ' ', utterance).strip()    


def process_stmts(df):
len(df)
    # 25999    
    df = df[df['Summary'].notnull()]

    # 25999
    # df = df[df['Categorization Tier 1'].notnull()]

    # # 33768
    # df = df[df['Ops cat 2'].notnull()]

    # # 33759
    # df = df[df['Ops cat 3'].notnull()]

    # # 33487
    # df = df[df['Product Categorization Tier 1'].notnull()]

    # # 33479
    # df = df[df['Prod Cat 2'].notnull()]

    # # 33475
    # df = df[df['Prod cat 3'].notnull()]
    
    # 25995
    df = df[df['Summary'].apply(lambda x: lengthCheck(x))]

    df = df[df['Summary'].apply(lambda x: isEnglish(x))]    

    df.reset_index(drop=True, inplace = True)

    # df = df[['Summary','Categorization Tier 1','Ops cat 2','Ops cat 3','Product Categorization Tier 1','Prod Cat 2','Prod cat 3']]
    # df.rename(columns={"Categorization Tier 1": "Ops cat 1", "Product Categorization Tier 1": "Prod cat 1", "Prod Cat 2":"Prod cat 2"}, inplace = True)
    return df

df = process_stmts(df)

df.to_excel(r"C:\Users\shrinidhi.mahishi\OneDrive - Happiest Minds Technologies Limited\Documents\TMF\Cleaned\All_Incident_TAC_Cleaned_3.xlsx", index = False) 

# df['Ops cat 1'].value_counts()
