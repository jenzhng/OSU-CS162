# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 2/15/2023
# Description: Function is_decreasing that takes parameter a list of numbers.
#              Function should return True if elements are in decreasing order,
#              but return False otherwise.



def is_decreasing(list1):
    """
    Function should return True if elements are in decreasing order.
    :param list1:
    :return:
    """
    if len(list1) == 1 or len(list1) == 0:
        return True
    return list1[0] >= list1[1] and is_decreasing(list1[1:])

def main():
    list1 = [4, 3, 2, 1]
    print(is_decreasing(list1))

if __name__ == '__main__':
    main()
