#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')


# In[2]:


def extract_keywords(resume_text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(resume_text.lower())
    keywords = [token for token in tokens if token.isalpha() and token not in stop_words]
    return keywords


# In[3]:


def find_matching_candidates(resume_text, desired_skills):
    resume_keywords = extract_keywords(resume_text)
    matching_candidates = []
    for candidate in desired_skills:
        candidate_keywords = extract_keywords(candidate)
        intersection = set(resume_keywords) & set(candidate_keywords)
        if len(intersection) > 0:
            matching_candidates.append(candidate)
    return matching_candidates


# In[4]:


desired_skills = [
    "Python programming",
    "Data analysis",
    "Machine learning",
    "Communication skills"
]

resume1 = "I have experience in Python programming and data analysis."
resume2 = "I am skilled in machine learning and have strong communication skills."
resume3 = "I have expertise in Java programming and database management."

matching_candidates = find_matching_candidates(resume1, desired_skills)
print("Matching candidates for resume 1:", matching_candidates)

matching_candidates = find_matching_candidates(resume2, desired_skills)
print("Matching candidates for resume 2:", matching_candidates)

matching_candidates = find_matching_candidates(resume3, desired_skills)
print("Matching candidates for resume 3:", matching_candidates)


# In[ ]:




