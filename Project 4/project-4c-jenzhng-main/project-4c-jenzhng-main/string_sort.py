# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 2/2/2023
# Description: Modified insertion sort to sort list of strings instead of numbers. 
#              Sorts list "in place".


def string_sort(str_list):
    '''
    Sorts str_list in alphabetical order and ignores case.
    '''
    for index in range(1, len(str_list)):
        value = str_list[index]
        pos = index - 1

     
        while pos >= 0 and value.lower() < str_list[pos].lower():
            str_list[pos + 1] = str_list[pos]
            pos -= 1
        str_list[pos + 1] = value
