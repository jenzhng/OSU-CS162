# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 2/15/2023
# Description: Recursive function named row_puzzle that takes a list of integers (the row)
#              as a parameter and returns True if the puzzle is solvable for that row,
#              but returns False otherwise

def row_puzzle(row_arr):
    """
    Takes a list of integers (the row)
    as a parameter and returns True if the puzzle is solvable for that row,
    but returns False otherwise
    :param row_arr:
    :return:
    """
    
    if row_arr[0] == 0:
        return True
    if len(row_arr) == 2 and row_arr[0] == 1:
        return True
    if (len(row_arr)) == row_arr[0]:
        return False
    if (len(row_arr)) < row_arr[0]:
        return False
    if row_arr[0] != 0:

        return row_puzzle(row_arr[row_arr[0]:])
    else:
        return False

def main():
    sample_row2 = [2, 4, 5, 3, 1, 3, 1, 4, 0]
    sample_row = [1, 3, 2, 1, 3, 4, 0]
    print(row_puzzle(sample_row2))

if __name__ == '__main__':
    main()
