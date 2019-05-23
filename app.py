import string
import glob
from nltk import sent_tokenize
from nltk import tokenize
import pandas as pd
import re

def sentence_extract_summarize(input_file):
    """
    This function will take a text file as a input and give output of a clean text file 
    containing sentences and a summary of the text file
    """
    key_words1 = [  "research and development",
                    "R&D",
                    "product development",
                    "research, engineering, and development",
                    "research and product development",
                    "research development",
                    "research project",
                    "research and evaluation project",
                    "research program"
                    "research collaboration",
                    "research facility",
                    "research facilities",
                    "research initiative",
                    "research venture",
                    "research center",
                    "conduct research",
                    "new technology", 
                    "joint research",
                    "develop technology",
                    "entering development",
                    "developing new products",
                    "development of new products",
                    "research operations",
                    "research pipeline",
                    "product engineering",
                    "technology development",
                    "technical development",
                    "technology milestone",
                    "technology breakthrough",
                    "technological breakthrough",
                    "breakthrough innovation"
                    "clinical candidate"
                    "product candidate",
                    "drug candidate",
                    "breakthrough in",
                    "developing new technologies",
                    "development of proprietary technology",
                    "established a collaboration",
                    "projects in development",
                    "completion of key milestones",
                    "continuing development of",
                    "preclinical development",
                    "preclinical data",
                    "evaluating the potential of",
                    "clinical data",
                    "clinical development",
                    "clinical program",
                    "clinical study",
                    "safety study",
                    "pilot study",
                    "announced a collaboration",
                    "joint venture to develop",
                    "collaborative initiative"
                    "collaborative research",
                    "research collaborative",
                    "new patent",
                    "applied for patent",
                    "claims in this patent",
                    "filed patent",
                    "granted a patent",
                    "issued a patent",
                    "received a patent",
                    "patent was awarded",
                    "key patent",
                    "important patent",
                    "patents pending",
                    "applications pending"
                ]

    key_words2 = [   "will",
                    "could",
                    "should",
                    "expect",
                    "anticipate",
                    "plan",
                    "hope",
                    "believe",
                    "can",
                    "may",
                    "might",
                    "intend",
                    "project",
                    "forecast",
                    "objective",
                    "goal"
                ]


    out_files = 'sen-extractor/'+str(input_file)


    
    fn = []
    nos = []
    nos1 = []
    nos1_n = []
    nos1_nos2 = []
    nok1 = [] 
    
    fn.append(input_file)
    
    
    # opening file
    with open(input_file,'r') as f:
        data = f.read()
        data = " ".join(data.split())
     
    new_sents = []
    # extracting sentences
    sentences = sent_tokenize(data)
    
    # preprocessing sentences and writing in a output file
    
    for sen in sentences:
        sen = sen.replace("\n", " ")
        sen = " ".join(sen.split())
        words_per_sentence = sen.split()
        no_words_per_sentence = len(words_per_sentence)
        if no_words_per_sentence > 8:
            new_sents.append(sen)
        if '<Header>' not in sen:
                    new_sents.append(sen)
    
                
    with open(out_files, 'w') as file:
        for sen in new_sents:
            file.writelines(sen)
            file.writelines('\n')
        
   
    sentence_keywords1 = set()
    sentence_keywords1_num = set()
    
    sentence_keywords = set()
    key_list1 = []
    
    total_number_sentence = len(ano_new)
    nos.append(total_number_sentence)
    
    # summarizing result
    
    for sen in new_sents:
        sen = sen.lower()
        for word in key_words1:
            if word in sen:
                sentence_keywords1.add(sen)
                
        numbers = [int(s) for s in sen.split() if s.isdigit()]
                
        for word in key_words1:
            if word in sen and len(numbers) > 0:
                sentence_keywords1_num.add(sen)


        for word in key_words1:
            if word in sen:
                for w in key_words2:
                    if w in sen:
                        sentence_keywords.add(sen)

                
        for word in key_words1:
            if word in sen:
                key_list1.append(word)
        
       

    total_number_sentence_keywords1 = len(sentence_keywords1)
    sentences_k1_num = len(sentence_keywords1_num)
   
    nos1_n.append(sentences_k1_num)
    nos1.append(total_number_sentence_keywords1)
    nos1_nos2 = len(sentence_keywords)
    nok1 = len(key_list1)
        
        
    result = pd.DataFrame({
        "filename": fn,
        "Number of sentences": nos,
        "Number of sentences with keyword list1 (Any word/words in keyword list 1)": nos1,
        "Number of sentences with keyword list1 and also numerical information that is NOT a date": nos1_n,
        "Number of sentences with BOTH keyword list1 and keyword list2 (Any word/words in keyword1 & any word/words in keyword2)": nos1_nos2,
        "Number of keywords in keyword list1": nok1
    })
    
    result.to_csv("output.csv", index=False, mode='a', header=False)
    
    


# write your file name in the list below
# file_name = ['Sample1.txt', 'Sample2.txt']
path = '*.txt'
file_name = glob.glob(path)

for file in file_name:
    sentence_extract_summarize(file)