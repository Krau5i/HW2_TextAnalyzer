# HW2 Text Analyzer

Create a program that answers questions about word and character usage in the plain text version of Alice in Wonderland (herein AiW), to be posted on Canvas. Organize your code into three modules, submitted in a single .zip file:

• aiw.py — Contains the main loop of the program, and defines no functions. Imports alice_funcs.py and nlp_funcs.py.

• aiw_funcs.py — Defines functions intended to be used only for this homework assignment.

• nlp_funcs.py — Defines functions that could be used in other word and character usage programs (NLP stands for Natural Language Processing). nlp_funcs will contain a routine called read_file which alice.py will use to read in AiW.
Program requirements:

The main loop gives the user the option of making an inquiry about Aiw, or exiting the program.

If the user chooses to make an inquiry, they enter a loop where they can choose one of the options below, or return to the main menu.

1. Show the number of distinct raw words in AiW, where a raw word is considered to be any sequence of symbols delimited by white space.

2. Show the number of standardized words in AiW, where a standardized word is a raw word with any upper case characters converted to lower case, and without punctuation marks other than an apostorphe("'") or dash ("-"). Hyphenation examples: "child-life" and "after-time" are considered to be one word, but "reality--the" and "it--once" are considered to be two.

3. Show counts for some of the most frequently used characters, listed in order of decreasing frequency. For example, the user can ask to see the counts for the 5 most frequently used characters.

4. Show counts for some of the most frequently used raw or standardized words, listed in order of decreasing frequency. For example, the user can ask to see the counts for the 2 most frequently used standardized words.

5. Show all the standardized words that occur a specified number of times in AiW. For example, show all the words that occur only once.

6. Show the longest and shortest raw or standardized words that contain every character in a list, and do not contain any character in another list. For example, the user can ask to see the longest and shortest raw words that contain '?' and 'A', and do not contain 'o', 'u', or 'e'.

7. List the frequency counts for a specified number of raw or standardized words that start with a particular string. For example, the user may ask for frequency counts for at most 10 raw words, listed in Unicode order, that start with the string "(B". Use binary search to find the first string to be displayed to the user.

Analyze the text using regular expressions, details to come.
