'''
This is where all nlp funcs go

global variables are only global for one modulelen
'''

def readFile():
    with open('alice.txt','r',encoding='utf-8',errors=None) as f:
        for line in f:
            words = line.split()
            for word in words:
                std_word_freq[word.lower()]=std_word_freq.get(word.lower(),0) +1
  

import string
alice_punc = sting.punctuation
'''
def optionOne():
    resultOne = len(contents.split())
    print(f'The text has {resultOne} raw words.')

def optionTwo():
    print('')

def optionThree():
    print('')

def optionFour():
    print('')

def optionFive():
    print('')

def optionSix():
    i= set([‘a’,’e’,’i’,’o’,’u’])
    e= set([‘a’,’e’,’i’,’o’,’u’])
    
    if  i.intersection(word) == true and e.intersection(word) == false:

    
    print('')

def optionSeven():
    print('')

'''
