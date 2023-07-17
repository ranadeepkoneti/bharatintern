#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.corpus import words
from nltk.metrics.distance import edit_distance
nltk.download('words')


# In[2]:


def find_closest_word(word):
    word_list = words.words()
    min_distance = float('inf')
    closest_word = None
    
    for w in word_list:
        distance = edit_distance(word, w)
        if distance < min_distance:
            min_distance = distance
            closest_word = w
    
    return closest_word


# In[3]:


input_word = "aple"
closest_word = find_closest_word(input_word)
print("Input word:", input_word)
print("Closest word:", closest_word)


# In[ ]:




