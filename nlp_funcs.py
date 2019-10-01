'''
This is where all nlp funcs go

global variables are only global for one modulelen
'''

def readFile():
    global file
    global contents
    try:
        file = open('alice.txt','r')
        contents = file.read()
    finally:
        file.close()

readFile()

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

