
# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 2/15/2023
# Description: Function named is_subsequence that takes two string parameters
#              and returns True if the first string is a subsequence of the
#              second string, but returns False otherwise.

def is_subsequence (string1, string2):
    """
    Function should return True if first string parameter is subsequence of
    second string parameter
    :param list1:
    :return:
    """
    if string1 == "":
        return True
    if string2 == "":
        return False
    if string1[0] == string2[0]:
        return is_subsequence(string1[1:], string2[1:])
    return is_subsequence(string1, string2[1:])

def main():
    str_1 = "yc"
    str_2 = "yuna"
    print(is_subsequence (str_1, str_2))

if __name__ == '__main__':
    main()
