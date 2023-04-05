
# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 2/15/2023
# Description: Function list_max that returns maximum value in list.
#               If multiple elements of the list are tied for the maximum,
#               return that value.

def list_max(list1):
    """
    Returns maximum value in list parameter
    :param list1: 
    :return: 
    """
    if len(list1) == 1:
        return list1[0]
    else:
        num_1 = list_max(list1[1:])
        if (num_1) > (list1[0]):
            return num_1
        if (num_1) == (list1[0]):
            return num_1
        else:
            return list1[0]

def main():
    list1 = [1, 3, 100, 2]
    print(list_max(list1))

if __name__ == '__main__':
    main()
