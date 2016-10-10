import re
import random

# getting lower case
lower_case = lambda text : text.lower()

# cleaning text from punctuation
remove_punctuation = lambda text : re.sub(r'[^\w\s]', r'', text)

# cleaning text from digits
remove_digits = lambda text : re.sub(r'[\d]', r'', text)

# cleaning text from double spaces
remove_double_spaces = lambda text : " ".join(text.split())

# random element of a list
random_element = lambda local_list : random.choice(local_list)

def text_preprocessing(local_text):
    local_text = lower_case(local_text)
    local_text = remove_punctuation(local_text)
    local_text = remove_digits(local_text)
    local_text = remove_double_spaces(local_text)
    return local_text

# the function returns 2 arguments: 
# sorted_local_dict - list of tuples which preserves order of the words by ther frequency
# new_local_dict - dict which showes connection between a word and its frequency
# the mainn difference is in the absence of order in the case of new_local_dict
def sorted_dict(local_text):
    local_list = local_text.split()
    unique_items = set(local_list)
    sorted_local_dict = dict()
    for i in unique_items:
        counter = 0
        counter = local_list.count(i)
        sorted_local_dict[i] = counter
    sorted_local_dict = sorted(sorted_local_dict.items(), key = lambda x : x[1], reverse = True)
    new_local_dict = dict()
    for pair in sorted_local_dict:
        new_local_dict[pair[0]] = pair[1]
    return sorted_local_dict, new_local_dict
    
def word_frequency_list(local_dict):
    local_output = 'Word frequency from the biggest to the smallest:\n'
    for pair in local_dict:
        local_output = local_output + '{}:{}\n'.format(pair[0], pair[1])
    return local_output

def max_supr_inf(local_dict):
    # getting max frequency, rounding supremum and infinum
    local_list = []
    for i in local_dict:
        local_list.append(local_dict[i])
    m = max(local_list)
    inf = m*0.02
    supr = m*0.15
    # print('The max frequency is {}, supremum - {}, infinum - {}'.format(m, supr, inf))
    # print('rounding supremum and infinum')
    inf = round(inf, 0)
    supr = round(supr, 0)
    # print('Rounded: the max frequency is {}, supremum - {}, infinum - {}'.format(m, supr, inf))
    return supr, inf
    '''
    inf = 0
    supr = 2
    
    # for i in range (inf+1, supr):
    for y in local_dict:    # for every element of a dict
        print('dict elements for search', y)
        if local_dict[y] in range(inf+1, supr):  # if value of a certain word (=frequency) is within limiters
            print('the article suits')
            print(list(local_dict.keys())[list(local_dict.values()).index(local_dict[y])])  # print key of the word
    
    return 0
    '''
# output of this function:
# local_output - entry words + str of words frequencies within a range
# local_putput_2 - str of words frequencies within a range
def selecting_words_with_certain_frequencies(local_input, local_supr, local_inf):
    local_inf = int(local_inf)
    local_supr = int(local_supr)
    # local_inf = 0
    # local_supr = 2
    local_input = local_input.split('\n')
    local_input = local_input[1:-1] # remove 1st and -1st elements (they are irrelevant)
    # print('local input', local_input)
    local_output_1 = 'Words with frequencies within the range:\n'
    local_output_2 = ''
    for i in local_input:
        # print('i', i)
        pair = i.split(':') #
        # print('pair 0 and 1:', pair[0], pair[1], type(pair[1]))
        pair[1] = int(pair[1])
        if pair[1] in range(local_inf+1, local_supr):   # we stopped here use print to see the problems
            # print('word in range', pair)
            local_output_2 += pair[0] + ' '
    if local_output_2 == '':
        local_output_2 = 'None'
    local_output = local_output_1 + local_output_2    
    return local_output, local_output_2

def unpacking_bgrms(local_bgr, local_word):
    local_bgr = local_bgr[0] # getting bgr itself
    local_bgr = list(local_bgr)
    if local_bgr[0] == local_word:
        local_bgr[0] = '____ '
    if local_bgr[1] == local_word:
        local_bgr[1] = ' ____'
    local_bgr = local_bgr[0] + local_bgr[1]
    return local_bgr

'''
# preprocessing text
my_text = text_preprocessing('Маша и маша "пришли" *** 54543 ДоМой!')       
print('prepocessed text:\n', my_text)

# getting sorted dictionary with word frequencies
my_list_of_tuples, my_dict = sorted_dict(my_text)
print('sorted list of tuples:\n', my_list_of_tuples)
print('dict:\n', my_dict)

# transforming sorted dictionary into normal output
my_output_word_frequency = word_frequency_list(my_list_of_tuples)
print('my output word_frequency:\n', my_output_word_frequency)

# get max supr inf
my_supr, my_inf = max_supr_inf(my_dict)
print('supr, inf:\n', my_supr, my_inf)

my_output_words_in_range, my_list_of_words_in_range = selecting_words_with_certain_frequencies(my_output_word_frequency, my_supr, my_inf)
print('my_output_words_in_range:\n', my_output_words_in_range)

my_list_of_words_in_range = my_list_of_words_in_range.split()
print('my_list_of_words_in_range:\n', my_list_of_words_in_range)

# random element
random_word = random_element(my_list_of_words_in_range)
print('random_word:\n', random_word)
'''
