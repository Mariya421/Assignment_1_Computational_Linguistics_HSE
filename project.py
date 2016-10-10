# coding: utf8
import nltk.data
from nltk.probability import FreqDist
import re

from functions import *

# openning the file
f = open('input.txt')
raw_text = f.read()
# print(raw_text)

# preprocessing text
my_text = text_preprocessing(raw_text)       
# print('prepocessed text:\n', my_text)

# getting sorted dictionary with word frequencies
my_list_of_tuples, my_dict = sorted_dict(my_text)
# print('sorted list of tuples:\n', my_list_of_tuples)
# print('dict:\n', my_dict)

# transforming sorted dictionary into normal output
my_output_word_frequency = word_frequency_list(my_list_of_tuples)
# print('my output word_frequency:\n', my_output_word_frequency)

# get max supr inf
my_supr, my_inf = max_supr_inf(my_dict)
# print('supr, inf:\n', my_supr, my_inf)

my_output_words_in_range, my_list_of_words_in_range = selecting_words_with_certain_frequencies(my_output_word_frequency, my_supr, my_inf)
# print('my_output_words_in_range:\n', my_output_words_in_range)

my_list_of_words_in_range = my_list_of_words_in_range.split()
# print('my_list_of_words_in_range:\n', my_list_of_words_in_range)
        
# loop which goes on till the very last attempt to try
counter_pc = 0
counter_usr = 0
while True:
        
    # random element
    word = random_element(my_list_of_words_in_range)
    # print('random_word:\n', word)

    # getting tokens
    tokens = nltk.word_tokenize(my_text)
    # print(tokens)

    # Create your bigrams
    bgs = nltk.bigrams(tokens)
    # print(bgs)

    # compute frequency distribution for all the bigrams in the text
    fdist = nltk.FreqDist(bgs)
    # print(fdist)
    local_dict = {}
    for k,v in fdist.items():# k - tuple (word, word), v - its frequency
        if k[0] == word or k[1] == word:
            local_dict[k] = v
    sorted_local_dict = sorted(local_dict.items(), key = lambda x : x[1], reverse = True)
    # print(sorted_local_dict, type(sorted_local_dict))
    final_local_dict = sorted_local_dict[:3]
    # print('final_local_dict', final_local_dict)

    first_bgr = final_local_dict[2]
    second_bgr = final_local_dict[1]
    third_bgr = final_local_dict[0]
    # print('selected bgrms:\n', first_bgr, second_bgr, third_bgr)

    # processing every tuple: unpacking it and making hints
    first_hint = unpacking_bgrms(first_bgr, word)
    second_hint = unpacking_bgrms(second_bgr, word)
    third_hint = unpacking_bgrms(third_bgr, word)
    # print('hints:\n')
    # print(first_hint, second_hint, third_hint)
             
    while True:
        print('First attempt! Try to guess the word marked with "____" in the example you see below:\n')
        print(first_hint)
        first_guess = input('What is the word?\n')
        print("You've typed the word '{}'".format(first_guess))
        if first_guess == word:
            print("you've guessed it right!")
            counter_usr += 1
            break
        if first_guess != word:
            print("you've guessed it wrong!\n")

        print("You've used your first attempt. Here comes the second one!\n")
        print('Try to guess the word marked with "____" in the example you see below:\n')
        print(second_hint) 
        second_guess = input('What is the word?\n')   
        print("You've typed the word '{}'".format(second_guess))
        if second_guess == word:
            print("you've guessed it right!")
            counter_usr += 1
            break
        if second_guess != word:
            print("you've guessed it wrong!\n")

        print("You've used your second attempt. Here comes the last one!\n")
        print('Try to guess the word marked with "____" in the example you see below:\n')
        print(third_hint) 
        third_guess = input('What is the word?\n')   
        print("You've typed the word '{}'".format(third_guess))
        if third_guess == word:
            print("you've guessed it right!")
            counter_usr += 1
            break
        if third_guess != word:
            print("you've guessed it wrong!\n")
            counter_pc += 1
            break
        
    print("The round is over!\n")
    if counter_pc > counter_usr:
        print("Yet, your laptop wins with {}:{} draw :P".format(counter_usr, counter_pc))
    if counter_pc < counter_usr:
        print("So far you are doing good with {}:{} draw :P".format(counter_usr, counter_pc))
    if counter_pc == counter_usr:
        print("Well..you're doing not bad with {}:{} draw :P".format(counter_usr, counter_pc))
